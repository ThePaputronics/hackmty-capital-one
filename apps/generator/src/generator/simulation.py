"""Simulation engine orchestrating warmup ledger creation and active test streams."""

from dataclasses import dataclass
from datetime import datetime, timedelta
import random
from typing import Any, Generator

from generator.clock import SimulatedClock
from generator.personas import Persona, PersonaFactory, generate_valid_clabe


@dataclass
class HiddenGroundTruth:
    """True nature of a proposed transaction (never leaked to Sentinel API)."""

    is_app_fraud: bool
    is_ato_fraud: bool
    playbook: str | None
    value_at_risk: float
    persona_type: str
    expected_outcome_on_pause: str  # e.g., "cancelled" if user cancels under friction


@dataclass
class PlannedTransfer:
    """A transfer to be evaluated along with preceding prerequisite events and hidden labels."""

    prerequisite_events: list[dict[str, Any]]
    evaluate_request: dict[str, Any]
    ground_truth: HiddenGroundTruth


class StreamSimulator:
    """Coordinates chronological event generation across all personas."""

    def __init__(
        self,
        start_date: datetime,
        warmup_days: int = 90,
        active_days: int = 30,
        seed: int = 42,
    ):
        random.seed(seed)
        self.start_date = start_date
        self.warmup_days = warmup_days
        self.active_days = active_days
        self.active_start_date = start_date + timedelta(days=warmup_days)

        self.personas: list[Persona] = []
        self._setup_cohort()

    def _setup_cohort(self) -> None:
        """Create a balanced cohort of legitimate users, small businesses, and attack targets."""
        # 30 Normal consumers
        for i in range(1, 31):
            self.personas.append(PersonaFactory.create_normal_payer(i, self.start_date))

        # 10 Small businesses / merchants (crucial for subgroup false-positive calibration)
        for i in range(1, 11):
            self.personas.append(PersonaFactory.create_small_merchant(i, self.start_date))

        # 8 Vulnerable targets subject to coercion playbooks
        for i in range(1, 9):
            self.personas.append(PersonaFactory.create_vulnerable_victim(i, self.start_date))

        # 4 Accounts targeted by credential/ATO attack
        for i in range(1, 5):
            self.personas.append(PersonaFactory.create_ato_target(i, self.start_date))

    def generate_warmup_events(self) -> list[dict[str, Any]]:
        """Generate historical baseline events over the 90-day warmup period in bulk."""
        events: list[dict[str, Any]] = []

        # 1. Register initial beneficiaries and devices
        for p in self.personas:
            for b in p.known_beneficiaries:
                events.append({
                    "payer_external_id": p.external_id,
                    "institution_code": p.institution_code,
                    "type": "beneficiary_added",
                    "occurred_at": b.created_at.isoformat(),
                    "payload": {
                        "destination_clabe": b.clabe,
                        "destination_institution_code": b.institution_code,
                        "alias": b.alias,
                    },
                })
            events.append({
                "payer_external_id": p.external_id,
                "institution_code": p.institution_code,
                "type": "device_seen",
                "occurred_at": (self.start_date + timedelta(days=1)).isoformat(),
                "payload": {"device_id": p.device_id},
            })

        # 2. Simulate historical settled transfers
        for day_offset in range(1, self.warmup_days):
            current_day = self.start_date + timedelta(days=day_offset)

            for p in self.personas:
                if p.persona_type == "merchant":
                    # Merchants transfer daily to 1-3 suppliers
                    num_tx = random.randint(1, 3)
                    for _ in range(num_tx):
                        b = random.choice(p.known_beneficiaries)
                        amt = round(random.uniform(800.0, 7500.0), 2)
                        p.current_balance = max(10000.0, p.current_balance - amt + random.uniform(500, 9000))
                        t_occ = current_day.replace(hour=random.randint(9, 19), minute=random.randint(0, 59))
                        events.append({
                            "payer_external_id": p.external_id,
                            "institution_code": p.institution_code,
                            "type": "transfer_settled",
                            "occurred_at": t_occ.isoformat(),
                            "payload": {
                                "amount": amt,
                                "destination_clabe": b.clabe,
                                "destination_institution_code": b.institution_code,
                                "balance_after": round(p.current_balance, 2),
                            },
                        })
                else:
                    # Consumers transfer every 3-5 days
                    if random.random() < 0.25 and p.known_beneficiaries:
                        b = random.choice(p.known_beneficiaries)
                        amt = round(random.uniform(200.0, 3200.0), 2)
                        p.current_balance = max(2000.0, p.current_balance - amt + random.uniform(0, 4000))
                        t_occ = current_day.replace(hour=random.randint(10, 21), minute=random.randint(0, 59))
                        events.append({
                            "payer_external_id": p.external_id,
                            "institution_code": p.institution_code,
                            "type": "transfer_settled",
                            "occurred_at": t_occ.isoformat(),
                            "payload": {
                                "amount": amt,
                                "destination_clabe": b.clabe,
                                "destination_institution_code": b.institution_code,
                                "balance_after": round(p.current_balance, 2),
                            },
                        })

        # Sort warmup events chronologically
        events.sort(key=lambda x: x["occurred_at"])
        return events

    def generate_active_day_transfers(self, day_num: int) -> list[PlannedTransfer]:
        """Generate all planned transfers for a specific day in the 30-day active stream."""
        planned: list[PlannedTransfer] = []
        current_day = self.active_start_date + timedelta(days=day_num)

        # 1. Normal daily routine transfers (Genuine - Expected Allow)
        for p in self.personas:
            if p.persona_type == "normal":
                if random.random() < 0.20:
                    b = random.choice(p.known_beneficiaries)
                    amt = round(random.uniform(250.0, 2800.0), 2)
                    t_time = current_day.replace(hour=random.randint(9, 20), minute=random.randint(0, 59))
                    planned.append(
                        PlannedTransfer(
                            prerequisite_events=[],
                            evaluate_request={
                                "payer_external_id": p.external_id,
                                "institution_code": p.institution_code,
                                "amount": amt,
                                "currency": "MXN",
                                "destination_clabe": b.clabe,
                                "destination_institution_code": b.institution_code,
                                "proposed_at": t_time.isoformat(),
                                "session": {
                                    "device_id": p.device_id,
                                    "is_new_device": False,
                                    "ip_risk": "low",
                                    "geo_risk": "low",
                                },
                                "context": {
                                    "active_call": False,
                                    "screen_share": False,
                                    "remote_access": False,
                                },
                            },
                            ground_truth=HiddenGroundTruth(
                                is_app_fraud=False,
                                is_ato_fraud=False,
                                playbook=None,
                                value_at_risk=amt,
                                persona_type="normal",
                                expected_outcome_on_pause="continued",
                            ),
                        )
                    )

            elif p.persona_type == "merchant":
                # Merchants execute 1 to 2 supplier payouts daily
                num_tx = random.randint(1, 2)
                for _ in range(num_tx):
                    b = random.choice(p.known_beneficiaries)
                    amt = round(random.uniform(1200.0, 8500.0), 2)
                    t_time = current_day.replace(hour=random.randint(8, 18), minute=random.randint(0, 59))
                    planned.append(
                        PlannedTransfer(
                            prerequisite_events=[],
                            evaluate_request={
                                "payer_external_id": p.external_id,
                                "institution_code": p.institution_code,
                                "amount": amt,
                                "currency": "MXN",
                                "destination_clabe": b.clabe,
                                "destination_institution_code": b.institution_code,
                                "proposed_at": t_time.isoformat(),
                                "session": {
                                    "device_id": p.device_id,
                                    "is_new_device": False,
                                    "ip_risk": "low",
                                    "geo_risk": "low",
                                },
                                "context": {
                                    "active_call": False,
                                    "screen_share": False,
                                    "remote_access": False,
                                },
                            },
                            ground_truth=HiddenGroundTruth(
                                is_app_fraud=False,
                                is_ato_fraud=False,
                                playbook=None,
                                value_at_risk=amt,
                                persona_type="merchant",
                                expected_outcome_on_pause="continued",
                            ),
                        )
                    )

        # 2. Targeted Scam Attacks scheduled on designated days
        # Playbook 1: Structuring under MTU cap with Active Phone Call (Days 3, 10, 18, 25)
        if day_num in (3, 10, 18, 25):
            victim = [p for p in self.personas if p.persona_type == "victim"][(day_num % 8)]
            mule_clabe = generate_valid_clabe("072", f"888{day_num:02d}000000")
            t_base = current_day.replace(hour=11, minute=30)

            prereqs = [
                # Beneficiary added 5 minutes prior
                {
                    "payer_external_id": victim.external_id,
                    "institution_code": victim.institution_code,
                    "type": "beneficiary_added",
                    "occurred_at": (t_base - timedelta(minutes=5)).isoformat(),
                    "payload": {
                        "destination_clabe": mule_clabe,
                        "destination_institution_code": "072",
                        "alias": "Cuenta Segura Banxico",
                    },
                }
            ]

            planned.append(
                PlannedTransfer(
                    prerequisite_events=prereqs,
                    evaluate_request={
                        "payer_external_id": victim.external_id,
                        "institution_code": victim.institution_code,
                        "amount": 12450.00,  # Right under the 1,500 UDIs MTU cap (~$12,800)
                        "currency": "MXN",
                        "destination_clabe": mule_clabe,
                        "destination_institution_code": "072",
                        "proposed_at": t_base.isoformat(),
                        "session": {
                            "device_id": victim.device_id,
                            "is_new_device": False,
                            "ip_risk": "low",
                            "geo_risk": "low",
                        },
                        "context": {
                            "active_call": True,  # Scammer actively coaching victim on the phone
                            "screen_share": False,
                            "remote_access": False,
                        },
                    },
                    ground_truth=HiddenGroundTruth(
                        is_app_fraud=True,
                        is_ato_fraud=False,
                        playbook="mtu_structuring_active_call",
                        value_at_risk=12450.00,
                        persona_type="victim",
                        expected_outcome_on_pause="cancelled",  # 80% of victims cancel upon explicit warning
                    ),
                )
            )

        # Playbook 2: Moving the Line (MTU limit raise + huge transfer) (Days 7, 21)
        if day_num in (7, 21):
            victim = [p for p in self.personas if p.persona_type == "victim"][(day_num % 8)]
            mule_clabe = generate_valid_clabe("014", f"777{day_num:02d}000000")
            t_base = current_day.replace(hour=16, minute=15)

            prereqs = [
                {
                    "payer_external_id": victim.external_id,
                    "institution_code": victim.institution_code,
                    "type": "limit_changed",
                    "occurred_at": (t_base - timedelta(minutes=12)).isoformat(),
                    "payload": {"previous_limit": 15000.0, "new_limit": 60000.0},
                },
                {
                    "payer_external_id": victim.external_id,
                    "institution_code": victim.institution_code,
                    "type": "beneficiary_added",
                    "occurred_at": (t_base - timedelta(minutes=8)).isoformat(),
                    "payload": {
                        "destination_clabe": mule_clabe,
                        "destination_institution_code": "014",
                        "alias": "Fondo Emergencia",
                    },
                },
            ]

            planned.append(
                PlannedTransfer(
                    prerequisite_events=prereqs,
                    evaluate_request={
                        "payer_external_id": victim.external_id,
                        "institution_code": victim.institution_code,
                        "amount": 48500.00,
                        "currency": "MXN",
                        "destination_clabe": mule_clabe,
                        "destination_institution_code": "014",
                        "proposed_at": t_base.isoformat(),
                        "session": {
                            "device_id": victim.device_id,
                            "is_new_device": False,
                            "ip_risk": "low",
                            "geo_risk": "low",
                        },
                        "context": {
                            "active_call": True,
                            "screen_share": False,
                            "remote_access": False,
                        },
                    },
                    ground_truth=HiddenGroundTruth(
                        is_app_fraud=True,
                        is_ato_fraud=False,
                        playbook="limit_increase_coercion",
                        value_at_risk=48500.00,
                        persona_type="victim",
                        expected_outcome_on_pause="cancelled",
                    ),
                )
            )

        # Playbook 3: ATO Takeover Attack (Days 5, 15, 27)
        if day_num in (5, 15, 27):
            ato_p = [p for p in self.personas if p.persona_type == "ato"][(day_num % 4)]
            mule_clabe = generate_valid_clabe("127", f"999{day_num:02d}000000")
            t_base = current_day.replace(hour=2, minute=45)  # Nocturnal 2:45 AM

            prereqs = [
                {
                    "payer_external_id": ato_p.external_id,
                    "institution_code": ato_p.institution_code,
                    "type": "credential_changed",
                    "occurred_at": (t_base - timedelta(hours=2)).isoformat(),
                    "payload": {"method": "sms_otp_reset"},
                }
            ]

            planned.append(
                PlannedTransfer(
                    prerequisite_events=prereqs,
                    evaluate_request={
                        "payer_external_id": ato_p.external_id,
                        "institution_code": ato_p.institution_code,
                        "amount": 28000.00,
                        "currency": "MXN",
                        "destination_clabe": mule_clabe,
                        "destination_institution_code": "127",
                        "proposed_at": t_base.isoformat(),
                        "session": {
                            "device_id": f"hacker_device_vpn_{day_num}",
                            "is_new_device": True,
                            "ip_risk": "high",
                            "geo_risk": "high",
                        },
                        "context": {
                            "active_call": False,
                            "screen_share": False,
                            "remote_access": False,
                        },
                    },
                    ground_truth=HiddenGroundTruth(
                        is_app_fraud=False,
                        is_ato_fraud=True,
                        playbook="credential_hijack_nocturnal_ato",
                        value_at_risk=28000.00,
                        persona_type="ato",
                        expected_outcome_on_pause="cancelled",
                    ),
                )
            )

        # Sort daily planned transfers chronologically
        planned.sort(key=lambda x: x.evaluate_request["proposed_at"])
        return planned
