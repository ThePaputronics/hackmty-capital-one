"""Helpers for seeding synthetic SPEI Intent Guard demo cases."""

from collections.abc import Iterable
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import (
    Account,
    Beneficiary,
    BeneficiaryChange,
    DecisionAudit,
    Event,
    LimitChange,
    RiskEvaluation,
    SecurityEvent,
    Session as UserSession,
    SignalResult,
    Transfer,
    User,
    UserBaseline,
)


@dataclass(frozen=True)
class SignalSeed:
    """Synthetic anomaly signal used to build a demo risk evaluation."""

    signal_key: str
    signal_group: str
    severity: str
    risk_points: int
    weight: float
    observed_value: str
    baseline_value: str
    explanation: str
    is_primary_signal: bool = True


@dataclass(frozen=True)
class DemoCase:
    """Synthetic end-to-end case for one payer transfer moment."""

    case_id: str
    display_name: str
    balance: float
    transfer_limit: float
    baseline_avg_amount: float
    baseline_max_usual_amount: float
    baseline_daily_amount: float
    baseline_daily_count: float
    minimum_residual_balance: float
    beneficiary_alias: str
    beneficiary_change_type: str
    previous_limit: float
    new_limit: float
    transfer_amount: float
    daily_amount_before: float
    session_is_new_device: bool
    session_is_unusual: bool
    session_ip_risk: str
    session_geo_risk: str
    security_event_type: str | None
    signals: tuple[SignalSeed, ...]


