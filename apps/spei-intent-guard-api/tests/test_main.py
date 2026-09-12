"""Tests for the FastAPI application shell."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import get_db
from app.main import app
from app.models import Base


@pytest.fixture
def client() -> TestClient:
    """Create a test client with an in-memory database."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    testing_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        db = testing_session()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        Base.metadata.drop_all(bind=engine)


def test_health(client: TestClient):
    """The API exposes a health endpoint."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "spei-intent-guard-api"}


def test_create_and_list_er_data(client: TestClient):
    """Create the ER-slice records needed for the first demo flow."""
    user_response = client.post(
        "/api/v1/users",
        json={"external_user_id": "demo-user-001", "display_name": "Demo Payer"},
    )
    assert user_response.status_code == 201
    user_id = user_response.json()["id"]

    account_response = client.post(
        "/api/v1/accounts",
        json={
            "user_id": user_id,
            "external_account_id": "demo-account-001",
            "institution_code": "demo-bank",
            "available_balance": 25_000,
            "daily_transfer_limit": 10_000,
        },
    )
    assert account_response.status_code == 201
    account_id = account_response.json()["id"]

    session_response = client.post(
        "/api/v1/sessions",
        json={
            "user_id": user_id,
            "channel": "mobile",
            "device_fingerprint_token": "tok_device_001",
            "is_new_device": True,
        },
    )
    assert session_response.status_code == 201
    session_id = session_response.json()["id"]

    beneficiary_response = client.post(
        "/api/v1/beneficiaries",
        json={
            "user_id": user_id,
            "alias": "New beneficiary",
            "clabe_token": "tok_clabe_001",
            "institution_code": "destination-bank",
        },
    )
    assert beneficiary_response.status_code == 201
    beneficiary_id = beneficiary_response.json()["id"]

    assert (
        client.post(
            "/api/v1/beneficiary-changes",
            json={
                "beneficiary_id": beneficiary_id,
                "session_id": session_id,
                "change_type": "created",
                "changed_fields": {"clabe_token": "created"},
            },
        ).status_code
        == 201
    )

    limit_response = client.post(
        "/api/v1/limit-changes",
        json={
            "account_id": account_id,
            "session_id": session_id,
            "previous_limit": 5_000,
            "new_limit": 10_000,
        },
    )
    assert limit_response.status_code == 201
    assert limit_response.json()["change_ratio"] == 2

    transfer_response = client.post(
        "/api/v1/transfers",
        json={
            "account_id": account_id,
            "beneficiary_id": beneficiary_id,
            "session_id": session_id,
            "amount": 9_900,
            "available_balance_before": 25_000,
            "daily_amount_before": 0,
        },
    )
    assert transfer_response.status_code == 201
    transfer_id = transfer_response.json()["id"]
    assert transfer_response.json()["available_balance_after"] == 15_100

    event_response = client.post(
        "/api/v1/events",
        json={
            "user_id": user_id,
            "account_id": account_id,
            "session_id": session_id,
            "event_type": "transfer_drafted",
            "entity_type": "transfer",
            "entity_id": transfer_id,
            "payload": {"amount": 9900},
        },
    )
    assert event_response.status_code == 201

    assert len(client.get("/api/v1/users").json()) == 1
    assert len(client.get("/api/v1/accounts").json()) == 1
    assert len(client.get("/api/v1/sessions").json()) == 1
    assert len(client.get("/api/v1/beneficiaries").json()) == 1
    assert len(client.get("/api/v1/beneficiary-changes").json()) == 1
    assert len(client.get("/api/v1/limit-changes").json()) == 1
    assert len(client.get("/api/v1/transfers").json()) == 1
    assert len(client.get("/api/v1/events").json()) == 1


def test_duplicate_external_user_id_returns_409(client: TestClient):
    """A repeated external_user_id is a client conflict, not a server fault."""
    payload = {"external_user_id": "demo-user-dup"}

    assert client.post("/api/v1/users", json=payload).status_code == 201

    conflict = client.post("/api/v1/users", json=payload)

    assert conflict.status_code == 409
    assert "conflicts" in conflict.json()["detail"]


def test_account_for_unknown_user_returns_409(client: TestClient):
    """A foreign key pointing nowhere must be rejected, not stored."""
    response = client.post(
        "/api/v1/accounts",
        json={
            "user_id": 999_999,
            "external_account_id": "orphan-account",
            "institution_code": "demo-bank",
            "available_balance": 10,
            "daily_transfer_limit": 10,
        },
    )

    assert response.status_code == 409
    assert client.get("/api/v1/accounts").json() == []
