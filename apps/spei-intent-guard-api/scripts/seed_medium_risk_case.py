"""Seed a medium-risk synthetic transfer case."""

from app.database import SessionLocal, init_db
from demo_cases.seed_helpers import DemoCase, SignalSeed, print_seed_summary, seed_demo_case


CASE = DemoCase(
    case_id="demo-medium-risk",
    display_name="Medium Risk Payer",
    balance=28_000,
    transfer_limit=12_000,
    baseline_avg_amount=2_000,
    baseline_max_usual_amount=6_000,
    baseline_daily_amount=4_500,
    baseline_daily_count=2,
    minimum_residual_balance=5_000,
    beneficiary_alias="New contractor",
    beneficiary_change_type="created",
    previous_limit=12_000,
    new_limit=12_000,
    transfer_amount=9_500,
    daily_amount_before=0,
    session_is_new_device=False,
    session_is_unusual=True,
    session_ip_risk="medium",
    session_geo_risk="low",
    security_event_type=None,
    signals=(
        SignalSeed(
            signal_key="new_beneficiary",
            signal_group="beneficiary",
            severity="medium",
            risk_points=3,
            weight=0.35,
            observed_value="created_now",
            baseline_value="known_beneficiaries",
            explanation="The beneficiary was newly registered for this payer.",
        ),
        SignalSeed(
            signal_key="amount_above_baseline",
            signal_group="transfer_amount",
            severity="medium",
            risk_points=4,
            weight=0.4,
            observed_value="9500",
            baseline_value="max_usual=6000",
            explanation="The transfer amount is above the payer's usual maximum.",
        ),
        SignalSeed(
            signal_key="unusual_session",
            signal_group="session_device",
            severity="low",
            risk_points=1,
            weight=0.1,
            observed_value="true",
            baseline_value="false",
            explanation="The session pattern is unusual, but only as secondary context.",
            is_primary_signal=False,
        ),
    ),
)


def main() -> None:
    """Seed the medium-risk case."""
    init_db()
    with SessionLocal() as db:
        evaluation = seed_demo_case(db, CASE)
        print_seed_summary("medium-risk", evaluation)


if __name__ == "__main__":
    main()