def seed_demo_case(db: Session, case: DemoCase) -> RiskEvaluation:
    """Seed one synthetic demo case and return its risk evaluation."""
    existing_user = db.execute(
        select(User).where(User.external_user_id == case.case_id)
    ).scalar_one_or_none()
    if existing_user is not None:
        return _latest_evaluation_for_user(db, existing_user)

    user = User(external_user_id=case.case_id, display_name=case.display_name)
    db.add(user)
    db.flush()

    account = Account(
        user_id=user.id,
        external_account_id=f"{case.case_id}-account",
        institution_code="demo-bank",
        available_balance=case.balance,
        daily_transfer_limit=case.transfer_limit,
    )
    db.add(account)
    db.flush()

    session = UserSession(
        user_id=user.id,
        channel="mobile",
        device_fingerprint_token=f"tok_device_{case.case_id}",
        ip_risk_level=case.session_ip_risk,
        geo_risk_level=case.session_geo_risk,
        is_new_device=case.session_is_new_device,
        is_unusual_session=case.session_is_unusual,
    )
    db.add(session)
    db.flush()

    beneficiary = Beneficiary(
        user_id=user.id,
        alias=case.beneficiary_alias,
        clabe_token=f"tok_clabe_{case.case_id}",
        institution_code="destination-bank",
    )
    db.add(beneficiary)
    db.flush()

    db.add(
        BeneficiaryChange(
            beneficiary_id=beneficiary.id,
            session_id=session.id,
            change_type=case.beneficiary_change_type,
            changed_fields={"source": "demo_seed"},
        )
    )

    if case.security_event_type:
        db.add(
            SecurityEvent(
                user_id=user.id,
                session_id=session.id,
                event_type=case.security_event_type,
                metadata_json={"source": "demo_seed"},
            )
        )

    db.add(
        LimitChange(
            account_id=account.id,
            session_id=session.id,
            previous_limit=case.previous_limit,
            new_limit=case.new_limit,
            change_ratio=case.new_limit / case.previous_limit
            if case.previous_limit > 0
            else 1.0,
        )
    )

    transfer = Transfer(
        account_id=account.id,
        beneficiary_id=beneficiary.id,
        session_id=session.id,
        amount=case.transfer_amount,
        status="evaluated",
        available_balance_before=case.balance,
        available_balance_after=case.balance - case.transfer_amount,
        daily_amount_before=case.daily_amount_before,
        daily_amount_after=case.daily_amount_before + case.transfer_amount,
    )
    db.add(transfer)
    db.flush()

    baseline = UserBaseline(
        user_id=user.id,
        account_id=account.id,
        avg_transfer_amount=case.baseline_avg_amount,
        max_usual_transfer_amount=case.baseline_max_usual_amount,
        avg_daily_transfer_amount=case.baseline_daily_amount,
        avg_daily_transfer_count=case.baseline_daily_count,
        minimum_residual_balance=case.minimum_residual_balance,
        usual_active_hours=[9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        usual_channels=["mobile"],
    )
    db.add(baseline)
    db.flush()

    total_points = sum(signal.risk_points for signal in case.signals)
    primary_count = sum(1 for signal in case.signals if signal.is_primary_signal)
    decision, risk_level = classify_seed_case(total_points, primary_count)

    evaluation = RiskEvaluation(
        transfer_id=transfer.id,
        baseline_id=baseline.id,
        anomaly_score=min(total_points / 25, 1.0),
        manipulation_risk_score=min((total_points + primary_count) / 30, 1.0),
        decision=decision,
        risk_level=risk_level,
        reason_summary=summarize_signals(case.signals),
        latency_ms=0,
    )
    db.add(evaluation)
    db.flush()

    db.add_all(
        SignalResult(
            risk_evaluation_id=evaluation.id,
            signal_key=signal.signal_key,
            signal_group=signal.signal_group,
            severity=signal.severity,
            risk_points=signal.risk_points,
            weight=signal.weight,
            observed_value=signal.observed_value,
            baseline_value=signal.baseline_value,
            is_primary_signal=signal.is_primary_signal,
            explanation=signal.explanation,
        )
        for signal in case.signals
    )

    db.add(
        DecisionAudit(
            risk_evaluation_id=evaluation.id,
            action={"allow": "none", "warn": "soft_warning", "pause": "reversible_pause"}[
                decision
            ],
            customer_message=build_customer_message(decision, case.signals),
            reason_codes=[signal.signal_key for signal in case.signals],
        )
    )

    db.add_all(build_events(user, account, session, beneficiary, transfer, case))
    db.commit()
    db.refresh(evaluation)
    return evaluation


def classify_seed_case(total_points: int, primary_count: int) -> tuple[str, str]:
    """Classify a seeded case with the MVP practical rule."""
    if primary_count >= 3 and total_points >= 12:
        return "pause", "high"
    if primary_count >= 2 and total_points >= 7:
        return "warn", "medium"
    return "allow", "low"


def summarize_signals(signals: Iterable[SignalSeed]) -> str:
    """Create a compact evaluation summary."""
    signal_names = [signal.signal_key.replace("_", " ") for signal in signals]
    return "Signals observed: " + ", ".join(signal_names)


def build_customer_message(decision: str, signals: tuple[SignalSeed, ...]) -> str:
    """Create a simple customer-facing explanation for the seeded case."""
    if decision == "pause":
        return (
            "This transfer combines several unusual signals for your recent behavior. "
            "Please review the beneficiary, amount, and limit change before continuing."
        )
    if decision == "warn":
        return (
            "This transfer has unusual context for your account. Review the details before "
            "confirming."
        )
    return "No unusual combination was detected for this transfer."


def build_events(
    user: User,
    account: Account,
    session: UserSession,
    beneficiary: Beneficiary,
    transfer: Transfer,
    case: DemoCase,
) -> list[Event]:
    """Build the event stream for a seeded transfer moment."""
    base = {
        "user_id": user.id,
        "account_id": account.id,
        "session_id": session.id,
    }
    return [
        Event(
            **base,
            event_type="session_started",
            entity_type="session",
            entity_id=session.id,
            payload={"case_id": case.case_id},
        ),
        Event(
            **base,
            event_type="beneficiary_created",
            entity_type="beneficiary",
            entity_id=beneficiary.id,
            payload={"alias": beneficiary.alias},
        ),
        Event(
            **base,
            event_type="limit_changed",
            entity_type="limit_change",
            entity_id=account.id,
            payload={"previous_limit": case.previous_limit, "new_limit": case.new_limit},
        ),
        Event(
            **base,
            event_type="transfer_evaluated",
            entity_type="transfer",
            entity_id=transfer.id,
            payload={"amount": case.transfer_amount},
        ),
    ]


def _latest_evaluation_for_user(db: Session, user: User) -> RiskEvaluation:
    """Return the latest seeded evaluation for an already seeded case."""
    stmt = (
        select(RiskEvaluation)
        .join(Transfer, RiskEvaluation.transfer_id == Transfer.id)
        .join(Account, Transfer.account_id == Account.id)
        .where(Account.user_id == user.id)
        .order_by(RiskEvaluation.id.desc())
    )
    evaluation = db.execute(stmt).scalars().first()
    if evaluation is None:
        raise RuntimeError(f"Seed case {user.external_user_id} exists without evaluation")
    return evaluation


def print_seed_summary(label: str, evaluation: RiskEvaluation) -> None:
    """Print a one-line seed result for terminal use."""
    print(
        f"{label}: evaluation={evaluation.id} decision={evaluation.decision} "
        f"risk={evaluation.risk_level} anomaly={evaluation.anomaly_score:.2f} "
        f"manipulation={evaluation.manipulation_risk_score:.2f}"
    )
