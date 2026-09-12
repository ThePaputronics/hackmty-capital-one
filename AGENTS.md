# Repository Guidelines

## Tech Stack
- Python >=3.11, FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2, PostgreSQL (or SQLite for tests)
- Vanilla HTML/JS for dashboard UI with Tailwind CSS (zero logic in frontend)

## Commands
- Run API tests: `PYTHONPATH=apps/api/src pytest apps/api/tests -v`
- Run Generator tests: `PYTHONPATH=apps/generator/src pytest apps/generator/tests -v`
- Run Evaluation Benchmark: `PYTHONPATH=apps/api/src:apps/generator/src python tools/evaluate/harness.py`
- Run entire stack: `docker compose up --build`

## Conventions
- Features are calculated relative to `as_of` timestamp, never `now()` (reproducible simulated clock).
- High precision monetary amounts use `Numeric(18, 2)` (never `Float`).
- Multi-factor corroboration rule governs decisions (`allow` / `challenge` / `pause`); single signals never trigger alone.
- All code, comments, docstrings, and commits are written in English.
