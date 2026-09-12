"""Print seeded demo risk evaluations."""

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import SessionLocal
from app.models import Account, RiskEvaluation, SignalResult, Transfer, User


def main() -> None:
    """Print seeded users, decisions, and signal points."""
    with SessionLocal() as db:
        stmt = (
            select(RiskEvaluation)
            .options(joinedload(RiskEvaluation.signals))
            .join(Transfer, RiskEvaluation.transfer_id == Transfer.id)
            .join(Account, Transfer.account_id == Account.id)
            .join(User, Account.user_id == User.id)
            .order_by(RiskEvaluation.id)
        )
        evaluations = db.execute(stmt).unique().scalars().all()

        if not evaluations:
            print("No seeded demo evaluations found.")
            return

        for evaluation in evaluations:
            signal_points = sum(signal.risk_points for signal in evaluation.signals)
            signal_keys = ", ".join(signal.signal_key for signal in evaluation.signals)
            print(
                f"evaluation={evaluation.id} decision={evaluation.decision} "
                f"risk={evaluation.risk_level} points={signal_points} "
                f"signals=[{signal_keys}]"
            )


if __name__ == "__main__":
    main()
