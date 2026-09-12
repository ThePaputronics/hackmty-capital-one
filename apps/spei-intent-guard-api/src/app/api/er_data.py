"""Endpoints for loading and inspecting ER-model data."""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.models import (
    Account,
    Beneficiary,
    BeneficiaryChange,
    Event,
    LimitChange,
    SecurityEvent,
    Transfer,
    User,
)
from app.models import (
    Session as UserSession,
)

router = APIRouter(prefix="/api/v1", tags=["er-data"])
DbSession = Annotated[Session, Depends(get_db)]


@router.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(payload: schemas.UserCreate, db: DbSession):
    """Create a synthetic payer profile."""
    return crud.create_user(db, payload)


@router.get("/users", response_model=list[schemas.UserResponse])
def list_users(db: DbSession, skip: int = 0, limit: int = 100):
    """List synthetic payer profiles."""
    return crud.list_records(db, User, skip=skip, limit=limit)


@router.post("/accounts", response_model=schemas.AccountResponse, status_code=201)
def create_account(payload: schemas.AccountCreate, db: DbSession):
    """Create a payer-owned source account."""
    return crud.create_account(db, payload)


@router.get("/accounts", response_model=list[schemas.AccountResponse])
def list_accounts(db: DbSession, skip: int = 0, limit: int = 100):
    """List source accounts."""
    return crud.list_records(db, Account, skip=skip, limit=limit)


@router.post("/sessions", response_model=schemas.SessionResponse, status_code=201)
def create_session(payload: schemas.SessionCreate, db: DbSession):
    """Create a user session."""
    return crud.create_session(db, payload)


@router.get("/sessions", response_model=list[schemas.SessionResponse])
def list_sessions(db: DbSession, skip: int = 0, limit: int = 100):
    """List user sessions."""
    return crud.list_records(db, UserSession, skip=skip, limit=limit)


@router.post("/security-events", response_model=schemas.SecurityEventResponse, status_code=201)
def create_security_event(payload: schemas.SecurityEventCreate, db: DbSession):
    """Create a user-side security or configuration event."""
    return crud.create_security_event(db, payload)


@router.get("/security-events", response_model=list[schemas.SecurityEventResponse])
def list_security_events(db: DbSession, skip: int = 0, limit: int = 100):
    """List security or configuration events."""
    return crud.list_records(db, SecurityEvent, skip=skip, limit=limit)


@router.post("/beneficiaries", response_model=schemas.BeneficiaryResponse, status_code=201)
def create_beneficiary(payload: schemas.BeneficiaryCreate, db: DbSession):
    """Create a payer-scoped beneficiary."""
    return crud.create_beneficiary(db, payload)


@router.get("/beneficiaries", response_model=list[schemas.BeneficiaryResponse])
def list_beneficiaries(db: DbSession, skip: int = 0, limit: int = 100):
    """List payer-scoped beneficiaries."""
    return crud.list_records(db, Beneficiary, skip=skip, limit=limit)


@router.post(
    "/beneficiary-changes",
    response_model=schemas.BeneficiaryChangeResponse,
    status_code=201,
)
def create_beneficiary_change(payload: schemas.BeneficiaryChangeCreate, db: DbSession):
    """Create a beneficiary lifecycle event."""
    return crud.create_beneficiary_change(db, payload)


@router.get("/beneficiary-changes", response_model=list[schemas.BeneficiaryChangeResponse])
def list_beneficiary_changes(db: DbSession, skip: int = 0, limit: int = 100):
    """List beneficiary lifecycle events."""
    return crud.list_records(db, BeneficiaryChange, skip=skip, limit=limit)


@router.post("/limit-changes", response_model=schemas.LimitChangeResponse, status_code=201)
def create_limit_change(payload: schemas.LimitChangeCreate, db: DbSession):
    """Create an MTU or transfer-limit change event."""
    return crud.create_limit_change(db, payload)


@router.get("/limit-changes", response_model=list[schemas.LimitChangeResponse])
def list_limit_changes(db: DbSession, skip: int = 0, limit: int = 100):
    """List MTU or transfer-limit changes."""
    return crud.list_records(db, LimitChange, skip=skip, limit=limit)


@router.post("/transfers", response_model=schemas.TransferResponse, status_code=201)
def create_transfer(payload: schemas.TransferCreate, db: DbSession):
    """Create a proposed or submitted SPEI transfer."""
    return crud.create_transfer(db, payload)


@router.get("/transfers", response_model=list[schemas.TransferResponse])
def list_transfers(db: DbSession, skip: int = 0, limit: int = 100):
    """List SPEI transfers."""
    return crud.list_records(db, Transfer, skip=skip, limit=limit)


@router.post("/events", response_model=schemas.EventResponse, status_code=201)
def create_event(payload: schemas.EventCreate, db: DbSession):
    """Create a normalized event stream row."""
    return crud.create_event(db, payload)


@router.get("/events", response_model=list[schemas.EventResponse])
def list_events(db: DbSession, skip: int = 0, limit: int = 100):
    """List normalized event stream rows."""
    return crud.list_records(db, Event, skip=skip, limit=limit)
