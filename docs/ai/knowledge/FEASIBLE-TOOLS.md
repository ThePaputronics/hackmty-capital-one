# Sponsor Tool Evaluation — Feasibility vs. Our Base Case

Companion to [`CAPITAL-ONE-NEEDS.md`](../use-cases/CAPITAL-ONE-NEEDS.md).
**Analysis only. Nothing has been implemented or installed.**

---

## 0. The filter we are applying

Every tool is scored against the base case from `CAPITAL-ONE-NEEDS.md`:

> **Constant data flow in → continuous, agentic, guarded output out.**

A tool earns a place **only** if it answers yes to all four:

1. **Does it serve the core loop?** (stream → process → agent → output → action)
2. **Is it simple?** Does it *remove* code rather than add glue?
3. **Does it avoid duplication?** No second database, no second memory layer, no second LLM gateway.
4. **Is it demo-safe?** Works offline-ish, degrades gracefully, no single point of demo failure.

Chasing prizes with unrelated SDKs is the fastest way to lose the main prize.
**Prize count is a tiebreaker, never a driver.**

---

## 1. Verdict at a glance

| Tool | Fit to base case | Verdict | Why |
| --- | --- | --- | --- |
| **Tiger Data** (Postgres + time-series) | ⭐ Direct | **CORE — adopt** | Literally the "constant data flow" storage layer. One DB for streams + relational. Plain SQL. |
| **Gemini API** | ⭐ Direct | **CORE — adopt** | The agent layer. Fast tier for low latency, function calling for actions, structured output for guardrails. |
| **Best Use of Gen AI** | ⭐ Direct | **FREE — auto-qualify** | Same Gemini integration satisfies this category. Zero extra work. |
| **Auth0** | ✅ Strong | **ADOPT — tier 2** | Fintech demo needs real auth; "Auth0 for AI Agents" maps 1:1 to agent consent/guardrails narrative. |
| **ElevenLabs** | ✅ Good | **ADOPT — tier 3 (polish)** | Proactive *voice* nudges = the Eno multi-channel story. High demo impact, ~1h of work, fully optional path. |
| **DigitalOcean** | 🟨 Neutral | **CONDITIONAL** | Fine hosting if we deploy. Pick **one** cloud only. |
| **Vultr** | 🟨 Neutral | **SKIP** | Redundant with DigitalOcean. Two clouds = zero extra value. |
| **Backboard** | 🟨 Overlap | **SKIP** | Duplicates state we already own in Postgres. Adds an external dependency to the critical path. |
| **Snowflake** | 🟨 Overlap | **SKIP (with regret)** | Second analytical DB. Contradicts Tiger Data. Tempting narrative — see §4. |
| **MongoDB Atlas** | 🟨 Overlap | **SKIP** | Second database. Our data is relational + time-series, which is exactly Postgres' home turf. |
| **Presage** | ⚠️ Off-axis | **SKIP** | Webcam vitals in a *banking* demo = privacy red flag + fragile hardware dependency. |
| **Solana** | ❌ Contradicts | **SKIP** | Crypto rails are off-strategy for Capital One and add a whole chain to maintain. |
| **.Tech domain** | ➕ Free | **ADOPT — 10 minutes** | Costs nothing, professionalizes the demo URL. |
| **GoDaddy Registry** | ➕ Free | **OPTIONAL** | Same slot as .Tech. Pick one registrar, not both. |

---

## 2. The recommended stack

```
 synthetic event generator  (Python/Node, configurable rate)
        │
        ▼
 ingest API  ──────────────────────────────────►  TIGER DATA
        │                                          • hypertable: transaction events
        │                                          • relational: users, accounts, subscriptions
        │                                          • continuous aggregates: rolling spend,
        │                                            utilization, runway, merchant baselines
        │                                          • compression for millions of events
        ▼
 rules / threshold detector  (SQL + small Python)   ← cheap, deterministic, fast, explainable
        │  emits candidate signals
        ▼
 AGENT LAYER  (GEMINI)
   understanding → planning → risk validation → explanation
        │   structured output (JSON schema) + function calling
        │   validation agent can BLOCK or DOWNGRADE an action
        ▼
 live dashboard + chat  (websocket/SSE, charts fed by continuous aggregates)
        │
        ├─► ELEVENLABS  — speaks the high-priority nudge aloud  (optional path)
        └─► human approve / override  →  simulated action + audit log

 AUTH0  wraps the app: login, and explicit consent before any agent action
 DIGITALOCEAN  hosts it   ·   .TECH  fronts it
```

