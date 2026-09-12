# Sentinel — SPEI Intent & Recipient Guard

> **HackMTY — Real-Time Anomaly & Security Sentinel**  
> Behavioral anomaly detection engine analyzing transaction ledgers in real time to intercept social-engineering coercion and APP (Authorized Push Payment) fraud before SPEI transfer execution.

---

## 1. The Core Problem

In Mexico, SPEI transactions settle irreversibly within seconds. When a genuine bank customer falls victim to telephone social engineering (fake banking executive, virtual kidnapping, coerced screen sharing), the victim authenticates normally with their password and biometrics. Traditional fraud systems ask:

> *"Is this the authorized user?"* → **YES** (Authentication succeeds)

Sentinel asks the right question:

> *"Is this authenticated user currently being manipulated or coerced?"*

By evaluating behavioral shifts, session telemetry, MTU regulatory cap structuring, and recipient network novelty simultaneously, Sentinel inserts **reversible, explained friction** (cooldown pauses and specific fraud warnings in Spanish) directly in the mobile banking app before funds enter the interbank rail.

---

## 2. Architecture & Design Principles

```
  generator/player ──POST /v1/events──────▶ ┌──────────────┐
  (acts as bank)   ──POST /v1/evaluate───▶ │ Sentinel API │──▶ PostgreSQL (RDS)
                   ──POST /outcome───────▶ │  (Product)   │
         │                                 └──────────────┘
         │ hidden labels                          ▲
         │ + clock + counters                     │ GET /v1/evaluations?after=cursor
         ▼                                        │ GET /v1/evaluations/{id}
   GET /sim/status                                │
         ▲                                        │
         └───────────── Dashboard UI ─────────────┘
                     (Zero logic, 1 Hz poll)
```

1. **Multi-Factor Corroboration (No Single-Signal False Alarms):**
   Decisions (`allow` / `challenge` / `pause`) require multiple independent risk dimensions (ATO, Intent, Recipient) to corroborate. Single high-value transfers or new contacts alone do not block transactions.
2. **Features relative to `as_of` (Simulated Clock):**
   Baselines and velocity windows are calculated strictly against the transaction's simulated timestamp, never wall-clock `now()`. This enables fully deterministic, reproducible replays.
3. **Stateless API, AWS-Scalable:**
   All state lives in standard PostgreSQL with Alembic migrations. Containerized and 12-factor compliant. Pause evaluations may take longer when Gemini generates the customer message.
4. **Zero-Logic UI:**
   The dashboard is a pure static viewer polling two endpoints: the public API (what a bank sees) and the generator (simulation ground truth).

---

## 3. API Contract

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/v1/events` | Append-only ledger ingestion (`transfer_settled`, `beneficiary_added`, `limit_changed`, `device_seen`) |
| `POST` | `/v1/evaluate` | Synchronous pre-submission evaluation returning decision, scores, explainability signals, and Spanish guidance |
| `POST` | `/v1/decisions/{id}/outcome` | Reporting final customer disposition (`cancelled`, `continued`, `verified_callback`) |
| `GET` | `/v1/evaluations` | Cursor-paginated incremental feed for live streaming dashboards |
| `GET` | `/v1/evaluations/{id}` | Drill-down detail with full signal breakdowns and mobile screen copy |
| `GET` | `/health` | Service health and active ruleset version |

When `API_KEY_REQUIRED=true`, the three `POST` endpoints require the institution key in the `X-API-Key` header (`INSTITUTION_API_KEY` on the API, `API_KEY` on the generator). The deployed stack enforces it; local Compose leaves it off. The `GET` endpoints stay public so the dashboard can read the feed.

---

## 4. Quickstart

### Option A: Docker Compose (Recommended)

Run all services (PostgreSQL, Sentinel API, Stream Generator, Dashboard UI) with one command:

```bash
docker compose up --build
```

To generate short protection-pause messages with Gemini, set `GEMINI_API_KEY` in your environment before starting Compose. The API uses `gemini-3.6-flash` by default; set `GEMINI_MODEL` to change it. The key stays in the API service. If it is missing or Gemini is unavailable, the API uses a concise Spanish template. Only pause messages use Gemini; the risk decision is always rule-based.

- **Dashboard UI:** [http://localhost:3000](http://localhost:3000)
- **Sentinel API & Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Simulation Status:** [http://localhost:8001/sim/status](http://localhost:8001/sim/status)

Click **"Iniciar demo"** on the dashboard to start the live 30-day accelerated replay.

### Option B: Local Python Development

1. **Install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e apps/api -e apps/generator
   ```

2. **Run tests:**
   ```bash
   PYTHONPATH=apps/api/src pytest apps/api/tests -v
   PYTHONPATH=apps/generator/src pytest apps/generator/tests -v
   ```

