"""Evaluation and calibration harness for Sentinel risk scoring."""

import argparse
from datetime import datetime
from decimal import Decimal
import json
import statistics
import time
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from generator.simulation import StreamSimulator
from sentinel.database import Base
from sentinel.feature_store import FeatureStore
from sentinel.models import Event, Payer
from sentinel.risk import RiskEngine
from sentinel.schemas import EvaluateRequest, SessionContext, DeviceContext


def run_benchmark(seed: int = 42, active_days: int = 30) -> dict[str, Any]:
    """Execute complete simulated stream in-memory and compute calibration metrics."""
    # 1. Setup isolated in-memory DB
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db: Session = SessionMaker()

    # 2. Setup simulation
    start_date = datetime(2026, 6, 1, 0, 0, 0)
    sim = StreamSimulator(start_date=start_date, warmup_days=90, active_days=active_days, seed=seed)

    print("--- [1/3] Loading Warmup Ledger Events (90 days) ---")
    warmup_events = sim.generate_warmup_events()
    payer_cache: dict[str, Payer] = {}

    for ev in warmup_events:
        pid = ev["payer_external_id"]
        payer = payer_cache.get(pid)
        if not payer:
            payer = Payer(
                external_id=pid,
                institution_code=ev["institution_code"],
                created_at=datetime.fromisoformat(ev["occurred_at"]),
            )
            db.add(payer)
            db.flush()
            payer_cache[pid] = payer

        db_ev = Event(
            payer_id=payer.id,
            type=ev["type"],
            occurred_at=datetime.fromisoformat(ev["occurred_at"]),
            payload=ev["payload"],
        )
        db.add(db_ev)
    db.commit()
    print(f"Loaded {len(warmup_events)} warmup events across {len(payer_cache)} payers.")

    print(f"--- [2/3] Simulating {active_days}-Day Active Stream with Hidden Labels ---")
    latencies: list[float] = []

    # Counters
    total_evals = 0
    genuine_normal_count = 0
    genuine_merchant_count = 0
    app_scam_count = 0
    ato_attack_count = 0

    app_value_total = 0.0
    app_value_intercepted = 0.0

    # Decision counts for corroboration engine
    genuine_normal_challenges_corrob = 0
    genuine_merchant_challenges_corrob = 0
    app_scams_detected_corrob = 0
    ato_attacks_detected_corrob = 0

    # Decision counts for naive weighted-sum baseline (for comparison)
    # Naive rule: 0.35*ato + 0.50*intent + 0.15*recipient >= 0.35 -> flag
    genuine_normal_challenges_sum = 0
    genuine_merchant_challenges_sum = 0
    app_scams_detected_sum = 0

    for day in range(1, active_days + 1):
        daily_transfers = sim.generate_active_day_transfers(day)
        for item in daily_transfers:
            # 1. Ingest prerequisites
            for pre in item.prerequisite_events:
                pid = pre["payer_external_id"]
                payer = payer_cache[pid]
                db_ev = Event(
                    payer_id=payer.id,
                    type=pre["type"],
                    occurred_at=datetime.fromisoformat(pre["occurred_at"]),
                    payload=pre["payload"],
                )
                db.add(db_ev)
            if item.prerequisite_events:
                db.commit()

            # 2. Build EvaluateRequest
            req_data = item.evaluate_request
            req = EvaluateRequest(
                payer_external_id=req_data["payer_external_id"],
                institution_code=req_data["institution_code"],
                amount=Decimal(str(req_data["amount"])),
                currency=req_data["currency"],
                destination_clabe=req_data["destination_clabe"],
                destination_institution_code=req_data["destination_institution_code"],
                proposed_at=datetime.fromisoformat(req_data["proposed_at"]),
                session=SessionContext(**req_data["session"]),
                context=DeviceContext(**req_data["context"]),
            )

            # 3. Evaluate and measure latency
            payer = payer_cache[req.payer_external_id]
            t_start = time.perf_counter()
            features = FeatureStore.get_features(
                db=db,
                payer=payer,
                destination_clabe=req.destination_clabe,
                destination_institution_code=req.destination_institution_code,
                as_of=req.proposed_at,
            )
            decision, scores, signals, reason_codes, _ = RiskEngine.evaluate(
                request=req,
                features=features,
                db=db,
            )
            elapsed_ms = (time.perf_counter() - t_start) * 1000.0
            latencies.append(elapsed_ms)

            # 4. Compare with naive weighted sum baseline
            naive_score = 0.35 * scores.ato + 0.50 * scores.intent + 0.15 * scores.recipient
            naive_flagged = naive_score >= 0.35

            gt = item.ground_truth
            amt = float(req.amount)
            total_evals += 1

            if gt.is_app_fraud:
                app_scam_count += 1
                app_value_total += amt
                if decision in ("pause", "challenge"):
                    app_scams_detected_corrob += 1
                    app_value_intercepted += amt
                if naive_flagged:
                    app_scams_detected_sum += 1

            elif gt.is_ato_fraud:
                ato_attack_count += 1
                if decision in ("pause", "challenge"):
                    ato_attacks_detected_corrob += 1

            else:
                if gt.persona_type == "merchant":
                    genuine_merchant_count += 1
                    if decision in ("pause", "challenge"):
                        genuine_merchant_challenges_corrob += 1
                    if naive_flagged:
                        genuine_merchant_challenges_sum += 1
                else:
                    genuine_normal_count += 1
                    if decision in ("pause", "challenge"):
                        genuine_normal_challenges_corrob += 1
                    if naive_flagged:
                        genuine_normal_challenges_sum += 1

    # 5. Compute Metrics
    latencies.sort()
    p50_latency = statistics.median(latencies) if latencies else 0.0
    p95_latency = latencies[int(len(latencies) * 0.95)] if latencies else 0.0

    app_recall_corrob = (app_scams_detected_corrob / app_scam_count) if app_scam_count > 0 else 0.0
    app_weighted_recall = (app_value_intercepted / app_value_total) if app_value_total > 0 else 0.0

    normal_fp_corrob = (genuine_normal_challenges_corrob / genuine_normal_count) if genuine_normal_count > 0 else 0.0
    merchant_fp_corrob = (genuine_merchant_challenges_corrob / genuine_merchant_count) if genuine_merchant_count > 0 else 0.0

    normal_fp_sum = (genuine_normal_challenges_sum / genuine_normal_count) if genuine_normal_count > 0 else 0.0
    merchant_fp_sum = (genuine_merchant_challenges_sum / genuine_merchant_count) if genuine_merchant_count > 0 else 0.0

    results = {
        "summary": {
            "total_transfers_evaluated": total_evals,
            "genuine_normal_transfers": genuine_normal_count,
            "genuine_merchant_transfers": genuine_merchant_count,
            "app_scam_attacks": app_scam_count,
            "ato_attacks": ato_attack_count,
            "latency_p50_ms": round(p50_latency, 2),
            "latency_p95_ms": round(p95_latency, 2),
        },
        "app_fraud_protection": {
            "attempts": app_scam_count,
            "intercepted": app_scams_detected_corrob,
            "detection_recall": round(app_recall_corrob * 100, 2),
            "value_at_risk_mxn": round(app_value_total, 2),
            "value_intercepted_mxn": round(app_value_intercepted, 2),
            "value_weighted_recall_pct": round(app_weighted_recall * 100, 2),
        },
        "ato_protection": {
            "attempts": ato_attack_count,
            "intercepted": ato_attacks_detected_corrob,
            "recall_pct": round((ato_attacks_detected_corrob / ato_attack_count) * 100, 2) if ato_attack_count else 0,
        },
        "subgroup_false_positive_rates": {
            "genuine_consumers_fp_rate_pct": round(normal_fp_corrob * 100, 2),
            "small_merchants_fp_rate_pct": round(merchant_fp_corrob * 100, 2),
        },
        "architecture_comparison": {
            "multi_factor_corroboration": {
                "consumer_fp_pct": round(normal_fp_corrob * 100, 2),
                "merchant_fp_pct": round(merchant_fp_corrob * 100, 2),
                "app_recall_pct": round(app_recall_corrob * 100, 2),
            },
            "naive_weighted_sum_baseline": {
                "consumer_fp_pct": round(normal_fp_sum * 100, 2),
                "merchant_fp_pct": round(merchant_fp_sum * 100, 2),
                "app_recall_pct": round((app_scams_detected_sum / app_scam_count) * 100, 2) if app_scam_count else 0,
            },
        },
    }
    return results


