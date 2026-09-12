"""Gemini pause copy generation and API persistence tests."""

import io
import json
from datetime import datetime
from urllib.error import URLError

from fastapi.testclient import TestClient

from sentinel.config import Settings
from sentinel.risk import gemini_message


def test_gemini_generates_short_message_without_customer_data(monkeypatch):
    """Send only risk reasons and accept a short Spanish response."""
    captured = {}

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        return io.BytesIO(json.dumps({"candidates": [{"content": {"parts": [{"text": "Pausamos tu transferencia. Llama a tu banco por el número oficial."}]}}]}).encode())

    monkeypatch.setattr(gemini_message, "urlopen", fake_urlopen)
    result = gemini_message.generate_pause_message(
        ["ACTIVE_CALL_MANIPULATION", "NEW_DESTINATION_RISK"],
        Settings(gemini_api_key="test-key"),
    )

    assert result == "Pausamos tu transferencia. Llama a tu banco por el número oficial."
    assert captured["request"].get_header("X-goog-api-key") == "test-key"
    assert captured["timeout"] == 3
    payload = json.loads(captured["request"].data)
    prompt = payload["contents"][0]["parts"][0]["text"]
    assert payload["generationConfig"]["thinkingConfig"] == {"thinkingLevel": "minimal"}
    assert "an active phone call" in prompt
    assert "a new destination account" in prompt
    assert "CLABE" not in prompt


def test_gemini_falls_back_when_response_is_too_long(monkeypatch):
    """Reject text that would overflow the protection-pause screen."""
    monkeypatch.setattr(
        gemini_message,
        "urlopen",
        lambda request, timeout: io.BytesIO(json.dumps({"candidates": [{"content": {"parts": [{"text": "x" * 221}]}}]}).encode()),
    )
    assert gemini_message.generate_pause_message([], Settings(gemini_api_key="test-key")) is None


def test_gemini_falls_back_when_request_fails(monkeypatch):
    """A Gemini outage must not prevent a protection pause."""
    def unavailable(request, timeout):
        raise URLError("unavailable")

    monkeypatch.setattr(gemini_message, "urlopen", unavailable)
    assert gemini_message.generate_pause_message([], Settings(gemini_api_key="test-key")) is None


def test_pause_message_is_saved_and_returned_to_dashboard(client: TestClient, monkeypatch):
    """The generated message reaches both evaluation and detail responses."""
    from sentinel import main

    generated = "Pausamos tu transferencia. Cuelga y llama a tu banco."
    monkeypatch.setattr(main, "generate_pause_message", lambda reasons, settings: generated)
    response = client.post(
        "/v1/evaluate",
        json={
            "payer_external_id": "gemini_test_payer",
            "institution_code": "012",
            "amount": 12500,
            "currency": "MXN",
            "destination_clabe": "072180009999999999",
            "destination_institution_code": "072",
            "proposed_at": datetime(2026, 9, 12, 12).isoformat(),
            "session": {"device_id": "known-device", "is_new_device": False},
            "context": {"active_call": True},
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "pause"
    assert body["payer_message_es"] == generated
    detail = client.get(f"/v1/evaluations/{body['evaluation_id']}").json()
    assert detail["payer_message_es"] == generated