**Deliberate design property:** every layer degrades independently.
Gemini down → rules engine still emits alerts. ElevenLabs down → text still renders.
Auth0 down → demo-user fallback. **No sponsor SDK can kill the demo.**

---

## 3. Why the core three

### 3.1 Tiger Data — the anchor

This is the single best match on the entire list. Our whole thesis is *continuous data
flow*, and Tiger Data is Postgres specialized for exactly that.

- **Continuous Aggregates** give us lag-free real-time charts *without* writing a
  separate stream processor — a large chunk of engineering we get to delete.
- **Unified stack**: user profiles + high-frequency transaction stream in one database.
  No sync job between a relational store and a metrics store.
- **Standard SQL**: everyone on the team can contribute; no obscure query language at 3am.
- **Compression**: millions of synthetic events on a free tier, so we can crank the
  generator during the demo without hitting disk limits.
- **Capital One alignment**: real-time feature store / unified data ecosystem, in miniature.

*Risk:* managed-instance latency from the venue network. *Mitigation:* local
Postgres+extension fallback with identical SQL, decided early — never mid-demo.

### 3.2 Gemini — the agent layer

- **Latency**: a fast/flash-tier model is what makes "real-time agentic" believable.
  A slow model turns our live demo into a loading spinner.
- **Structured output (JSON schema)**: the guardrail mechanism. The validation agent
  returns a typed verdict, not prose we have to regex.
- **Function calling**: how agents *take actions* instead of just talking — the exact
  Chat Concierge behavior Capital One is investing in.
- **Two prizes, one integration**: Best Use of Gemini API **and** Best Use of Gen AI.
- **Swappable**: if quota or the venue network fails us, the provider sits behind one
  interface and any Gen AI API can replace it. Build that seam on day one.

### 3.3 Auth0 — cheap credibility

Normally auth is hackathon overhead. Here it is thematic:

- A **financial** app with no auth looks unserious to judges from a **bank**.
- **Auth0 for AI Agents** lets us frame authorization as *agent governance*: the agent
  may only act within the scope the human granted. That is the responsible-AI story
  Capital One explicitly cares about, implemented rather than claimed.
- Drop-in SDK, generous free tier, ~1–2 hours.

**Guardrail on ourselves:** timebox it. If auth is not working in 2 hours, ship a demo
user and move on. It is tier 2 for a reason.

### 3.4 ElevenLabs — highest polish-per-hour

Capital One's Eno is explicitly **multi-channel** (app, text, email, notifications).
A proactive alert that *speaks*: "Heads up — your streaming subscription just went up
15%. Want me to cancel it?" is the single most memorable thing we can add for ~1 hour.

Strictly a **tier-3 additive path**: text first, audio layered on top, never a dependency.

---

## 4. Why we are skipping the rest

**Backboard** — genuinely useful in the general case, but our base case already stores
every event, feature, and decision in Tiger Data. Adding a second memory service means
two sources of truth for user state, and a network hop inside the critical loop. Our
"memory" is not chat history — it is a queryable financial event store. *Reconsider only
if we pivot to a chat-first product with no time-series backbone.*

**Snowflake** — the most tempting skip. Capital One really does operate on Snowflake
(their Slingshot product optimizes it), so the narrative is strong, and its REST LLM API
is a legitimate one-call integration. But running Snowflake *and* Tiger Data means two
analytical stores, two schemas, and a sync problem we will not finish. Choose one.
Tiger Data wins because continuous aggregates directly serve our live dashboard.

**MongoDB Atlas** — our domain is transactions, balances, and time-ordered events with
aggregations: relational + time-series. Postgres is the correct shape. Document storage
and vector search would only matter if we made heavy RAG central, which we should not.

**Vultr** — a second cloud adds a second deployment target and zero user value. If we
need GPU inference it becomes relevant; we are using hosted LLM APIs, so we do not.

**Presage** — "detect financial stress from the user's face" sounds clever and is a trap:
webcam permissions on a demo laptop, venue lighting, biometric/emotion inference inside a
**banking** product, and judges from a regulated financial institution who will immediately
think consent, bias, and compliance. High risk, off-thesis, cut it.

