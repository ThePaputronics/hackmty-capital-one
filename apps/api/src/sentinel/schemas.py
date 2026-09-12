"""Pydantic schemas for the Sentinel API contract."""

from datetime import datetime
from decimal import Decimal
from typing import Any, Literal
from pydantic import BaseModel, Field


# --- Event Ingest Schemas ---

class EventCreate(BaseModel):
    """Single ledger event payload."""

    payer_external_id: str = Field(..., description="External unique ID for the payer")
    institution_code: str = Field(..., description="Originating institution code")
    type: str = Field(
        ...,
        description="Event type: transfer_settled, beneficiary_added, limit_changed, session_started, device_seen, credential_changed",
    )
    occurred_at: datetime = Field(..., description="Simulated timestamp when event occurred")
    payload: dict[str, Any] = Field(default_factory=dict, description="Event-specific metadata")


class EventBatchCreate(BaseModel):
    """Batch ingestion of ledger events."""

    events: list[EventCreate] = Field(..., min_length=1, max_length=1000)


class EventIngestResponse(BaseModel):
    """Response returned upon event ingestion."""

    accepted: int
    status: Literal["ok"] = "ok"


# --- Evaluation Schemas ---

class SessionContext(BaseModel):
    """Session telemetry provided by the originating banking app."""

    device_id: str
    is_new_device: bool = False
    ip_risk: Literal["low", "medium", "high"] = "low"
    geo_risk: Literal["low", "medium", "high"] = "low"


class DeviceContext(BaseModel):
    """Device-level vulnerability indicators reported by bank mobile SDK."""

    active_call: bool = False
    screen_share: bool = False
    remote_access: bool = False


class EvaluateRequest(BaseModel):
    """Request payload for pre-submission transfer evaluation."""

    payer_external_id: str
    institution_code: str
    amount: Decimal = Field(..., gt=0, decimal_places=2)
    currency: str = "MXN"
    destination_clabe: str = Field(..., min_length=18, max_length=18)
    destination_institution_code: str
    proposed_at: datetime = Field(..., description="Simulated submission time")
    session: SessionContext
    context: DeviceContext = Field(default_factory=DeviceContext)


class SignalItem(BaseModel):
    """Individual explainable factor."""

    key: str
    signal_group: Literal["ato", "intent", "recipient"]
    points: int = Field(..., ge=1, le=5)
    observed: str
    baseline: str
    explanation: str


class ScoresBreakdown(BaseModel):
    """Normalized 0.0 - 1.0 individual dimension risk scores."""

    ato: float
    intent: float
    recipient: float


class EvaluateResponse(BaseModel):
    """Evaluation verdict with explainability and customer guidance."""

    evaluation_id: int
    payer_external_id: str
    decision: Literal["allow", "challenge", "pause"]
    scores: ScoresBreakdown
    signals: list[SignalItem]
    reason_codes: list[str]
    payer_message_es: str
    latency_ms: int
    ruleset_version: str
    evaluated_at: datetime


# --- Outcome Schemas ---

class OutcomeCreate(BaseModel):
    """Reported disposition after customer interaction."""

    outcome: Literal["cancelled", "continued", "verified_callback"]


class OutcomeResponse(BaseModel):
    """Confirmation of recorded outcome."""

    evaluation_id: int
    outcome: str
    recorded: bool
    reported_at: datetime


# --- Feed and Detail Schemas ---

class EvaluationSummary(BaseModel):
    """Lightweight evaluation record for live UI streaming."""

    id: int
    payer_external_id: str
    destination_clabe: str
    destination_institution_code: str
    amount: Decimal
    currency: str
    decision: str
    score_ato: float
    score_intent: float
    score_recipient: float
    reason_codes: list[str]
    proposed_at: datetime
    evaluated_at: datetime
    outcome: str | None = None


class EvaluationFeedResponse(BaseModel):
    """Cursor-paginated feed of evaluation events."""

    items: list[EvaluationSummary]
    next_cursor: int | None = None


class EvaluationDetailResponse(EvaluateResponse):
    """Full evaluation record with reported outcome for drill-down."""

    amount: Decimal
    currency: str
    destination_clabe: str
    destination_institution_code: str
    proposed_at: datetime
    outcome: OutcomeResponse | None = None