3. **Run the Calibration & Evaluation Benchmark:**
   ```bash
   PYTHONPATH=apps/api/src:apps/generator/src python tools/evaluate/harness.py --days 30 --seed 42
   ```

---

## 5. Evaluation Benchmark & Subgroup Results

Running `tools/evaluate/harness.py` runs a full 90-day warmup followed by a 30-day active stream containing 52 diverse personas (consumers, small businesses, and attack targets) with hidden ground truth:

```text
==================================================================
      SENTINEL - EVALUATION & CALIBRATION BENCHMARK REPORT        
==================================================================
Total Transfers Evaluated: 615
Latency: p50 = 1.06 ms | p95 = 1.37 ms (In-request, sub-second)
------------------------------------------------------------------
1. APP FRAUD PROTECTION (Social Engineering Coercion)
   - Attack Attempts: 6 | Intercepted: 6
   - Detection Recall: 100.0%
   - Value at Risk: $146,800.00 MXN
   - Value Intercepted: $146,800.00 MXN
   - Value-Weighted Recall: 100.0%
------------------------------------------------------------------
2. SUBGROUP TESTING (False Alarm Discipline)
   - Regular Consumer False Positive Rate: 0.0% (Target: <= 1.0%)
   - Small Merchant (Changarro) False Positive Rate: 0.0%
------------------------------------------------------------------
3. ARCHITECTURAL PROOF: Corroboration vs Naive Weighted Sum
   Multi-Factor Corroboration:
     * Merchant FP Rate: 0.0% | Consumer FP Rate: 0.0% | Recall: 100%
   Naive Weighted Sum:
     * High false alarm exposure on legitimate high-frequency accounts
==================================================================
```

---

## 6. Production Deployment

