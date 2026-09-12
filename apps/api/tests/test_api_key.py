"""Tests for institution API key enforcement on write endpoints."""

from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from sentinel import main

API_KEY = "test-institution-key"

EVENT = {
    "payer_external_id": "payer_ana_01",
    "institution_code": "012",
    "type": "beneficiary_added",
    "occurred_at": datetime(2026, 9, 12, 12, 0, 0).isoformat(),
    "payload": {
        "destination_clabe": "012180001234567890",
        "destination_institution_code": "012",
        "alias": "Mama",
    },
}


@pytest.fixture
def enforced(monkeypatch: pytest.MonkeyPatch) -> None:
    """Enable API key enforcement with a known key."""
    monkeypatch.setattr(main.settings, "api_key_required", True)
    monkeypatch.setattr(main.settings, "institution_api_key", API_KEY)


@pytest.mark.parametrize(
    ("path", "body"),
    [
        ("/v1/events", EVENT),
        ("/v1/evaluate", {}),
        ("/v1/decisions/1/outcome", {"outcome": "cancelled"}),
    ],
)
@pytest.mark.parametrize(
    "headers",
    # Raw UTF-8 bytes reach the server as a non-ASCII string; the check must reject it, not crash.
    [{}, {"X-API-Key": "wrong-key"}, {"X-API-Key": "llave-inválida".encode()}],
)
def test_writes_reject_missing_or_wrong_key(client: TestClient, enforced: None, path: str, body: dict, headers: dict):
    """Every write endpoint returns 401 without the correct key."""
    response = client.post(path, json=body, headers=headers)
    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"] == "APIKey"


def test_write_accepts_correct_key(client: TestClient, enforced: None):
    """A write with the institution key is processed normally."""
    response = client.post("/v1/events", json=EVENT, headers={"X-API-Key": API_KEY})
    assert response.status_code == 201
    assert response.json()["accepted"] == 1


def test_reads_stay_public_when_enforced(client: TestClient, enforced: None):
    """The dashboard feed and health check need no key."""
    assert client.get("/health").status_code == 200
    assert client.get("/v1/evaluations").status_code == 200
    assert client.get("/v1/evaluations/1").status_code == 404


def test_writes_open_when_enforcement_disabled(client: TestClient, monkeypatch: pytest.MonkeyPatch):
    """With enforcement off (the local default) writes need no key."""
    monkeypatch.setattr(main.settings, "api_key_required", False)
    assert client.post("/v1/events", json=EVENT).status_code == 201