**Solana** — near-zero transaction cost and high throughput are real strengths, but
Capital One's stated priorities contain no blockchain component. Adding a chain means
wallets, keys, and RPC reliability in exchange for a prize and a weaker main pitch.

**GoDaddy Registry vs .Tech** — same slot. Register one domain, spend the remaining
time on the product.

---

## 5. Integration cost and risk

Estimates for planning only — to be re-checked against the real schedule.

| Tool | Est. effort | Risk if it fails | Blocks demo? |
| --- | --- | --- | --- |
| Tiger Data | 2–3 h | Fall back to local Postgres, same SQL | Yes — mitigate early |
| Gemini | 2–4 h | Rules engine still produces alerts | No |
| Auth0 | 1–2 h | Demo user fallback | No |
| ElevenLabs | ~1 h | Text-only output | No |
| DigitalOcean | 1–2 h | Run locally + tunnel | No |
| .Tech domain | ~10 min | Use the raw host URL | No |

**Sequencing rule:** the core loop (generator → Tiger Data → rules → visible output)
must be working *before* anyone touches a tier-2 or tier-3 tool. Each stage should be
independently demoable, so we always have something to show.

---

## 6. Scoreboard, honestly

The recommended stack plausibly qualifies for: **Tiger Data, Gemini API, Gen AI, Auth0,
ElevenLabs, .Tech**, plus **DigitalOcean** if we deploy there — from essentially **one
coherent architecture** where every piece earns its place in the product.

Compare with the alternative of bolting on Solana, Presage, MongoDB, and Backboard: more
categories entered, but a fragmented product, four extra failure modes, and a main pitch
that no longer holds together. We optimize for the Capital One challenge first.

---

## 7. Open questions

- `TODO: Verify` — **Prize windows vs. event date.** The pasted list carries validity
  ranges, and against today's date several appear to fall outside their stated window
  (Gemini `Q1 2025–Q1 2026`, Gen AI listed under the same Gemini window, Vultr `Q4 2025`,
  DigitalOcean `Q4 2025–Q1 2026`, Snowflake `Q3 2025–Q1 2026`, MongoDB `Q4 2024–Q4 2025`,
  GoDaddy `2025`), while Tiger Data, ElevenLabs, Auth0, Presage, Solana and `.Tech` appear
  current. **Confirm the official prize list for this specific event before relying on any
  category.** Note that the technical recommendation in §2 does **not** depend on this:
  Tiger Data and a Gen AI provider are the right choices regardless of prize eligibility,
  and the LLM provider is deliberately swappable.
- `TODO: Verify` — Backboard has **no validity window listed**; confirm whether it is
  offered at this event.
- `TODO: Verify` — whether the challenge mandates a specific Capital One API or sandbox
  dataset, which could override parts of the data layer.
- `TODO: Verify` — LLM API key availability, quota, and whether costs are covered.
- `TODO: Verify` — venue network reliability and outbound access to managed cloud
  services; this decides managed vs. local for Tiger Data.
- `TODO: Verify` — whether judging requires a public deployed URL (decides
  DigitalOcean vs. local + tunnel).
- `TODO: Verify` — team size and skills, to confirm the tier-2/tier-3 tools are
  realistic in parallel with the core loop.

---

## 8. Alternative project cases vs. this stack

The four alternatives from [`CAPITAL-ONE-NEEDS.md` §4.2](../use-cases/CAPITAL-ONE-NEEDS.md), scored
against the same stack.

| Case | C1 alignment | Demo impact | Scope risk | Data authenticity | Differentiation vs. shipped Eno | Stack reuse |
| --- | --- | --- | --- | --- | --- | --- |
| **A. FlowGuard** (wellness coach) | High | High | Medium | High (synthetic is expected) | Medium-High | 100% |
| **B. Fraud / anomaly co-pilot** | **Very high** | High | Medium | Medium (needs believable anomalies) | High | 100% |
| **C. Subscription optimizer** | Medium | Medium | **Low** | High | **Low** — closest to shipped | ~85% |
| **D. Credit / rewards optimizer** | Medium-High | Medium | Medium-High | **Low** — needs a card catalog | Medium | ~90% |
| **E. Journey observability** (internal) | High | **Low** | Medium | Medium | High | ~80% |
| **F. Hybrid A+B** | **Very high** | **Very high** | **High** | High | High | 100% |

