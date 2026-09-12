"""Seed a high-risk synthetic transfer case."""

from app.database import SessionLocal, init_db
from demo_cases.seed_helpers import DemoCase, SignalSeed, print_seed_summary, seed_demo_case


CASE = DemoCase(
    case_id="demo-high-risk",
    display_name="High Risk Payer",
    balance=22_000,
    transfer_limit=20_000,
    baseline_avg_amount=1_800,
    baseline_max_usual_amount=5_000,
    baseline_daily_amount=3_500,
    baseline_daily_count=1,
    minimum_residual_balance=4_000,
    beneficiary_alias="Urgent new beneficiary",
    beneficiary_change_type="created",
    previous_limit=5_000,
    new_limit=20_000,
    transfer_amount=19_900,
    daily_amount_before=0,
    session_is_new_device=True,
    session_is_unusual=True,
    session_ip_risk="medium",
    session_geo_risk="medium",
    security_event_type="alerts_disabled",
    signals=(
        SignalSeed(
            signal_key="recent_limit_increase",
            signal_group="limit_configuration",
            severity="high",
            risk_points=5,
            weight=0.55,
            observed_value="5000_to_20000",
            baseline_value="5000",
            explanation="The transfer limit was increased immediately before the transfer.",
        ),
        SignalSeed(
            signal_key="new_beneficiary",
            signal_group="beneficiary",
            severity="high",
            risk_points=4,
            weight=0.45,
            observed_value="created_now",
            baseline_value="known_beneficiaries",
            explanation="The beneficiary was created during the same sensitive flow.",
        ),
        SignalSeed(
            signal_key="amount_near_mtu",
            signal_group="limit_evasion",
            severity="high",
            risk_points=5,
            weight=0.5,
            observed_value="19900_of_20000",
            baseline_value="limit=20000",
            explanation="The amount is just below the configured transfer limit.",
        ),
        SignalSeed(
            signal_key="amount_above_baseline",
            signal_group="transfer_amount",
            severity="high",
            risk_points=4,
            weight=0.4,
            observed_value="19900",
            baseline_value="max_usual=5000",
            explanation="The amount is far above the payer's usual maximum.",
        ),
        SignalSeed(
            signal_key="low_residual_balance",
            signal_group="financial_context",
            severity="medium",
            risk_points=3,
            weight=0.25,
            observed_value="2100",
            baseline_value="minimum_residual=4000",
            explanation="The transfer would leave the account below its usual residual balance.",
        ),
        SignalSeed(
            signal_key="new_device",
            signal_group="session_device",
            severity="low",
            risk_points=1,
            weight=0.1,
            observed_value="true",
            baseline_value="false",
            explanation="The session used a new device, which is secondary context only.",
            is_primary_signal=False,
        ),
    ),
)


def main() -> None:
    """Seed the high-risk case."""
    init_db()
    with SessionLocal() as db:
        evaluation = seed_demo_case(db, CASE)
        print_seed_summary("high-risk", evaluation)


if __name__ == "__main__":
    main()
