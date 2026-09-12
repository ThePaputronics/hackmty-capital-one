# SPEI Intent Guard Data Model

## Purpose

This document defines the minimum relational data model for the SPEI Intent
Guard MVP. The system scores transfer intent risk for a payer at the moment a
SPEI transfer is about to be submitted.

The model must answer this question:

> How abnormal and potentially manipulated does this transfer look for this
> payer, at this moment?

It must not estimate whether a person or beneficiary is fraudulent.

## MVP Modeling Principles

- Score the transfer, not the receiver as a person.
- Use multiple independent signals before showing strong friction.
- Keep beneficiary data scoped to the payer's relationship with that
  beneficiary.
- Persist only the fields required for event replay, explanation, and demo
  auditability.
- Use synthetic data for the hackathon MVP.
- Keep sensitive financial inference lightweight and explainable.
- Exclude protected attributes, complaint counts, and private receiver
  reputation lists.

## Recommended MVP Entities

## Current Backend Phase

The current backend lives in `apps/spei-intent-guard-api`.

Phase 1 is a data-loading API for the ER slice. It lets the team create and
inspect the payer, transfer-context, and event-stream records needed for demo
data. It does not yet evaluate risk.

Implemented endpoint groups:

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

Next phase:

- Add the risk-evaluation endpoint after demo seed data can be loaded.
- Add signal calculation for the primary MVP anomaly factors.
- Persist `risk_evaluations`, `signal_results`, and `decision_audits` from the
  evaluation flow.

Seed data state:

- `scripts/reset_db.py` drops and recreates local SQLAlchemy-managed tables.
- `scripts/seed_demo_cases.py` creates all synthetic demo cases.
- `scripts/seed_low_risk_case.py` creates a normal transfer case that resolves
  to `allow`.
- `scripts/seed_medium_risk_case.py` creates a suspicious transfer case that
  resolves to `warn`.
- `scripts/seed_high_risk_case.py` creates a high-risk transfer moment that
  resolves to `pause`.
- `scripts/print_demo_summary.py` prints seeded evaluation decisions, risk
  levels, points, and signal keys.

Current seeded demo outcomes:

- Low risk: `allow`, `low`, 1 point.
- Medium risk: `warn`, `medium`, 8 points.
- High risk: `pause`, `high`, 22 points.

## Code Separation

Current app structure:

- `src/app/main.py`: FastAPI application setup, CORS, health endpoint, and
  router registration.
- `src/app/api/er_data.py`: HTTP route handlers for creating and listing ER
  data.
- `src/app/schemas.py`: Pydantic request and response models.
- `src/app/crud.py`: database insert/list helpers.
- `src/app/models.py`: SQLAlchemy tables and relationships.
- `src/app/database.py`: database URL, engine, sessions, and table
  initialization.
- `scripts/init_db.py`: local script that creates the SQLAlchemy tables in the
  configured database.
- `compose.db.yaml`: local Postgres container for development and testing.

Current local database defaults:

- Host: `localhost`
- Port: `5433`
- Database: `spei_intent_guard`
- User: `spei`
- Password: `spei`
- SQLAlchemy URL:
  `postgresql+psycopg://spei:spei@localhost:5433/spei_intent_guard`

Local demo commands:

```bash
cd apps/spei-intent-guard-api
docker compose -f compose.db.yaml up -d
uv sync --extra dev
uv run python scripts/reset_db.py
uv run python scripts/seed_demo_cases.py
uv run python scripts/print_demo_summary.py
uv run uvicorn app.main:app --reload
```

Testing commands:

```bash
cd apps/spei-intent-guard-api
uv run pytest
uv run ruff check .
```

The current shared environment used an existing app virtualenv for validation:

```bash
apps/spei-intent-guard-api/.venv/bin/python -m pytest apps/spei-intent-guard-api/tests
```

Validated result: 5 tests passed, with one non-blocking Starlette/TestClient
deprecation warning from AnyIO.

### users

Represents the payer whose behavior is being evaluated.

Key fields:

- `id`
- `external_user_id`
- `created_at`
- `display_name`
- `risk_profile_version`

Notes:

- Do not store protected attributes such as age, gender, ethnicity,
  nationality, socioeconomic level, or neighborhood risk.
- For the MVP, `display_name` may be synthetic demo data.

### accounts

Represents a payer-owned source account.

Key fields:

- `id`
- `user_id`
- `external_account_id`
- `institution_code`
- `account_type`
- `available_balance`
- `daily_transfer_limit`
- `created_at`
- `updated_at`

Relationships:

