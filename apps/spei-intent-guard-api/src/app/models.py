"""Database models for the SPEI Intent Guard MVP."""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


class User(Base):
    """Synthetic payer profile evaluated by the MVP."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    external_user_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    display_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    risk_profile_version: Mapped[str] = mapped_column(String(50), default="mvp-v1")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    accounts: Mapped[list["Account"]] = relationship(back_populates="user")
    beneficiaries: Mapped[list["Beneficiary"]] = relationship(back_populates="user")
    sessions: Mapped[list["Session"]] = relationship(back_populates="user")


class Account(Base):
    """Payer-owned source account."""

    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    external_account_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    institution_code: Mapped[str] = mapped_column(String(40))
    account_type: Mapped[str] = mapped_column(String(40), default="checking")
    available_balance: Mapped[float] = mapped_column(Float)
    daily_transfer_limit: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    user: Mapped[User] = relationship(back_populates="accounts")
    transfers: Mapped[list["Transfer"]] = relationship(back_populates="account")


class Beneficiary(Base):
    """Payer-scoped saved destination, not a global receiver reputation record."""

    __tablename__ = "beneficiaries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    alias: Mapped[str] = mapped_column(String(255))
    clabe_token: Mapped[str] = mapped_column(String(255), index=True)
    institution_code: Mapped[str] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    last_used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped[User] = relationship(back_populates="beneficiaries")
    changes: Mapped[list["BeneficiaryChange"]] = relationship(back_populates="beneficiary")
    transfers: Mapped[list["Transfer"]] = relationship(back_populates="beneficiary")


class BeneficiaryChange(Base):
    """Beneficiary lifecycle change used as transfer context."""

    __tablename__ = "beneficiary_changes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    beneficiary_id: Mapped[int] = mapped_column(ForeignKey("beneficiaries.id"), index=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("sessions.id"), nullable=True)
    change_type: Mapped[str] = mapped_column(String(60))
    changed_fields: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    beneficiary: Mapped[Beneficiary] = relationship(back_populates="changes")


class Session(Base):
    """User session context around sensitive actions."""

    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    channel: Mapped[str] = mapped_column(String(40), default="mobile")
    device_fingerprint_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ip_risk_level: Mapped[str] = mapped_column(String(20), default="low")
    geo_risk_level: Mapped[str] = mapped_column(String(20), default="low")
    is_new_device: Mapped[bool] = mapped_column(Boolean, default=False)
    is_unusual_session: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped[User] = relationship(back_populates="sessions")


class SecurityEvent(Base):
    """User-side security or configuration change."""

    __tablename__ = "security_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("sessions.id"), nullable=True)
    event_type: Mapped[str] = mapped_column(String(80))
    metadata_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class LimitChange(Base):
    """MTU or transfer-limit change."""

    __tablename__ = "limit_changes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("sessions.id"), nullable=True)
    previous_limit: Mapped[float] = mapped_column(Float)
    new_limit: Mapped[float] = mapped_column(Float)
    change_ratio: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Transfer(Base):
    """Proposed or submitted SPEI transfer."""

    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    beneficiary_id: Mapped[int] = mapped_column(ForeignKey("beneficiaries.id"), index=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("sessions.id"), nullable=True)
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(3), default="MXN")
    status: Mapped[str] = mapped_column(String(40), default="draft")
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    available_balance_before: Mapped[float] = mapped_column(Float)
    available_balance_after: Mapped[float] = mapped_column(Float)
    daily_amount_before: Mapped[float] = mapped_column(Float, default=0)
    daily_amount_after: Mapped[float] = mapped_column(Float, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    account: Mapped[Account] = relationship(back_populates="transfers")
    beneficiary: Mapped[Beneficiary] = relationship(back_populates="transfers")
    evaluations: Mapped[list["RiskEvaluation"]] = relationship(back_populates="transfer")


class UserBaseline(Base):
    """Payer-specific behavioral expectations."""

    __tablename__ = "user_baselines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    window_days: Mapped[int] = mapped_column(Integer, default=90)
    avg_transfer_amount: Mapped[float] = mapped_column(Float)
    max_usual_transfer_amount: Mapped[float] = mapped_column(Float)
    avg_daily_transfer_amount: Mapped[float] = mapped_column(Float)
    avg_daily_transfer_count: Mapped[float] = mapped_column(Float)
    minimum_residual_balance: Mapped[float] = mapped_column(Float)
    usual_active_hours: Mapped[list[int] | None] = mapped_column(JSON, nullable=True)
    usual_channels: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
    computed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class RiskEvaluation(Base):
    """Result of evaluating one transfer."""

    __tablename__ = "risk_evaluations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transfer_id: Mapped[int] = mapped_column(ForeignKey("transfers.id"), index=True)
    baseline_id: Mapped[int] = mapped_column(ForeignKey("user_baselines.id"), index=True)
    evaluated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    anomaly_score: Mapped[float] = mapped_column(Float)
    manipulation_risk_score: Mapped[float] = mapped_column(Float)
    decision: Mapped[str] = mapped_column(String(20))
    risk_level: Mapped[str] = mapped_column(String(20))
    reason_summary: Mapped[str] = mapped_column(Text)
    model_version: Mapped[str] = mapped_column(String(50), default="rules-mvp-v1")
    ruleset_version: Mapped[str] = mapped_column(String(50), default="rules-mvp-v1")
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)

    transfer: Mapped[Transfer] = relationship(back_populates="evaluations")
    signals: Mapped[list["SignalResult"]] = relationship(back_populates="risk_evaluation")
    decision_audit: Mapped["DecisionAudit | None"] = relationship(back_populates="risk_evaluation")


class SignalResult(Base):
    """Individual explainable signal emitted by the risk engine."""

    __tablename__ = "signal_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    risk_evaluation_id: Mapped[int] = mapped_column(ForeignKey("risk_evaluations.id"), index=True)
    signal_key: Mapped[str] = mapped_column(String(100))
    signal_group: Mapped[str] = mapped_column(String(80))
    severity: Mapped[str] = mapped_column(String(20))
    risk_points: Mapped[int] = mapped_column(Integer, default=1)
    weight: Mapped[float] = mapped_column(Float)
    observed_value: Mapped[str | None] = mapped_column(String(255), nullable=True)
    baseline_value: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_primary_signal: Mapped[bool] = mapped_column(Boolean, default=True)
    explanation: Mapped[str] = mapped_column(Text)

    risk_evaluation: Mapped[RiskEvaluation] = relationship(back_populates="signals")


class DecisionAudit(Base):
    """Customer-facing risk action and reason codes."""

    __tablename__ = "decision_audits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    risk_evaluation_id: Mapped[int] = mapped_column(ForeignKey("risk_evaluations.id"), unique=True)
    action: Mapped[str] = mapped_column(String(40))
    customer_message: Mapped[str] = mapped_column(Text)
    reason_codes: Mapped[list[str]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    risk_evaluation: Mapped[RiskEvaluation] = relationship(back_populates="decision_audit")


class Event(Base):
    """Normalized event stream row for demo replay and feature calculation."""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    account_id: Mapped[int | None] = mapped_column(ForeignKey("accounts.id"), nullable=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("sessions.id"), nullable=True)
    event_type: Mapped[str] = mapped_column(String(80), index=True)
    entity_type: Mapped[str | None] = mapped_column(String(80), nullable=True)
    entity_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