### The strategically important finding

**The recommended stack is idea-agnostic.** Every case above is
*stream → time-series store → detection → agent reasoning → continuous output*.
Tiger Data, Gemini, Auth0, and ElevenLabs serve all six without modification.

Consequence: **we do not need to lock the idea before we start building.** The core loop
(generator → Tiger Data → rules → live UI) is shared by every case, so it can begin
immediately, and the product decision can be deferred until the agent layer — buying
several hours and removing the single biggest planning blocker.

### Per-case notes

**B. Fraud co-pilot — the strongest tool fit.** Tiger Data becomes *more* valuable
(rolling merchant baselines, z-scores, velocity windows are textbook time-series SQL).
Auth0 stops being decoration and becomes product: step-up authentication on a suspicious
action is exactly how real fraud UX works. ElevenLabs becomes thematic rather than
cosmetic — Capital One explicitly invests in fraud-call summarization for service agents.
*Risks:* crowded hackathon theme, and bank engineers will judge detection quality
harshly. Mitigate by competing on the **agentic investigation and explanation**, not on
beating anyone's anomaly model.

**C. Subscription optimizer — the safe floor.** Genuinely low risk and finishable, but the
detection is mostly periodicity rules, which shrinks the agent layer and weakens both the
"agentic AI" pitch and the Gen AI prize case. If chosen, restore agency with a
cancel-negotiation drafting agent and "what if I switch?" simulation. Best treated as a
**fallback**, not a first choice.

**D. Credit / rewards optimizer — data authenticity is the weak point.** Reward rules
require a card product catalog we would have to invent, which collides directly with the
repository rule against inventing APIs and requirements. Only viable if a real catalog or
sandbox is provided.

**E. Journey observability — right engineering, wrong room.** Excellent Tiger Data fit
(session/API traces are pure time-series) but no emotional hook. Choose only if judging
is heavily engineering-weighted — `TODO: Verify` the rubric.

**F. Hybrid — recommended, with a hard boundary.** Ship FlowGuard as the surface and make
fraud/anomaly *one agent inside it*. This captures both themes for roughly one extra
detector plus one extra agent prompt. The boundary: the fraud agent reuses the same
event stream, the same store, and the same output channel. The moment it needs its own
pipeline, cut it.

---

## 9. Alternative stacks (Plan B through E)

| Plan | Trigger | Substitution | Cost of switching |
| --- | --- | --- | --- |
| **A — recommended** | default | Tiger Data + Gemini + Auth0 + ElevenLabs + cloud + .Tech | — |
| **B — offline/venue network** | unreliable venue network | Local Postgres + time-series extension in Docker; minimal LLM calls with cached responses; pre-rendered audio; tunnel instead of deploy | Low if SQL is written portably from hour one |
| **C — no Tiger Data** | service unavailable or prize not offered | Plain Postgres with materialized views on a refresh interval, or DuckDB for local analytics | Medium — we write the aggregation layer ourselves and lose compression |
| **D — no LLM access** | quota, cost, or network failure | Rules-only detection with templated explanations; replay a cached agent transcript in the demo | High to the *pitch*, low to the *product* — outputs still flow |
| **E — Snowflake mandated** | challenge or judges require it | Snowflake as store + its REST LLM API | High — re-do the data layer; only if externally forced |

**The portability rule that makes B and C cheap:** write standard SQL, keep
vendor-specific features (continuous aggregates, compression) behind a thin module, and
put every LLM call behind one interface. Roughly an hour of discipline on day one that
converts three potential demo-day disasters into config changes.

---

## 10. Alternative solutions for the streaming layer

This is where over-engineering is most likely, so it deserves an explicit decision.

| Option | Authenticity to C1 | Ops cost | Verdict |
| --- | --- | --- | --- |
| **Kafka / Redpanda** | Highest — matches their real architecture | **High** — brokers, topics, consumer groups, a container that can die mid-demo | **Avoid** unless required |
| **Redis Streams** | Good — real log semantics, consumer groups | Medium — one extra container | **Upgrade path** if we need multiple independent consumers |
| **Postgres table + `LISTEN/NOTIFY`** | Adequate — real push semantics | **Near zero** — no new dependency | **Recommended start** |
| **In-process async queue** | Weakest — hard to show as a pipeline | Zero | Prototype only |

