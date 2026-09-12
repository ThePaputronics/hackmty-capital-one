"""Tests for SPEI Intent Guard database models."""

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import crud, schemas
from app.models import (
    Base,
    Event,
    LimitChange,
    SecurityEvent,
    Session as UserSession,
    Transfer,
)
from app.schemas import AccountCreate, BeneficiaryCreate, UserCreate


@pytest.fixture
def db_session():
    """Create an in-memory test database session."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    testing_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = testing_session()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_domain_tables_are_created(db_session: Session):
    """The ER model should be reflected in concrete database tables."""
    table_names = set(inspect(db_session.bind).get_table_names())

    assert {
        "accounts",
        "beneficiaries",
        "beneficiary_changes",
        "decision_audits",
        "events",
        "limit_changes",
        "risk_evaluations",
        "security_events",
        "sessions",
        "signal_results",
        "transfers",
        "user_baselines",
        "users",
    }.issubset(table_names)


def test_create_core_payer_context(db_session: Session):
    """Create the minimum payer context that a future risk flow will need."""
    user = crud.create_user(
        db_session,
        UserCreate(external_user_id="demo-user-001", display_name="Demo Payer"),
    )
    account = crud.create_account(
        db_session,
        AccountCreate(
            user_id=user.id,
            external_account_id="demo-account-001",
            institution_code="demo-bank",
            available_balance=25_000,
            daily_transfer_limit=10_000,
        ),
    )
    beneficiary = crud.create_beneficiary(
        db_session,
        BeneficiaryCreate(
            user_id=user.id,
            alias="New supplier",
            clabe_token="tok_demo_clabe",
            institution_code="demo-destination-bank",
        ),
    )

    assert user.id is not None
    assert account.user_id == user.id
    assert beneficiary.user_id == user.id
    session = crud.create_session(
        db_session,
        schemas.SessionCreate(
            user_id=user.id,
            channel="mobile",
            device_fingerprint_token="tok_device",
            is_new_device=True,
        ),
    )
    security_event = crud.create_security_event(
        db_session,
        schemas.SecurityEventCreate(
            user_id=user.id,
            session_id=session.id,
            event_type="mfa_changed",
            metadata_json={"method": "sms"},
        ),
    )
    beneficiary_change = crud.create_beneficiary_change(
        db_session,
        schemas.BeneficiaryChangeCreate(
            beneficiary_id=beneficiary.id,
            session_id=session.id,
            change_type="created",
            changed_fields={"clabe_token": "created"},
        ),
    )
    limit_change = crud.create_limit_change(
        db_session,
        schemas.LimitChangeCreate(
            account_id=account.id,
            session_id=session.id,
            previous_limit=5_000,
            new_limit=10_000,
        ),
    )
    transfer = crud.create_transfer(
        db_session,
        schemas.TransferCreate(
            account_id=account.id,
            beneficiary_id=beneficiary.id,
            session_id=session.id,
            amount=9_900,
            available_balance_before=25_000,
        ),
    )
    event = crud.create_event(
        db_session,
        schemas.EventCreate(
            user_id=user.id,
            account_id=account.id,
            session_id=session.id,
            event_type="transfer_drafted",
            entity_type="transfer",
            entity_id=transfer.id,
        ),
    )

    assert crud.get_user_by_external_id(db_session, "demo-user-001").id == user.id
    assert session.id is not None
    assert security_event.id is not None
    assert beneficiary_change.id is not None
    assert limit_change.change_ratio == 2
    assert transfer.available_balance_after == 15_100
    assert event.id is not None
    assert len(crud.list_records(db_session, UserSession)) == 1
    assert len(crud.list_records(db_session, SecurityEvent)) == 1
    assert len(crud.list_records(db_session, LimitChange)) == 1
    assert len(crud.list_records(db_session, Transfer)) == 1
    assert len(crud.list_records(db_session, Event)) == 1


def test_signal_results_include_risk_points(db_session: Session):
    """Signal severity should have numeric points for future validation."""
    columns = {column["name"] for column in inspect(db_session.bind).get_columns("signal_results")}

    assert "risk_points" in columns