- Many accounts belong to one user.
- Transfers originate from one account.

### beneficiaries

Represents a payer-saved destination. This is not a global receiver reputation
record.

Key fields:

- `id`
- `user_id`
- `alias`
- `clabe_token`
- `institution_code`
- `created_at`
- `updated_at`
- `last_used_at`
- `is_active`

Relationships:

- Many beneficiaries belong to one user.
- A transfer may target one beneficiary.

Notes:

- `clabe_token` should be tokenized or synthetic in the MVP.
- Beneficiary name or alias must not be treated as proof of receiver identity.

### beneficiary_changes

Captures sensitive beneficiary events used by anomaly rules.

Key fields:

- `id`
- `beneficiary_id`
- `session_id`
- `change_type`
- `changed_fields`
- `created_at`

Supported `change_type` examples:

- `created`
- `clabe_changed`
- `alias_changed`
- `reactivated`
- `deactivated`

Relationships:

- Many changes belong to one beneficiary.
- A change may be associated with one session.

### sessions

Represents the user session around a sensitive action.

Key fields:

- `id`
- `user_id`
- `started_at`
- `ended_at`
- `channel`
- `device_fingerprint_token`
- `ip_risk_level`
- `geo_risk_level`
- `is_new_device`
- `is_unusual_session`

Relationships:

- Many sessions belong to one user.
- Events, limit changes, beneficiary changes, and transfers may reference a
  session.

Notes:

- Session/device fields are context only. They should not decide fraud alone.

### security_events

Captures user-side security or configuration changes before a transfer.

Key fields:

- `id`
- `user_id`
- `session_id`
- `event_type`
- `created_at`
- `metadata`

Supported `event_type` examples:

- `password_reset`
- `phone_changed`
- `email_changed`
- `mfa_changed`
- `alerts_disabled`
- `auth_method_changed`

Relationships:

- Many security events belong to one user.
- A security event may be associated with one session.

### limit_changes

Captures MTU or transfer-limit changes.

Key fields:

- `id`
- `account_id`
- `session_id`
- `previous_limit`
- `new_limit`
- `created_at`
- `change_ratio`

Relationships:

- Many limit changes belong to one account.
- A limit change may be associated with one session.

### transfers

Represents a proposed or submitted SPEI transfer.

Key fields:

- `id`
- `account_id`
- `beneficiary_id`
- `session_id`
- `amount`
- `currency`
- `created_at`
- `submitted_at`
- `status`
- `description`
- `available_balance_before`
- `available_balance_after`
- `daily_amount_before`
- `daily_amount_after`

Supported `status` examples:

- `draft`
- `evaluated`
- `submitted`
- `cancelled`
- `failed`

Relationships:

- Many transfers originate from one account.
- Many transfers may target one beneficiary.
- One transfer may have one or more risk evaluations.

### user_baselines

Stores payer-specific behavioral expectations.

Key fields:

- `id`
- `user_id`
- `account_id`
- `window_days`
- `avg_transfer_amount`
- `max_usual_transfer_amount`
- `avg_daily_transfer_amount`
- `avg_daily_transfer_count`
- `usual_active_hours`
- `usual_channels`
- `usual_beneficiary_age_days`
- `minimum_residual_balance`
- `computed_at`

Relationships:

- Many baselines may exist for one user/account over time.
- Risk evaluations reference the baseline version used.

Notes:

- For the MVP, baselines can be computed from synthetic seed data.

### risk_evaluations

Stores the result of evaluating one transfer at one point in time.

Key fields:

- `id`
- `transfer_id`
- `baseline_id`
- `evaluated_at`
- `anomaly_score`
- `manipulation_risk_score`
- `decision`
- `risk_level`
- `reason_summary`
- `model_version`
- `ruleset_version`
- `latency_ms`

Supported `decision` values:

- `allow`
- `warn`
- `pause`

Supported `risk_level` values:

- `low`
- `medium`
- `high`

Relationships:

- Many evaluations may belong to one transfer.
- Each evaluation can produce many signal results.
- Each evaluation can produce one decision audit record.

### signal_results

Stores individual signal outputs that explain an evaluation.

Key fields:

- `id`
- `risk_evaluation_id`
- `signal_key`
- `signal_group`
- `severity`
- `risk_points`
- `weight`
- `observed_value`
- `baseline_value`
- `is_primary_signal`
- `explanation`

Supported `signal_group` examples:

- `transfer_amount`
- `velocity_frequency`
- `limit_evasion`
- `beneficiary`
- `limit_configuration`
- `session_device`
- `user_behavior`
- `financial_context`

