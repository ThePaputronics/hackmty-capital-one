"""Database helpers for the SPEI Intent Guard MVP."""

from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from app import schemas
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

ModelT = TypeVar("ModelT")


def list_records(db: Session, model: type[ModelT], skip: int = 0, limit: int = 100) -> list[ModelT]:
    """List model records with simple pagination."""
    stmt = select(model).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars().all())


def create_user(db: Session, payload: schemas.UserCreate) -> User:
    """Create a synthetic payer profile."""
    user = User(**payload.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_external_id(db: Session, external_user_id: str) -> User | None:
    """Get a payer profile by external demo ID."""
    stmt = select(User).where(User.external_user_id == external_user_id)
    return db.execute(stmt).scalar_one_or_none()


def create_account(db: Session, payload: schemas.AccountCreate) -> Account:
    """Create a payer-owned source account."""
    account = Account(**payload.model_dump())
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def create_session(db: Session, payload: schemas.SessionCreate) -> UserSession:
    """Create a user session."""
    session = UserSession(**payload.model_dump())
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def create_security_event(db: Session, payload: schemas.SecurityEventCreate) -> SecurityEvent:
    """Create a security or configuration event."""
    event = SecurityEvent(**payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def create_beneficiary(db: Session, payload: schemas.BeneficiaryCreate) -> Beneficiary:
    """Create a payer-scoped beneficiary."""
    beneficiary = Beneficiary(**payload.model_dump())
    db.add(beneficiary)
    db.commit()
    db.refresh(beneficiary)
    return beneficiary


def create_beneficiary_change(
    db: Session, payload: schemas.BeneficiaryChangeCreate
) -> BeneficiaryChange:
    """Create a beneficiary lifecycle event."""
    change = BeneficiaryChange(**payload.model_dump())
    db.add(change)
    db.commit()
    db.refresh(change)
    return change


def create_limit_change(db: Session, payload: schemas.LimitChangeCreate) -> LimitChange:
    """Create an MTU or transfer-limit change event."""
    payload_data = payload.model_dump()
    previous_limit = payload.previous_limit
    new_limit = payload.new_limit
    payload_data["change_ratio"] = new_limit / previous_limit if previous_limit > 0 else 1.0
    limit_change = LimitChange(**payload_data)
    db.add(limit_change)
    db.commit()
    db.refresh(limit_change)
    return limit_change


def create_transfer(db: Session, payload: schemas.TransferCreate) -> Transfer:
    """Create a proposed or submitted SPEI transfer."""
    payload_data = payload.model_dump()
    amount = payload.amount
    payload_data["available_balance_after"] = payload.available_balance_before - amount
    payload_data["daily_amount_after"] = payload.daily_amount_before + amount
    transfer = Transfer(**payload_data)
    db.add(transfer)
    db.commit()
    db.refresh(transfer)
    return transfer


def create_event(db: Session, payload: schemas.EventCreate) -> Event:
    """Create a normalized event stream row."""
    event = Event(**payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
