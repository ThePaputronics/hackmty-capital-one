"""Simulated clock for time-accelerated financial stream replay."""

from datetime import datetime, timedelta
import time


class SimulatedClock:
    """Manages virtual timeline progression decoupled from wall-clock time."""

    def __init__(self, start_time: datetime, seconds_per_simulated_day: float = 6.0):
        self.current_time = start_time
        self.start_time = start_time
        self.seconds_per_day = seconds_per_simulated_day
        self._last_tick_wall_time = time.time()

    def set_time(self, new_time: datetime) -> None:
        """Manually advance clock without sleeping (used during warmup)."""
        self.current_time = new_time
        self._last_tick_wall_time = time.time()

    def advance(self, delta: timedelta) -> datetime:
        """Advance the simulated clock by delta and sleep proportionally to speed setting."""
        if self.seconds_per_day > 0:
            simulated_seconds = delta.total_seconds()
            sleep_duration = (simulated_seconds / 86400.0) * self.seconds_per_day
            if sleep_duration > 0.001:
                time.sleep(sleep_duration)
        self.current_time += delta
        self._last_tick_wall_time = time.time()
        return self.current_time

    @property
    def now(self) -> datetime:
        """Return the current simulated timestamp."""
        return self.current_time
