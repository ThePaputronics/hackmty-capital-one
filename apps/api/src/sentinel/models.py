"""SQLAlchemy models for Sentinel."""

from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import (
    JSON,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sentinel.database import Base


class Payer(Base):
    """Payer profile originating transactions."""

    __tablename__ = "payers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    external_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    institution_code: Mapped[str] = mapped_column(String(40), index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow
    )

    events: Mapped[list["Event"]] = relationship(back_populates="payer", cascade="all, delete-orphan")
    evaluations: Mapped[list["Evaluation"]] = relationship(back_populates="payer")


class Event(Base):
    """Append-only transaction ledger and security event stream."""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    payer_id: Mapped[int] = mapped_column(ForeignKey("payers.id"), index=True)
    type: Mapped[str] = mapped_column(String(80), index=True)
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)

    payer: Mapped[Payer] = relationship(back_populates="events")

    __table_args__ = (
        Index("idx_events_payer_occurred", "payer_id", "occurred_at"),
        Index("idx_events_type_occurred", "type", "occurred_at"),
    )


class Evaluation(Base):
    """Real-time transfer risk evaluation record."""

    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    payer_id: Mapped[int] = mapped_column(ForeignKey("payers.id"), index=True)
    destination_clabe: Mapped[str] = mapped_column(String(30), index=True)
    destination_institution_code: Mapped[str] = mapped_column(String(40))
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    currency: Mapped[str] = mapped_column(String(3), default="MXN")
    proposed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)

    # Decisions: allow, challenge, pause
    decision: Mapped[str] = mapped_column(String(20), index=True)

    # Individual component scores normalized 0.0000 - 1.0000
    score_ato: Mapped[Decimal] = mapped_column(Numeric(5, 4), default=Decimal("0.0"))
    score_intent: Mapped[Decimal] = mapped_column(Numeric(5, 4), default=Decimal("0.0"))
    score_recipient: Mapped[Decimal] = mapped_column(Numeric(5, 4), default=Decimal("0.0"))

    # Explanation and audit
    reason_codes: Mapped[list[str]] = mapped_column(JSON, default=list)
    payer_message_es: Mapped[str] = mapped_column(Text, default="")
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)
    ruleset_version: Mapped[str] = mapped_column(String(50))
    evaluated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow
    )

    payer: Mapped[Payer] = relationship(back_populates="evaluations")
    signals: Mapped[list["EvaluationSignal"]] = relationship(
        back_populates="evaluation", cascade="all, delete-orphan"
    )
    outcome: Mapped["Outcome | None"] = relationship(
        back_populates="evaluation", uselist=False, cascade="all, delete-orphan"
    )


class EvaluationSignal(Base):
    """Individual explainable factor contributing to an evaluation decision."""

    __tablename__ = "evaluation_signals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    evaluation_id: Mapped[int] = mapped_column(ForeignKey("evaluations.id"), index=True)
    key: Mapped[str] = mapped_column(String(100))
    signal_group: Mapped[str] = mapped_column(String(40))  # ato, intent, recipient
    points: Mapped[int] = mapped_column(Integer, default=1)  # 1 - 5 severity points
    observed: Mapped[str] = mapped_column(String(255))
    baseline: Mapped[str] = mapped_column(String(255))
    explanation: Mapped[str] = mapped_column(Text)

    evaluation: Mapped[Evaluation] = relationship(back_populates="signals")


class Outcome(Base):
    """Actual disposition reported back by the participating bank."""

    __tablename__ = "outcomes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    evaluation_id: Mapped[int] = mapped_column(ForeignKey("evaluations.id"), unique=True, index=True)
    # Outcome status: cancelled, continued, verified_callback
    outcome: Mapped[str] = mapped_column(String(40))
    reported_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow
    )

    evaluation: Mapped[Evaluation] = relationship(back_populates="outcome")
