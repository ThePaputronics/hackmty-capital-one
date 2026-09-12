"""Seed a low-risk synthetic transfer case."""

from demo_cases.seed_helpers import DemoCase, SignalSeed, print_seed_summary, seed_demo_case

from app.database import SessionLocal, init_db

CASE = DemoCase(
    case_id="demo-low-risk",
    display_name="Low Risk Payer",
    balance=32_000,
    transfer_limit=10_000,
    baseline_avg_amount=2_500,
    baseline_max_usual_amount=8_000,
    baseline_daily_amount=4_000,
    baseline_daily_count=2,
    minimum_residual_balance=6_000,
    beneficiary_alias="Known rent account",
    beneficiary_change_type="reactivated",
    previous_limit=10_000,
    new_limit=10_000,
    transfer_amount=3_200,
    daily_amount_before=0,
    session_is_new_device=False,
    session_is_unusual=False,
    session_ip_risk="low",
    session_geo_risk="low",
    security_event_type=None,
    signals=(
        SignalSeed(
            signal_key="normal_amount",
            signal_group="transfer_amount",
            severity="low",
            risk_points=1,
            weight=0.1,
            observed_value="3200",
            baseline_value="avg=2500,max=8000",
            explanation="Transfer amount is within the payer baseline.",
            is_primary_signal=False,
        ),
    ),
)


def main() -> None:
    """Seed the low-risk case."""
    init_db()
    with SessionLocal() as db:
        evaluation = seed_demo_case(db, CASE)
        print_seed_summary("low-risk", evaluation)


if __name__ == "__main__":
    main()