The stack runs live at **[https://sixsevencitos.tech](https://sixsevencitos.tech)** ([`/docs`](https://sixsevencitos.tech/docs), [`/sim/status`](https://sixsevencitos.tech/sim/status)), deployed by `.github/workflows/deploy.yml` to a GitHub Actions **self-hosted runner** (labels `[self-hosted, Linux, X64, hackathon]`) on a shared hackathon server. It does not use `compose.yaml` — each service is a standalone `docker run` container, since the runner's host manages multiple hackathon projects and Compose would namespace-collide with them.

### How to deploy

- **Automatic:** push (or merge) to `main`. Every push runs the full pipeline.
- **Manual:** GitHub → **Actions** → **Deploy** → **Run workflow**, pick a branch. Or with the CLI:
  ```bash
  gh workflow run deploy.yml --ref <branch>
  gh run watch          # follow the run; the summary links the deployed URLs
  ```
- Deploys are serialized (`concurrency: deploy-hackathon-server`, `cancel-in-progress: false`) — a second push queues behind one already running instead of racing it.
- There is no separate staging environment; whatever lands on `main` goes to the live domain. Check locally with `docker compose up --build` before merging.

### What the pipeline does

1. **Stage the release** — `git archive` of the deployed commit into `/srv/hackathon/apps/capital-one/releases/<sha>` (mirrors the `hello-world` app already on that runner).
2. **Build images** — `api`, `generator`, `ui`, each tagged `<sha>` and `latest`.
3. **Write environment files** (0600, `ramon`-only, under `/srv/hackathon/apps/capital-one/`):
   - `postgres.env` — Postgres user/password, generated once on first deploy and reused after (rotating it would orphan the existing data volume).
   - `api.env` — `DATABASE_URL`, `API_KEY_REQUIRED=true`, `INSTITUTION_API_KEY` (generated once, stable across deploys), and `GEMINI_API_KEY` from the `GEMINI_API_KEY` repo secret (a warning is logged, not a failure, if the secret is empty — Gemini messages just fall back to the static template).
   - `generator.env` — `API_KEY`, the same value as `INSTITUTION_API_KEY`, so the generator can call the protected write endpoints.
4. **Postgres** — created once (`hackathon-capital-one-postgres`) and left running across deploys; the pipeline only waits for its health check, never rebuilds it.
5. **App containers** — `api`, `generator`, `ui` are stopped, removed, and recreated from the new images (`docker rm -f` + `docker run`), each waited on via its health/status endpoint before the next one starts (the API runs Alembic migrations on boot, so it comes up before the generator and UI).
6. **HTTPS proxy** — a Caddy container (`deploy/Caddyfile`) terminates TLS for `sixsevencitos.tech` (auto-issued Let's Encrypt certificate, renewed automatically, stored in a named volume so it survives redeploys) and routes by path: `/v1/*`, `/health`, `/docs`, `/redoc`, `/openapi.json` → API; `/sim/*` → generator; everything else → the dashboard. `www` redirects to the bare domain; plain HTTP redirects to HTTPS. The Caddyfile is validated before the running proxy is ever replaced.
7. **Release bookkeeping** — writes `current-tag`, keeps the last 5 release directories and images, prunes the rest.
8. **On failure** — the last 100 log lines of every container are dumped to the run's output.

### Server layout

```
/srv/hackathon/apps/capital-one/
├── releases/<sha>/          # git archive of each deployed commit (last 5 kept)
├── current-tag              # sha of the currently live release
├── postgres.env             # 0600 — DB credentials (generated once)
├── api.env                  # 0600 — DATABASE_URL, API_KEY_REQUIRED, INSTITUTION_API_KEY, GEMINI_API_KEY
└── generator.env            # 0600 — API_KEY for the generator's calls to the API
```

Containers (`docker ps --filter label=io.hackathon.project=capital-one`), all on the private `hackathon-capital-one` network:

| Container | Image | Published | Notes |
|---|---|---|---|
| `hackathon-capital-one-postgres` | `postgres:16-alpine` | — (network-only) | long-lived, not recreated per deploy |
| `hackathon-capital-one-api` | built from `apps/api/Dockerfile` | `127.0.0.1:8000` | runs migrations on start |
| `hackathon-capital-one-generator` | built from `apps/generator/Dockerfile` | `127.0.0.1:8001` | `AUTO_START=false` |
| `hackathon-capital-one-ui` | built from `apps/ui/Dockerfile` | `127.0.0.1:3000` | |
| `hackathon-capital-one-proxy` | `caddy:2-alpine` | `0.0.0.0:80`, `0.0.0.0:443` | only container reachable from the internet |

App ports are bound to `127.0.0.1` — the internet reaches the stack only through Caddy on 80/443. Postgres publishes no host port at all; only containers on the `hackathon-capital-one` network can reach it.

### Adding a new service to the deploy

1. Give it a `Dockerfile` under `apps/<name>/`.
2. Add it to the build loop (`for svc in api generator ui; do`) in the **Build images** step.
3. Add a `replace "$IMAGE_PREFIX-<name>" --network-alias <name> ... "$IMAGE_PREFIX-<name>:$GITHUB_SHA"` call in **Deploy application containers**, followed by a `wait_http` check against its health endpoint.
4. If it needs to be public, add a route for it in `deploy/Caddyfile` (path-based `handle` block, like `/sim/*`); if it's internal-only (called by other containers, not by the browser), it just needs the `--network-alias` and no Caddy route.
5. If it needs secrets, extend the **Write container environment files** step and give it its own `<name>.env` file rather than inlining values on the `docker run` command line (`ps` would show those).

### Secrets

- `GEMINI_API_KEY` is a **GitHub Actions repository secret** (Settings → Secrets and variables → Actions), referenced in the workflow as `${{ secrets.GEMINI_API_KEY }}`. Rotate it with `gh secret set GEMINI_API_KEY` — the next deploy picks it up automatically.
- `INSTITUTION_API_KEY` and the Postgres password are **not** GitHub secrets; they're generated on the server on first deploy and persisted in the 0600 env files above, so they survive redeploys without needing to round-trip through GitHub. To read the live institution key (e.g. to call a write endpoint by hand, or hand it to a judge):
  ```bash
  ssh ramon@209.126.9.18 'cat /srv/hackathon/apps/capital-one/institution-api-key.env'
  ```

### Troubleshooting

- **Watch a run:** `gh run list --workflow deploy.yml` then `gh run watch <id>`.
- **Container logs:** `ssh ramon@209.126.9.18 'sudo docker logs --tail 200 hackathon-capital-one-api'` (swap the container name; `sudo` needs no password for `ramon` on this box).
- **HTTPS not live right after a DNS change:** the pipeline warns (doesn't fail) if `https://sixsevencitos.tech/health` isn't reachable yet — Let's Encrypt needs the A record to already resolve to the server. Re-run the workflow (or just push again) once `dig +short sixsevencitos.tech` returns `209.126.9.18`.
- **A deploy is stuck/queued:** check `gh run list --workflow deploy.yml` — only one run executes at a time by design.

---

## 7. Declared Caveats & Assumptions

1. **Merchant Category Hops:**
   The challenge brief mentions merchant category hops (MCC). In Mexico, SPEI is an interbank peer-to-peer rail without MCC metadata. Sentinel targets the other two challenge dimensions: velocity bursts and abnormal account behaviors.
2. **Recipient Rail Visibility:**
   Cross-bank fan-in requires platform-level rail observation (e.g. Banco de México). For a single participating bank, Recipient evaluates counterparty novelty for that payer.
3. **Synthetic Ground Truth:**
   Official CONDUSEF metrics track unauthorized transactions rather than authorized coercion. All evaluation labels are synthetically generated and declared as such.
4. **Customer Cancellation Assumption ($p$):**
   The simulation assumes an $85\%$ probability ($p = 0.85$) that an educated payer cancels the transfer when presented with explicit, friction-heavy scam warnings. This is a declared assumption, visibly reported on the dashboard.
