"""Pydantic schemas for SPEI Intent Guard API requests and responses."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    """Create a synthetic payer profile."""

    external_user_id: str
    display_name: str | None = None


class UserResponse(UserCreate):
    """Payer profile response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    risk_profile_version: str
    created_at: datetime


class AccountCreate(BaseModel):
    """Create a payer-owned source account."""

    user_id: int
    external_account_id: str
    institution_code: str
    account_type: str = "checking"
    available_balance: float = Field(ge=0)
    daily_transfer_limit: float = Field(gt=0)


class AccountResponse(AccountCreate):
    """Source account response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class SessionCreate(BaseModel):
    """Create a user session."""

    user_id: int
    channel: str = "mobile"
    device_fingerprint_token: str | None = None
    ip_risk_level: str = "low"
    geo_risk_level: str = "low"
    is_new_device: bool = False
    is_unusual_session: bool = False


class SessionResponse(SessionCreate):
    """User session response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    started_at: datetime
    ended_at: datetime | None = None


class BeneficiaryCreate(BaseModel):
    """Create a payer-scoped beneficiary."""

    user_id: int
    alias: str
    clabe_token: str
    institution_code: str
    is_active: bool = True


class BeneficiaryResponse(BeneficiaryCreate):
    """Payer-scoped beneficiary response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    last_used_at: datetime | None = None


class BeneficiaryChangeCreate(BaseModel):
    """Create a beneficiary lifecycle event."""

    beneficiary_id: int
    session_id: int | None = None
    change_type: str
    changed_fields: dict[str, Any] | None = None


class BeneficiaryChangeResponse(BeneficiaryChangeCreate):
    """Beneficiary lifecycle event response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class SecurityEventCreate(BaseModel):
    """Create a user-side security or configuration event."""

    user_id: int
    session_id: int | None = None
    event_type: str
    metadata_json: dict[str, Any] | None = None


class SecurityEventResponse(SecurityEventCreate):
    """Security event response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class LimitChangeCreate(BaseModel):
    """Create an MTU or transfer-limit change event."""

    account_id: int
    session_id: int | None = None
    previous_limit: float = Field(ge=0)
    new_limit: float = Field(gt=0)


class LimitChangeResponse(LimitChangeCreate):
    """Limit change response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    change_ratio: float
    created_at: datetime


class TransferCreate(BaseModel):
    """Create a proposed or submitted SPEI transfer."""

    account_id: int
    beneficiary_id: int
    session_id: int | None = None
    amount: float = Field(gt=0)
    currency: str = "MXN"
    status: str = "draft"
    description: str | None = None
    available_balance_before: float = Field(ge=0)
    daily_amount_before: float = Field(ge=0, default=0)


class TransferResponse(TransferCreate):
    """SPEI transfer response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    available_balance_after: float
    daily_amount_after: float
    created_at: datetime
    submitted_at: datetime | None = None


class EventCreate(BaseModel):
    """Create a normalized event stream row."""

    user_id: int
    account_id: int | None = None
    session_id: int | None = None
    event_type: str
    entity_type: str | None = None
    entity_id: int | None = None
    payload: dict[str, Any] | None = None


class EventResponse(EventCreate):
    """Normalized event response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    occurred_at: datetime
