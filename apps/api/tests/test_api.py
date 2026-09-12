"""Comprehensive tests for Sentinel API."""

from datetime import datetime, timedelta
from decimal import Decimal
import pytest
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Verify health check endpoint returns 200 and version."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data
    assert "ruleset_version" in data


def test_event_ingest_single_and_batch(client: TestClient):
    """Verify single and batch ledger events ingestion."""
    now = datetime(2026, 9, 12, 12, 0, 0)

    # 1. Single event
    res1 = client.post(
        "/v1/events",
        json={
            "payer_external_id": "payer_ana_01",
            "institution_code": "012",  # BBVA
            "type": "beneficiary_added",
            "occurred_at": now.isoformat(),
            "payload": {
                "destination_clabe": "012180001234567890",
                "destination_institution_code": "012",
                "alias": "Mama",
            },
        },
    )
    assert res1.status_code == 201
    assert res1.json()["accepted"] == 1

    # 2. Batch event
    res2 = client.post(
        "/v1/events",
        json={
            "events": [
                {
                    "payer_external_id": "payer_ana_01",
                    "institution_code": "012",
                    "type": "transfer_settled",
                    "occurred_at": (now + timedelta(minutes=5)).isoformat(),
                    "payload": {
                        "amount": 1200.00,
                        "destination_clabe": "012180001234567890",
                        "destination_institution_code": "012",
                        "balance_after": 25000.00,
                    },
                },
                {
                    "payer_external_id": "payer_ana_01",
                    "institution_code": "012",
                    "type": "device_seen",
                    "occurred_at": (now + timedelta(minutes=6)).isoformat(),
                    "payload": {"device_id": "phone_ana_iphone15"},
                },
            ]
        },
    )
    assert res2.status_code == 201
    assert res2.json()["accepted"] == 2


def test_normal_transfer_returns_allow(client: TestClient):
    """Verify legitimate transaction to known beneficiary from recognized device results in allow."""
    t0 = datetime(2026, 9, 1, 10, 0, 0)
    dest_clabe = "012180001234567890"

    # Seed 90d history: Ana transfers to Mom
    client.post(
        "/v1/events",
        json={
            "events": [
                {
                    "payer_external_id": "payer_ana_normal",
                    "institution_code": "012",
                    "type": "transfer_settled",
                    "occurred_at": t0.isoformat(),
                    "payload": {
                        "amount": 2500.00,
                        "destination_clabe": dest_clabe,
                        "destination_institution_code": "012",
                        "balance_after": 30000.00,
                    },
                },
                {
                    "payer_external_id": "payer_ana_normal",
                    "institution_code": "012",
                    "type": "device_seen",
                    "occurred_at": t0.isoformat(),
                    "payload": {"device_id": "device_ana_known"},
                },
            ]
        },
    )

    # Evaluate new transfer: same beneficiary, recognized device, normal amount
    t_eval = t0 + timedelta(days=5, hours=2)
    response = client.post(
        "/v1/evaluate",
        json={
            "payer_external_id": "payer_ana_normal",
            "institution_code": "012",
            "amount": 1800.00,
            "currency": "MXN",
            "destination_clabe": dest_clabe,
            "destination_institution_code": "012",
            "proposed_at": t_eval.isoformat(),
            "session": {
                "device_id": "device_ana_known",
                "is_new_device": False,
                "ip_risk": "low",
                "geo_risk": "low",
            },
            "context": {
                "active_call": False,
                "screen_share": False,
                "remote_access": False,
            },
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "allow"
    assert data["scores"]["ato"] == 0.0
    assert data["scores"]["recipient"] == 0.0
    assert "No se detectaron anomalías" in data["payer_message_es"]


def test_coerced_victim_under_call_triggers_pause(client: TestClient):
    """Verify victim guided by phone scammer to add new beneficiary and transfer near MTU cap triggers PAUSE."""
    t0 = datetime(2026, 9, 10, 10, 0, 0)
    known_clabe = "012180001111111111"
    new_mule_clabe = "072180009999999999"

    # Baseline: small usual transfers of $500 MXN
    client.post(
        "/v1/events",
        json={
            "events": [
                {
                    "payer_external_id": "victim_carlos",
                    "institution_code": "012",
                    "type": "transfer_settled",
                    "occurred_at": (t0 - timedelta(days=10)).isoformat(),
                    "payload": {
                        "amount": 500.00,
                        "destination_clabe": known_clabe,
                        "destination_institution_code": "012",
                        "balance_after": 14000.00,
                    },
                },
                # Coercion timeline: scammer calls, victim adds mule beneficiary 4 mins ago
                {
                    "payer_external_id": "victim_carlos",
                    "institution_code": "012",
                    "type": "beneficiary_added",
                    "occurred_at": (t0 - timedelta(minutes=4)).isoformat(),
                    "payload": {
                        "destination_clabe": new_mule_clabe,
                        "destination_institution_code": "072",  # Banorte
                        "alias": "Cuenta Segura Banxico",
                    },
                },
            ]
        },
    )

    # Scammer tells victim to send $12,500 MXN (right below 1,500 UDIs MTU cap) while on the phone
    response = client.post(
        "/v1/evaluate",
        json={
            "payer_external_id": "victim_carlos",
            "institution_code": "012",
            "amount": 12500.00,
            "currency": "MXN",
            "destination_clabe": new_mule_clabe,
            "destination_institution_code": "072",
            "proposed_at": t0.isoformat(),
            "session": {
                "device_id": "device_carlos",
                "is_new_device": False,
                "ip_risk": "low",
                "geo_risk": "low",
            },
            "context": {
                "active_call": True,  # Telemetry: phone call active during transfer
                "screen_share": False,
                "remote_access": False,
            },
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "pause"
    assert "ACTIVE_CALL_MANIPULATION" in data["reason_codes"]
    assert "NEW_DESTINATION_RISK" in data["reason_codes"]
    assert "Pausamos esta transferencia" in data["payer_message_es"]
    assert len(data["payer_message_es"]) <= 220

    # Verify outcome reporting
    eval_id = data["evaluation_id"]
    out_res = client.post(
        f"/v1/decisions/{eval_id}/outcome",
        json={"outcome": "cancelled"},
    )
    assert out_res.status_code == 201
    assert out_res.json()["outcome"] == "cancelled"


def test_feed_and_drill_down_endpoints(client: TestClient):
    """Verify live feed pagination and detailed inspection drill-down."""
    t0 = datetime(2026, 9, 12, 14, 0, 0)
    clabe = "012180005555555555"

    eval_res = client.post(
        "/v1/evaluate",
        json={
            "payer_external_id": "feed_payer",
            "institution_code": "012",
            "amount": 500.00,
            "currency": "MXN",
            "destination_clabe": clabe,
            "destination_institution_code": "012",
            "proposed_at": t0.isoformat(),
            "session": {"device_id": "dev1", "is_new_device": False},
            "context": {"active_call": False},
        },
    )
    eval_id = eval_res.json()["evaluation_id"]

    # Test feed cursor
    feed_res = client.get("/v1/evaluations?after=0&limit=10")
    assert feed_res.status_code == 200
    feed_data = feed_res.json()
    assert len(feed_data["items"]) >= 1
    assert feed_data["items"][-1]["id"] == eval_id

    # Test drill-down
    detail_res = client.get(f"/v1/evaluations/{eval_id}")
    assert detail_res.status_code == 200
    detail = detail_res.json()
    assert detail["evaluation_id"] == eval_id
    assert "scores" in detail
    assert "signals" in detail