Relationships:

- Many signal results belong to one risk evaluation.

Notes:

- Signals should explain the decision but not independently decide it.
- At least three reinforcing independent signals should be required before a
  reversible pause.
- `risk_points` uses a 1-5 scale where 1 is weak context and 5 is a severe
  primary signal. Validation should combine independent signal count, severity,
  and total points; points must not let one isolated signal create a fraud
  conclusion.

### decision_audits

Stores the final customer-facing decision and why it happened.

Key fields:

- `id`
- `risk_evaluation_id`
- `action`
- `customer_message`
- `reason_codes`
- `created_at`

Supported `action` examples:

- `none`
- `soft_warning`
- `reversible_pause`
- `manual_continue_allowed`
- `cancelled_by_user`

Relationships:

- One risk evaluation may have one decision audit.

### events

Stores the normalized event stream used to replay the demo and calculate
features.

Key fields:

- `id`
- `user_id`
- `account_id`
- `session_id`
- `event_type`
- `entity_type`
- `entity_id`
- `occurred_at`
- `payload`

Supported `event_type` examples:

- `session_started`
- `beneficiary_created`
- `beneficiary_updated`
- `limit_changed`
- `transfer_drafted`
- `transfer_evaluated`
- `transfer_submitted`
- `transfer_cancelled`
- `security_setting_changed`

Relationships:

- Many events belong to one user.
- Events may reference accounts, sessions, beneficiaries, transfers, or
  evaluations through `entity_type` and `entity_id`.

## Signals To Implement First

Primary MVP signals:

1. Recent MTU increase.
2. Newly registered beneficiary.
3. First transfer to beneficiary.
4. Amount significantly above personal baseline.
5. Multiple transfers just below MTU.
6. Unusual speed between limit change, beneficiary creation, and transfer.
7. Transfer leaves unusually low residual balance.

Secondary MVP signals:

- New device.
- Unusual session or location risk level.
- Atypical hour.
- Recent security data change.
- Retry or duplicate payment behavior.
- Sudden transfer-frequency change.

Production-only signals:

- Receiver fan-in/fan-out across institutions.
- Money movement after receipt.
- Cross-account device/phone/funding-source relationships.
- Mule-account investigation workflows.

## Fields Or Entities To Exclude From The MVP

Do not model these as risk inputs:

- CONDUSEF complaint counts.
- Unadjudicated reports.
- Private suspicious-receiver lists.
- Receiver CURP, INE, RFC, age, gender, ethnicity, nationality, or
  socioeconomic level.
- Beneficiary name, neighborhood, or institution as proof of fraud.
- A global receiver risk score.
- Any single signal as a deterministic fraud decision.

## Practical Decision Rule

- One signal informs.
- Two independent signals create attention.
- Three or more reinforcing independent signals may trigger a reversible pause.

The decision should remain transaction-scoped and explainable.

## MVP Completion Plan

The project is not complete yet. Another agent should continue in this order:

1. Add an anomaly/baseline service.
   - Compute primary MVP signals from the payer's own records.
   - Keep deterministic, explainable rules first.
   - Treat scikit-learn as a supporting anomaly scorer only after the rule
     baseline works.
2. Add `POST /api/v1/risk/evaluate`.
   - Input: transfer context or transfer ID.
   - Output: `allow`, `warn`, or `pause`, risk level, scores, reason codes,
     customer message, and signal breakdown.
   - Persist `risk_evaluations`, `signal_results`, `decision_audits`, and a
     normalized `transfer_evaluated` event.
3. Add tests proving:
   - Low-risk case returns `allow`.
   - Medium-risk case returns `warn`.
   - High-risk case returns `pause`.
   - One isolated signal cannot trigger a pause.
   - Session/device signals are secondary context, not deterministic proof.
4. Build the demo UI.
   - Show the seeded scenarios.
   - Show the transfer draft, signal timeline, risk score, and reversible
     pause/warning message before confirmation.
5. Add a final demo runbook.
   - Include start DB, initialize tables, seed data, start API, start frontend,
     and run the three scenarios.
6. Clean documentation before judging.
   - Keep all final user-facing docs in English.
   - Fix `docs/architechture` typo if the team agrees.
   - Update the ER diagram if any table changes.

ML decision for the MVP:

- Anomaly detection is required.
- Heavy model training is not required for the first functional demo.
- The first implementation should use payer baseline statistics plus
  transparent rules.
- `scikit-learn` can be used later for a small `IsolationForest` or similar
  anomaly score, but the final decision must stay explainable and bounded by
  the practical rule above.
