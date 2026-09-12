# Repository Guidelines

## Tech Stack
- Python >=3.11, FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2, PostgreSQL (or SQLite for tests)
- Vanilla HTML/JS for dashboard UI styled with the Classical design-system stylesheet `apps/ui/styles.css` (zero logic in frontend)

## Commands
- Run API tests: `PYTHONPATH=apps/api/src pytest apps/api/tests -v`
- Run Generator tests: `PYTHONPATH=apps/generator/src pytest apps/generator/tests -v`
- Run Evaluation Benchmark: `PYTHONPATH=apps/api/src:apps/generator/src python tools/evaluate/harness.py`
- Run entire stack: `docker compose up --build`
- Trigger a production deploy: `gh workflow run deploy.yml --ref main` (or push to `main` — see README § Production Deployment)

## Conventions
- Features are calculated relative to `as_of` timestamp, never `now()` (reproducible simulated clock).
- High precision monetary amounts use `Numeric(18, 2)` (never `Float`).
- Multi-factor corroboration rule governs decisions (`allow` / `challenge` / `pause`); single signals never trigger alone.
- Write endpoints depend on `require_api_key` (`X-API-Key`, enforced when `API_KEY_REQUIRED=true`); read endpoints stay public for the dashboard.
- All code, comments, docstrings, and commits are written in English.

## Deployment
- `.github/workflows/deploy.yml` deploys `api`, `generator`, and `ui` as standalone `docker run` containers (no Compose) to a self-hosted GitHub Actions runner, behind a Caddy HTTPS proxy at `sixsevencitos.tech`. Runs on push to `main` or manual dispatch.
- Full details — pipeline steps, server file layout, container list, adding a new service, secrets, troubleshooting — are in README § **6. Production Deployment**. Read it before touching `.github/workflows/deploy.yml` or `deploy/Caddyfile`.
- Per-deploy secrets live in 0600 env files on the server (`postgres.env`, `api.env`, `generator.env` under `/srv/hackathon/apps/capital-one/`), generated once and reused — never commit credentials to the repo or print them in workflow logs.
