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

## 6. Declared Caveats & Assumptions

1. **Merchant Category Hops:**
   The challenge brief mentions merchant category hops (MCC). In Mexico, SPEI is an interbank peer-to-peer rail without MCC metadata. Sentinel targets the other two challenge dimensions: velocity bursts and abnormal account behaviors.
2. **Recipient Rail Visibility:**
   Cross-bank fan-in requires platform-level rail observation (e.g. Banco de México). For a single participating bank, Recipient evaluates counterparty novelty for that payer.
3. **Synthetic Ground Truth:**
   Official CONDUSEF metrics track unauthorized transactions rather than authorized coercion. All evaluation labels are synthetically generated and declared as such.
4. **Customer Cancellation Assumption ($p$):**
   The simulation assumes an $85\%$ probability ($p = 0.85$) that an educated payer cancels the transfer when presented with explicit, friction-heavy scam warnings. This is a declared assumption, visibly reported on the dashboard.
