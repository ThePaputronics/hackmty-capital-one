# Capital One — Needs, Context, and Working Hypothesis (HackMTY)

Source of this synthesis: [`CAPITAL-ONE-RAW.md`](CAPITAL-ONE-RAW.md).
This document is **analysis and planning only**. No implementation has started.

> **Status: raw draft, superseded in part.** This was written before the
> sponsor's canonical challenge statement was available, so its reconstruction
> of what Capital One wants is inference, not requirements. The canonical three
> tracks — and the rule that a submission may target one track or blend two or
> three — live in
> [`docs/ai/knowledge/challenge-brief.md`](docs/ai/knowledge/challenge-brief.md),
> which wins wherever the two disagree. Kept for its background research and for
> the reasoning behind the selected direction.

---

## 1. One-line framing

> Capital One wants **constant data flow in → continuous intelligent output out**:
> streaming transaction/behavioral data processed in near real time by **agentic AI
> with guardrails**, producing **alerts, insights, recommendations, and autonomous
> actions** that move cognitive burden off the customer.

The hackathon prompt — *"smart financial tools using constant data flow and output"* —
is a near-direct restatement of that strategy. Anything we build should make the
**stream visible** and the **output continuous**. A request/response CRUD app, no
matter how polished, misses the theme.

---

## 2. What Capital One actually cares about

### 2.1 Engineering-side priorities

| Priority | What it means concretely | Implication for our build |
| --- | --- | --- |
| **Real-time / streaming decisioning** | Kafka/Kinesis-style event architectures, feature hubs, low-latency fraud/risk/personalization scoring, continuous learning after deploy | Need an actual event pipeline, not a batch job on a button click. Latency should be measurable and shown. |
| **Agentic / multi-agent AI** | Pipelines of specialized agents: understanding → reasoning/planning → validation → explanation. Customer-facing agents that *act* (Chat Concierge), not just answer | Our agents should be visibly distinct roles, with the handoff shown in the demo. |
| **Guardrails, governance, evaluation** | Customized open-weight models, strong guardrails, responsible AI, evaluation harnesses | A validation/risk agent that can **block or downgrade** an action is a differentiator, not overhead. |
| **Developer experience / platform eng** | Standardization, automation of undifferentiated work, serverless defaults, observability | Clean repo, reproducible run, and observability of our own pipeline score points. |
| **Data as a product** | Conversational + real-time-ready data, unstructured data, tokenization / privacy-preserving techniques | Never use real PII. Synthetic/mock data, tokenized identifiers, explicit privacy story. |
| **Cloud-native / serverless-first** | Fully public cloud, AWS-leaning, Python/Go | If cloud is infeasible in the time box, mirror the *architecture* (queue + stateless consumers) and state the cloud mapping explicitly. |

### 2.2 Customer-side pain points

- Too much cognitive load: users must dig through statements to understand their own money.
- Reactive, not proactive: they learn about a problem after it costs them.
- Fragmented channels: app, text, email, browser, notifications.
- Under-served segments: students, travelers, small businesses.
- Wants: proactive coaching (spending, debt payoff, savings goals, rewards),
  real-time protection (fraud, subscription price hikes, unusual patterns),
  and assistants that **take action on their behalf**.

Existing baseline to beat / extend: **Eno** — real-time transaction alerts,
subscription tracking and price-hike detection, virtual card numbers, fraud
protection, balance/payment help, spending insights.

> **Design consequence:** "another chatbot that answers questions about your balance"
> is already shipped. Our edge must be **proactive + agentic + real-time**: the system
> speaks first, reasons, and proposes or executes a concrete action.

---

## 3. What a winning PoC looks like

Derived from the brief's judging signals:

1. **Visible data flow** — live stream → processing → outputs updating on screen, no refresh.
2. **Explicit agent collaboration** — show which agent did what, and show a guardrail firing.
3. **Measurable impact** — "saves $X/month", "detected in <5s", "avoided N overdrafts".
4. **Tight scope** — mock data + core pipeline + one polished surface (dashboard or chat).
5. **Responsible AI** — explanations, human override, confidence, refusal paths.
6. **Cloud-native framing** — serverless/streaming vocabulary, even if locally simulated.

Anti-patterns to avoid: static CSV upload; "AI" that is one LLM call; a dashboard with
no stream behind it; demo that requires the judge to imagine the real-time part;
a fully autonomous money-mover with no human override (governance red flag).

---

## 4. Candidate directions

> **Resolved 2026-09-11:** the owner selected the hybrid in §4.2 — wellness
> coach as the product surface with anomaly/fraud detection as an agent
> inside it. See [`docs/ai/knowledge/challenge-brief.md`](docs/ai/knowledge/challenge-brief.md),
> which is authoritative for the direction and for the sponsor's official
> track statements. The analysis below is kept as the reasoning behind that
> choice.

### 4.1 Primary recommendation — Real-time Agentic Financial Wellness Coach ("FlowGuard")

- **Input stream:** synthetic transactions, balances, recurring charges, credit
  utilization; optional context signals (academic calendar for students, payroll dates).
- **Processing:** event queue → lightweight rules/ML scoring → multi-agent layer
  (intent/understanding → planning → risk validation → natural-language explanation).