def print_report(results: dict[str, Any]) -> None:
    """Format and display calibration report in terminal."""
    s = results["summary"]
    app_f = results["app_fraud_protection"]
    ato_f = results["ato_protection"]
    sub = results["subgroup_false_positive_rates"]
    comp = results["architecture_comparison"]

    print("\n==================================================================")
    print("      SENTINEL - EVALUATION & CALIBRATION BENCHMARK REPORT        ")
    print("==================================================================")
    print(f"Total Transfers Evaluated: {s['total_transfers_evaluated']}")
    print(f"Latency: p50 = {s['latency_p50_ms']} ms | p95 = {s['latency_p95_ms']} ms (In-request, sub-second)")
    print("------------------------------------------------------------------")
    print("1. APP FRAUD PROTECTION (Social Engineering Coercion)")
    print(f"   - Attack Attempts: {app_f['attempts']} | Intercepted: {app_f['intercepted']}")
    print(f"   - Detection Recall: {app_f['detection_recall']}%")
    print(f"   - Value at Risk: ${app_f['value_at_risk_mxn']:,.2f} MXN")
    print(f"   - Value Intercepted: ${app_f['value_intercepted_mxn']:,.2f} MXN")
    print(f"   - Value-Weighted Recall: {app_f['value_weighted_recall_pct']}%")
    print("------------------------------------------------------------------")
    print("2. ATO ATTACKS (Credential / Device Takeover)")
    print(f"   - Attempts: {ato_f['attempts']} | Intercepted: {ato_f['intercepted']}")
    print(f"   - Recall: {ato_f['recall_pct']}%")
    print("------------------------------------------------------------------")
    print("3. SUBGROUP TESTING (False Alarm Discipline)")
    print(f"   - Regular Consumer False Positive Rate: {sub['genuine_consumers_fp_rate_pct']}% (Target: <= 1.0%)")
    print(f"   - Small Merchant (Changarro) False Positive Rate: {sub['small_merchants_fp_rate_pct']}%")
    print("------------------------------------------------------------------")
    print("4. ARCHITECTURAL PROOF: Corroboration vs Naive Weighted Sum")
    print(f"   Multi-Factor Corroboration (Sentinel):")
    print(f"     * Merchant FP Rate: {comp['multi_factor_corroboration']['merchant_fp_pct']}%")
    print(f"     * Consumer FP Rate: {comp['multi_factor_corroboration']['consumer_fp_pct']}%")
    print(f"     * Fraud Recall:    {comp['multi_factor_corroboration']['app_recall_pct']}%")
    print(f"   Naive Weighted Sum (Single-Signal False Alarms):")
    print(f"     * Merchant FP Rate: {comp['naive_weighted_sum_baseline']['merchant_fp_pct']}%")
    print(f"     * Consumer FP Rate: {comp['naive_weighted_sum_baseline']['consumer_fp_pct']}%")
    print(f"     * Fraud Recall:    {comp['naive_weighted_sum_baseline']['app_recall_pct']}%")
    print("==================================================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentinel Calibration and Evaluation Harness")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for deterministic replay")
    parser.add_argument("--days", type=int, default=30, help="Simulated active days")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of text report")

    args = parser.parse_args()
    res = run_benchmark(seed=args.seed, active_days=args.days)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print_report(res)
