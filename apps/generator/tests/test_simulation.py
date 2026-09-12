"""Tests for simulation and synthetic generation."""

from datetime import datetime
from generator.simulation import StreamSimulator


def test_simulation_determinism_and_warmup():
    """Verify stream simulator produces consistent events with same random seed."""
    t0 = datetime(2026, 6, 1, 0, 0, 0)
    sim1 = StreamSimulator(start_date=t0, warmup_days=90, active_days=30, seed=42)
    warmup1 = sim1.generate_warmup_events()

    sim2 = StreamSimulator(start_date=t0, warmup_days=90, active_days=30, seed=42)
    warmup2 = sim2.generate_warmup_events()

    assert len(warmup1) > 500
    assert len(warmup1) == len(warmup2)
    assert warmup1[0]["occurred_at"] == warmup2[0]["occurred_at"]
    assert warmup1[-1]["occurred_at"] == warmup2[-1]["occurred_at"]


def test_active_day_generation_and_hidden_labels():
    """Verify active day generation produces planned transfers with hidden ground-truth labels."""
    t0 = datetime(2026, 6, 1, 0, 0, 0)
    sim = StreamSimulator(start_date=t0, warmup_days=90, active_days=30, seed=42)

    # Day 3 has scheduled MTU structuring coercion scam
    day3_transfers = sim.generate_active_day_transfers(day_num=3)
    assert len(day3_transfers) > 0

    scams = [t for t in day3_transfers if t.ground_truth.is_app_fraud]
    assert len(scams) == 1
    scam = scams[0]
    assert scam.ground_truth.playbook == "mtu_structuring_active_call"
    assert scam.evaluate_request["context"]["active_call"] is True
    assert len(scam.prerequisite_events) >= 1