- **Continuous outputs:**
  - proactive nudges — "this subscription just rose 15%, cancel?"
  - dynamic **runway forecast** — "shortfall in 12 days unless X"
  - debt-payoff simulations gated by a risk check
  - rewards optimization suggestions
  - virtual-card recommendation for a risky merchant
- **Why it fits:** hits "constant data flow and output" literally, showcases agentic AI,
  obvious human value (reduces financial anxiety), demos live, and has a natural home
  for guardrails and human override.

### 4.2 Alternatives

Scored against the sponsor-tool stack in
[`FEASIBLE-TOOLS.md` §8](FEASIBLE-TOOLS.md).

| # | Idea | Strength | Risk |
| --- | --- | --- | --- |
| 1 | **Streaming Fraud / Anomaly Co-pilot** — real-time anomaly scoring + multi-agent investigation (explain alert, suggest lock/dispute, surface related patterns) | Strongest pure-engineering demo; core bank need | Crowded theme; needs convincing anomaly data |
| 2 | **Proactive Subscription & Recurring Spend Optimizer** — detect subscriptions + price changes, one-click cancel, "what if I switch?" projections | Simple, practical, easy to finish | Closest to shipped Eno features — must add real delta |
| 3 | **Real-time Credit / Rewards Optimizer** — dynamic card routing, limit suggestions, reward maximization with risk checks | Clear $ impact metric | Rewards logic can get fiddly; needs card-product data |
| 4 | **Customer Journey Observability Tool** — reconstruct real-time customer paths from session/API events, surface friction | Differentiated, internal-facing, matches their observability work | Less emotionally compelling to judges; harder to demo value |

**Hybrid worth considering — selected.** Wellness coach as the product surface, with
fraud/anomaly detection as one agent inside it. Gets both themes without doubling the
scope. This is the direction of record; see §4's note.

---

## 5. Architecture sketch (to be validated before building)

```
 synthetic event generator            ── "constant data flow"
        │  (transactions, balances, recurring charges, signals)
        ▼
 event bus / stream  (Kafka|Kinesis|Redis Streams|in-proc queue)
        │
        ▼
 stream processor: enrichment + feature state + rules/ML scoring
        │
        ▼
 AGENT LAYER
   understanding ─► planning ─► risk & policy validation ─► explanation
                                   │ (can block / downgrade)
        ▼
 output channel: live dashboard + chat + action proposals
        │
        ▼
 human override / approve → (simulated) action execution + audit log
```

Cross-cutting: latency metrics per stage, audit trail of every agent decision,
confidence + reasoning attached to each output, kill switch.

---

## 6. Repository context

This repo currently contains **no product code** — it is a shared Codex/agent
engineering environment:

- `AGENTS.md` — repository working agreement (source of truth); English-only output;
  small reversible changes; no invented APIs or test results; `TODO: Verify` for
  unverifiable claims.
- `CLAUDE.md` — maps the same agreement onto Claude Code.
- `.codex/config.toml`, `.codex/agents/` — 25 specialist roles coordinated by `miku`.
- `.agents/skills/` — 11 reusable workflows.
- `docs/ai/knowledge/` — shared contracts, strategies, infrastructure and
  knowledge-sync rules.
- `scripts/validate-ai-config.py`, `scripts/evaluate-agent-strategy.py` — validators.

**Notable constraint:** the only authorized remote filesystem scope is `/srv/hackathon`.
Deployment planning must read `docs/ai/knowledge/infrastructure.md` first.

**Useful coincidence:** the repo's own multi-agent orchestration setup mirrors the
multi-agent product we would build — we can build the product *with* the agent catalog
and mention that in the pitch.

---

## 7. Open questions — must be answered before implementation

All of the following are unknown from the available material and must not be assumed:

- ~~Official Capital One challenge statement~~ — **resolved**: the three canonical
  sponsor tracks are recorded verbatim in
  [`docs/ai/knowledge/challenge-brief.md`](docs/ai/knowledge/challenge-brief.md),
  which also records that a submission may target one track or blend two or three.
  `TODO: Verify` — exact hackathon rules and published judging rubric / weights
  remain unknown.
- `TODO: Verify` — submission deadline and demo format (live demo? video? pitch length?).
- `TODO: Verify` — team size, member skill sets, and who owns which layer.
- `TODO: Verify` — required or provided APIs (e.g., a Capital One / Nessie-style
  sandbox API), and whether external LLM API keys are permitted and funded. The
  owner holds one sponsor-issued API key locally; its scope and quota are not yet
  confirmed. The key itself must stay out of the repository.
- `TODO: Verify` — tech stack preference (Python vs Go vs TypeScript) and whether
  AWS credits / cloud accounts are available, or everything must run locally.
- `TODO: Verify` — internet reliability at the venue (decides local model vs hosted API).
- `TODO: Verify` — whether real data is provided, or we generate synthetic data.
- `TODO: Verify` — IP / open-source requirements for submitted code.

---

## 8. Proposed next steps (awaiting "Go On")

1. ~~Lock the idea~~ — **done 2026-09-11**: hybrid per §4.2.
2. Resolve the open questions in §7, especially rubric, stack, and API availability.
3. Define the demo narrative first — the 3-minute story judges will see — then build
   backwards from it.
4. Slice scope into: event generator → stream + state → agent layer → UI → polish,
   each independently demoable so we always have something to show.
5. Decide the impact metric we will put on screen.

---

*Status: analysis only. No code, dependencies, or infrastructure changes made.*
