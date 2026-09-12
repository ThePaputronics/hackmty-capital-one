"""Main FastAPI application entry point for Sentinel."""

import logging
import time
from contextlib import asynccontextmanager
from datetime import datetime
from decimal import Decimal
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from sentinel.config import get_settings
from sentinel.database import get_db
from sentinel.feature_store import FeatureStore, _to_utc
from sentinel.models import Evaluation, EvaluationSignal, Event, Outcome, Payer
from sentinel.risk import RiskEngine
from sentinel.risk.gemini_message import generate_pause_message
from sentinel.schemas import (
    EvaluateRequest,
    EvaluateResponse,
    EvaluationDetailResponse,
    EvaluationFeedResponse,
    EvaluationSummary,
    EventBatchCreate,
    EventCreate,
    EventIngestResponse,
    OutcomeCreate,
    OutcomeResponse,
    ScoresBreakdown,
    SignalItem,
)

logger = logging.getLogger("sentinel")
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context for startup and shutdown."""
    logger.info("Starting Sentinel SPEI Guard API [Ruleset: %s]", settings.ruleset_version)
    yield
    logger.info("Shutting down Sentinel SPEI Guard API")


app = FastAPI(
    title=settings.app_name,
    description="SPEI Intent & Recipient Guard API — Pre-submission fraud intervention engine",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    """Service health check."""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "environment": settings.environment,
        "ruleset_version": settings.ruleset_version,
    }


# --- Ledger Event Ingestion ---

@app.post("/v1/events", response_model=EventIngestResponse, status_code=status.HTTP_201_CREATED, tags=["Ledger"])
def ingest_event(
    payload: EventCreate | EventBatchCreate,
    db: Session = Depends(get_db),
) -> EventIngestResponse:
    """Ingest one or multiple ledger and security events into the append-only stream."""
    items: list[EventCreate] = payload.events if isinstance(payload, EventBatchCreate) else [payload]
    if not items:
        return EventIngestResponse(accepted=0, status="ok")

    # Cache payer records per batch
    payer_cache: dict[str, Payer] = {}

    for item in items:
        occ_utc = _to_utc(item.occurred_at)
        payer = payer_cache.get(item.payer_external_id)
        if not payer:
            stmt = select(Payer).where(Payer.external_id == item.payer_external_id)
            payer = db.execute(stmt).scalar_one_or_none()
            if not payer:
                payer = Payer(
                    external_id=item.payer_external_id,
                    institution_code=item.institution_code,
                    created_at=occ_utc,
                )
                db.add(payer)
                db.flush()
            payer_cache[item.payer_external_id] = payer

        db_event = Event(
            payer_id=payer.id,
            type=item.type,
            occurred_at=occ_utc,
            payload=item.payload,
        )
        db.add(db_event)

    db.commit()
    return EventIngestResponse(accepted=len(items), status="ok")


# --- Pre-submission Evaluation ---

@app.post("/v1/evaluate", response_model=EvaluateResponse, tags=["Sentinel"])
def evaluate_transfer(
    request: EvaluateRequest,
    db: Session = Depends(get_db),
) -> EvaluateResponse:
    """Evaluate a proposed SPEI transfer against ATO, Intent, and Recipient risk signals."""
    start_time = time.perf_counter()
    prop_utc = _to_utc(request.proposed_at)

    # 1. Resolve or register payer
    stmt = select(Payer).where(Payer.external_id == request.payer_external_id)
    payer = db.execute(stmt).scalar_one_or_none()
    if not payer:
        payer = Payer(
            external_id=request.payer_external_id,
            institution_code=request.institution_code,
            created_at=prop_utc,
        )
        db.add(payer)
        db.flush()

    # 2. Extract baseline and contextual features as of simulated proposed_at
    features = FeatureStore.get_features(
        db=db,
        payer=payer,
        destination_clabe=request.destination_clabe,
        destination_institution_code=request.destination_institution_code,
        as_of=prop_utc,
    )

    # 3. Corroborate signals through RiskEngine
    decision, scores, signals, reason_codes, payer_message_es = RiskEngine.evaluate(
        request=request,
        features=features,
        db=db,
    )

    if decision == "pause":
        payer_message_es = generate_pause_message(reason_codes, settings) or payer_message_es

    elapsed_ms = int((time.perf_counter() - start_time) * 1000)

    # 4. Persist evaluation record
    evaluation = Evaluation(
        payer_id=payer.id,
        destination_clabe=request.destination_clabe,
        destination_institution_code=request.destination_institution_code,
        amount=request.amount,
        currency=request.currency,
        proposed_at=prop_utc,
        decision=decision,
        score_ato=Decimal(str(scores.ato)),
        score_intent=Decimal(str(scores.intent)),
        score_recipient=Decimal(str(scores.recipient)),
        reason_codes=reason_codes,
        payer_message_es=payer_message_es,
        latency_ms=elapsed_ms,
        ruleset_version=settings.ruleset_version,
    )
    db.add(evaluation)
    db.flush()

    # 5. Persist signal explanations
    for sig in signals:
        db_sig = EvaluationSignal(
            evaluation_id=evaluation.id,
            key=sig.key,
            signal_group=sig.signal_group,
            points=sig.points,
            observed=sig.observed,
            baseline=sig.baseline,
            explanation=sig.explanation,
        )
        db.add(db_sig)

    db.commit()

    return EvaluateResponse(
        evaluation_id=evaluation.id,
        payer_external_id=payer.external_id,
        decision=decision,
        scores=scores,
        signals=signals,
        reason_codes=reason_codes,
        payer_message_es=payer_message_es,
        latency_ms=elapsed_ms,
        ruleset_version=settings.ruleset_version,
        evaluated_at=evaluation.evaluated_at,
    )


# --- Outcome Reporting ---

@app.post(
    "/v1/decisions/{evaluation_id}/outcome",
    response_model=OutcomeResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Sentinel"],
)
def report_outcome(
    evaluation_id: int,
    payload: OutcomeCreate,
    db: Session = Depends(get_db),
) -> OutcomeResponse:
    """Record customer outcome (cancelled, continued, verified_callback) for an evaluated transfer."""
    stmt = select(Evaluation).where(Evaluation.id == evaluation_id)
    evaluation = db.execute(stmt).scalar_one_or_none()
    if not evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluation ID not found")

    # Check if outcome already exists
    stmt_out = select(Outcome).where(Outcome.evaluation_id == evaluation_id)
    outcome_record = db.execute(stmt_out).scalar_one_or_none()
    if outcome_record:
        outcome_record.outcome = payload.outcome
        outcome_record.reported_at = datetime.utcnow()
    else:
        outcome_record = Outcome(
            evaluation_id=evaluation_id,
            outcome=payload.outcome,
        )
        db.add(outcome_record)

    db.commit()

    return OutcomeResponse(
        evaluation_id=evaluation_id,
        outcome=outcome_record.outcome,
        recorded=True,
        reported_at=outcome_record.reported_at,
    )


# --- Feed and Drill-Down Endpoints for UI ---

@app.get("/v1/evaluations", response_model=EvaluationFeedResponse, tags=["Dashboard Feed"])
def get_evaluation_feed(
    after: int = Query(0, description="Cursor: return evaluations with id > after"),
    limit: int = Query(50, ge=1, le=200, description="Page limit"),
    db: Session = Depends(get_db),
) -> EvaluationFeedResponse:
    """Fetch incremental evaluations feed for live streaming dashboard."""
    stmt = (
        select(Evaluation)
        .options(selectinload(Evaluation.payer), selectinload(Evaluation.outcome))
        .where(Evaluation.id > after)
        .order_by(Evaluation.id.asc())
        .limit(limit)
    )
    rows = db.execute(stmt).scalars().all()

    items = [
        EvaluationSummary(
            id=row.id,
            payer_external_id=row.payer.external_id if row.payer else f"payer-{row.payer_id}",
            destination_clabe=row.destination_clabe,
            destination_institution_code=row.destination_institution_code,
            amount=row.amount,
            currency=row.currency,
            decision=row.decision,
            score_ato=float(row.score_ato),
            score_intent=float(row.score_intent),
            score_recipient=float(row.score_recipient),
            reason_codes=row.reason_codes or [],
            proposed_at=row.proposed_at,
            evaluated_at=row.evaluated_at,
            outcome=row.outcome.outcome if row.outcome else None,
        )
        for row in rows
    ]

    next_cursor = rows[-1].id if rows else None
    return EvaluationFeedResponse(items=items, next_cursor=next_cursor)


@app.get("/v1/evaluations/{evaluation_id}", response_model=EvaluationDetailResponse, tags=["Dashboard Feed"])
def get_evaluation_detail(
    evaluation_id: int,
    db: Session = Depends(get_db),
) -> EvaluationDetailResponse:
    """Fetch complete drill-down evaluation details including signals and Spanish mobile message."""
    stmt = (
        select(Evaluation)
        .options(
            selectinload(Evaluation.payer),
            selectinload(Evaluation.signals),
            selectinload(Evaluation.outcome),
        )
        .where(Evaluation.id == evaluation_id)
    )
    row = db.execute(stmt).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluation not found")

    signals = [
        SignalItem(
            key=s.key,
            signal_group=s.signal_group,
            points=s.points,
            observed=s.observed,
            baseline=s.baseline,
            explanation=s.explanation,
        )
        for s in row.signals
    ]

    outcome_resp = (
        OutcomeResponse(
            evaluation_id=row.outcome.evaluation_id,
            outcome=row.outcome.outcome,
            recorded=True,
            reported_at=row.outcome.reported_at,
        )
        if row.outcome
        else None
    )

    return EvaluationDetailResponse(
        evaluation_id=row.id,
        payer_external_id=row.payer.external_id if row.payer else f"payer-{row.payer_id}",
        amount=row.amount,
        currency=row.currency,
        destination_clabe=row.destination_clabe,
        destination_institution_code=row.destination_institution_code,
        proposed_at=row.proposed_at,
        decision=row.decision,
        scores=ScoresBreakdown(
            ato=float(row.score_ato),
            intent=float(row.score_intent),
            recipient=float(row.score_recipient),
        ),
        signals=signals,
        reason_codes=row.reason_codes or [],
        payer_message_es=row.payer_message_es,
        latency_ms=row.latency_ms,
        ruleset_version=row.ruleset_version,
        evaluated_at=row.evaluated_at,
        outcome=outcome_resp,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sentinel.main:app", host=settings.host, port=settings.port, reload=True)
