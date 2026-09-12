"""Seed all synthetic demo cases for local validation."""

from demo_cases.seed_helpers import print_seed_summary, seed_demo_case
from seed_high_risk_case import CASE as HIGH_RISK_CASE
from seed_low_risk_case import CASE as LOW_RISK_CASE
from seed_medium_risk_case import CASE as MEDIUM_RISK_CASE

from app.database import SessionLocal, init_db


def main() -> None:
    """Seed low, medium, and high-risk demo cases."""
    init_db()
    with SessionLocal() as db:
        for label, case in (
            ("low-risk", LOW_RISK_CASE),
            ("medium-risk", MEDIUM_RISK_CASE),
            ("high-risk", HIGH_RISK_CASE),
        ):
            evaluation = seed_demo_case(db, case)
            print_seed_summary(label, evaluation)


if __name__ == "__main__":
    main()
