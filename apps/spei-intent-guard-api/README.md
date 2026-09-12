# SPEI Intent Guard API

FastAPI backend scaffold for the HackMTY Capital One MVP.

## Current Phase

Phase 1 exposes:

- `GET /health`
- `POST /api/v1/users`
- `GET /api/v1/users`
- `POST /api/v1/accounts`
- `GET /api/v1/accounts`
- `POST /api/v1/sessions`
- `GET /api/v1/sessions`
- `POST /api/v1/security-events`
- `GET /api/v1/security-events`
- `POST /api/v1/beneficiaries`
- `GET /api/v1/beneficiaries`
- `POST /api/v1/beneficiary-changes`
- `GET /api/v1/beneficiary-changes`
- `POST /api/v1/limit-changes`
- `GET /api/v1/limit-changes`
- `POST /api/v1/transfers`
- `GET /api/v1/transfers`
- `POST /api/v1/events`
- `GET /api/v1/events`

These endpoints are intentionally simple data-loading and inspection endpoints
for the ER slice. Risk scoring is still a later phase.

## MVP Stack

- Python
- FastAPI
- SQLAlchemy
- Postgres
- Pydantic
- scikit-learn
- pytest
- Ruff
- uv

## Domain Model

The database models currently cover:

- users
- accounts
- beneficiaries
- beneficiary_changes
- sessions
- security_events
- limit_changes
- transfers
- user_baselines
- risk_evaluations
- signal_results
- decision_audits
- events

The model is currently payer-centered: it evaluates whether a transfer looks
abnormal for that payer at that moment. It does not create CONDUSEF complaint
scoring, or any reputation record attached to a person, CURP, or RFC.

A receiver-side layer scoring a **CLABE** — an account, never a person — is in
scope as of 2026-09-12 and is not yet built. See
[`ADR-0002`](../../docs/architechture/ADR-0002-bank-integrated-api-and-receiver-worker.md)
for the architecture and the data-model document for the missing entities.

## Local Commands

Start the local Postgres database:

```bash
docker compose -f compose.db.yaml up -d
```

Install dependencies:

```bash
uv sync --extra dev
```

Create the database tables:

```bash
uv run python scripts/init_db.py
```

Seed synthetic demo cases:

```bash
uv run python scripts/seed_demo_cases.py
```

Seed cases one at a time:

```bash
uv run python scripts/seed_low_risk_case.py
uv run python scripts/seed_medium_risk_case.py
uv run python scripts/seed_high_risk_case.py
```

Reset local synthetic data:

```bash
uv run python scripts/reset_db.py
```

Print seeded decision summaries:

```bash
uv run python scripts/print_demo_summary.py
```

Run the development server:

```bash
uv run uvicorn app.main:app --reload
```

Run tests:

```bash
uv run pytest
```

Run linting:

```bash
uv run ruff check .
```

## Notes

Anomaly signals use `risk_points` from 1 to 5:

- `1`: weak context only
- `3`: meaningful anomaly
- `5`: severe primary anomaly

The seeded cases currently produce:

- low risk: `allow`
- medium risk: `warn`
- high risk: `pause`