**Recommendation:** start with the Postgres-native path. It gives a genuine
producer → durable log → push-notified consumer loop with **one** piece of
infrastructure, and it keeps the "stream is visible" demo requirement fully intact.
Present the Kafka/Kinesis mapping in the architecture slide rather than paying its
operational cost during a hackathon.

Guard against the opposite failure too: judges must *see* the flow. Whatever the
substrate, the UI needs a live event ticker, per-stage latency, and a throughput dial.

---

## 11. Alternative solutions for the agent layer

| Option | Verdict |
| --- | --- |
| **Plain function calls + structured output**, one module per agent role | **Recommended.** Debuggable at 3am, no framework surprises, and the role separation is explicit in the code we show judges. |
| **LangGraph / CrewAI / AutoGen** | **Avoid.** Framework debugging under time pressure is a known hackathon killer, and it hides the agent collaboration we specifically want to demonstrate. |
| **Single mega-prompt** | **Avoid.** Collapses exactly the multi-agent story the challenge rewards, and makes guardrails unverifiable. |
| **Local/open-weight model** | Fallback only. Aligns with Capital One's customized open-weight approach, but venue hardware and latency make it a demo risk. |

The validation agent must be able to **block** an action, and that block must be visible
on screen at least once during the demo. It is the cheapest possible proof of guardrails.

---

## 12. Alternative frontend and transport choices

| Decision | Options | Recommendation |
| --- | --- | --- |
| Live updates | Polling / **SSE** / WebSocket | **SSE** — one-way server push is exactly our shape, and it is far less code than WebSocket |
| UI framework | Streamlit / Next.js / React+Vite | Fastest path the *team* already knows. Streamlit is quickest for charts but weak for a polished chat + action-approval surface — `TODO: Verify` team skills |
| Deployment | App Platform / Droplet + Docker Compose / local + tunnel | Droplet + Compose if we need control; App Platform if we want speed; keep a tunnel ready as the emergency path |

---

## 13. Reconsideration triggers for skipped tools

Each rejection has a specific condition that would reverse it. Nothing is rejected on
principle.

| Tool | Reverse the decision if… |
| --- | --- |
| **Backboard** | We pivot to chat-first with long-lived cross-session memory as the *core* feature, rather than a time-series backbone |
| **Snowflake** | The challenge mandates it, or we drop Tiger Data entirely (never both) |
| **MongoDB** | The dataset turns out to be document-shaped or unstructured-heavy, or RAG becomes central |
| **Vultr** | We need GPU inference for a self-hosted model |
| **Presage** | Never for a banking surface. Only if the challenge explicitly asks for wellbeing/biometric sensing, with consent handled |
| **Solana** | The challenge adds a payments-rail or settlement requirement |

---

## 14. Failure-mode contingency matrix

| What breaks | What we still show |
| --- | --- |
| Managed database unreachable | Local Postgres, identical SQL, same dashboard |
| LLM quota exhausted | Rules-based alerts plus a cached agent transcript |
| Auth0 misbehaving | Demo user, auth described in the slide |
| ElevenLabs down | Text nudges only |
| Venue internet down | Fully local stack behind a tunnel, or laptop-only demo |
| Deployment fails | Localhost demo — decided **before** the presentation, never during |

The requirement behind this table: **at every point after the first few hours, there must
exist something demoable.** Build the core loop end-to-end early and thin, then deepen.

---

## 15. Decision requested

- **Stack:** Tiger Data + Gemini + Auth0 + ElevenLabs + one cloud + .Tech, built in that
  priority order, with everything after Gemini strictly optional.
- **Case:** default to **F (FlowGuard with a fraud agent inside)**, with **B** as the
  pivot if we want the stronger engineering story and **C** as the safety net if time or
  team size is tighter than expected.
- **Streaming substrate:** Postgres-native to start; upgrade only if a real need appears.
- **Deferral:** because the stack is idea-agnostic, the final case can be decided after
  the core loop is running rather than before.

*Status: analysis only. No code, dependencies, accounts, or infrastructure changes made.*
