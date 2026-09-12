"""Generator bank-player loop and simulation metrics tracking."""

from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
import logging
import random
import time
from typing import Any
import httpx

from generator.clock import SimulatedClock
from generator.simulation import PlannedTransfer, StreamSimulator

logger = logging.getLogger("generator")


@dataclass
class SimulationStatus:
    """Current simulation status and ground-truth metrics (exposed via /sim/status)."""

    state: str = "idle"  # idle, warming_up, streaming, completed
    day: int = 0
    total_days: int = 30
    simulated_clock: str = ""
    speed_seconds_per_day: float = 6.0
    cancellation_probability_p: float = 0.85  # Declared assumption: p(cancel | pause)

    # Counters
    total_transfers_evaluated: int = 0
    genuine_transfers: int = 0
    merchant_transfers: int = 0
    app_scams_attempted: int = 0
    ato_attacks_attempted: int = 0

    # Detections & Value Protection
    app_scams_intercepted: int = 0
    app_scams_missed: int = 0
    ato_attacks_intercepted: int = 0

    total_value_at_risk_mxn: float = 0.0
    pesos_protected_mxn: float = 0.0

    # Subgroup False Alarms
    genuine_challenges: int = 0
    merchant_challenges: int = 0


class BankPlayer:
    """Simulates the bank client interacting with the Sentinel API."""

    def __init__(
        self,
        api_base_url: str = "http://localhost:8000",
        start_date: datetime | None = None,
        warmup_days: int = 90,
        active_days: int = 30,
        speed_seconds_per_day: float = 6.0,
        seed: int = 42,
        cancellation_p: float = 0.85,
    ):
        self.api_url = api_base_url.rstrip("/")
        self.start_date = start_date or datetime(2026, 6, 1, 0, 0, 0)
        self.warmup_days = warmup_days
        self.active_days = active_days
        self.speed = speed_seconds_per_day
        self.seed = seed
        self.cancellation_p = cancellation_p

        self.clock = SimulatedClock(self.start_date, seconds_per_simulated_day=self.speed)
        self.simulator = StreamSimulator(
            start_date=self.start_date,
            warmup_days=self.warmup_days,
            active_days=self.active_days,
            seed=self.seed,
        )

        self.status = SimulationStatus(
            state="idle",
            total_days=self.active_days,
            simulated_clock=self.start_date.isoformat(),
            speed_seconds_per_day=self.speed,
            cancellation_probability_p=self.cancellation_p,
        )
        self._http_client = httpx.Client(timeout=10.0)

    def run_warmup(self) -> int:
        """Transmit historical warmup events to the API to establish baseline histories."""
        self.status.state = "warming_up"
        warmup_events = self.simulator.generate_warmup_events()
        total = len(warmup_events)
        logger.info("Injecting %d warmup events in batches...", total)

        batch_size = 100
        for i in range(0, total, batch_size):
            batch = warmup_events[i : i + batch_size]
            res = self._http_client.post(f"{self.api_url}/v1/events", json={"events": batch})
            res.raise_for_status()

        self.status.state = "warmup_complete"
        self.clock.set_time(self.simulator.active_start_date)
        self.status.simulated_clock = self.clock.now.isoformat()
        logger.info("Warmup complete. %d events stored.", total)
        return total

    def play_active_stream(self) -> None:
        """Stream 30 days of live simulation, evaluating transfers and reporting outcomes."""
        self.status.state = "streaming"
        logger.info("Beginning 30-day active stream simulation...")

        for day_idx in range(1, self.active_days + 1):
            self.status.day = day_idx
            daily_transfers = self.simulator.generate_active_day_transfers(day_idx)
            day_start = self.simulator.active_start_date + timedelta(days=day_idx)

            for item in daily_transfers:
                prop_time = datetime.fromisoformat(item.evaluate_request["proposed_at"])

                # Advance simulated clock to the moment of this transfer
                if prop_time > self.clock.now:
                    time_diff = prop_time - self.clock.now
                    self.clock.advance(time_diff)
                    self.status.simulated_clock = self.clock.now.isoformat()

                # 1. Ingest prerequisite events (e.g. beneficiary added 4 mins prior)
                if item.prerequisite_events:
                    self._http_client.post(
                        f"{self.api_url}/v1/events",
                        json={"events": item.prerequisite_events},
                    )

                # 2. Call Sentinel API evaluate
                eval_res = self._http_client.post(
                    f"{self.api_url}/v1/evaluate",
                    json=item.evaluate_request,
                )
                if eval_res.status_code != 200:
                    logger.error("Evaluate error: %s", eval_res.text)
                    continue

                eval_data = eval_res.json()
                eval_id = eval_data["evaluation_id"]
                decision = eval_data["decision"]
                gt = item.ground_truth
                amt = float(item.evaluate_request["amount"])

                self.status.total_transfers_evaluated += 1

                # 3. Simulate customer response and determine outcome
                outcome = "continued"
                if gt.is_app_fraud:
                    self.status.app_scams_attempted += 1
                    self.status.total_value_at_risk_mxn += amt
                    if decision in ("pause", "challenge"):
                        self.status.app_scams_intercepted += 1
                        # Victim cancels when exposed to clear friction
                        if random.random() <= self.cancellation_p:
                            outcome = "cancelled"
                            self.status.pesos_protected_mxn += amt
                        else:
                            outcome = "continued"
                    else:
                        self.status.app_scams_missed += 1
                        outcome = "continued"

                elif gt.is_ato_fraud:
                    self.status.ato_attacks_attempted += 1
                    self.status.total_value_at_risk_mxn += amt
                    if decision == "pause":
                        self.status.ato_attacks_intercepted += 1
                        outcome = "verified_callback"
                        self.status.pesos_protected_mxn += amt
                    else:
                        outcome = "continued"

                else:
                    self.status.genuine_transfers += 1
                    if gt.persona_type == "merchant":
                        self.status.merchant_transfers += 1
                        if decision in ("challenge", "pause"):
                            self.status.merchant_challenges += 1
                    else:
                        if decision in ("challenge", "pause"):
                            self.status.genuine_challenges += 1
                    outcome = "continued"

                # 4. Report outcome back to API
                self._http_client.post(
                    f"{self.api_url}/v1/decisions/{eval_id}/outcome",
                    json={"outcome": outcome},
                )

        self.status.state = "completed"
        logger.info("Active simulation stream completed successfully.")
