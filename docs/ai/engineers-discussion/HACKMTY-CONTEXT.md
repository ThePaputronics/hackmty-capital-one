# HackMTY Capital One — Consolidated Product Context

**Purpose:** Single planning context for the hackathon deliverable. This file condenses the prior planning sessions, research conclusions, scope decisions, legal concerns, alternative directions, and implementation constraints.

**Status:** Product-discovery context only. No product implementation is specified by this file.

**Context date:** September 12, 2026.

## 1. Decision Status and Source of Truth

There are two decisions at different levels and they must not be conflated:

- **Authoritative repository direction:** The repository challenge brief records a hybrid of Track 1 and Track 3: a consumer financial-wellness surface with real-time anomaly and fraud detection as a first-class agent inside the same pipeline. See [`docs/ai/knowledge/challenge-brief.md`](docs/ai/knowledge/challenge-brief.md).
- **Latest product-discovery recommendation:** The Mexico opportunity research recommends narrowing the first deliverable to a pre-submission **SPEI Intent Guard** for authorized-push-payment scams and coercion. This is a more specific product wedge, not yet an explicit replacement of the repository's recorded hybrid decision. See [`MEXICO-OPPORTUNITY-MAP.md`](MEXICO-OPPORTUNITY-MAP.md).

Until the owner confirms otherwise, implementation planning should treat the SPEI Intent Guard as the leading product wedge while preserving the hybrid's Track 1 plus Track 3 framing. The wellness experience can remain the user-facing shell, but the MVP should have one sharp intervention rather than several unrelated financial-coaching features.

Older exploratory documents contain useful reasoning but are subordinate to the canonical challenge brief and this status clarification:

- [`CAPITAL-ONE-NEEDS.md`](CAPITAL-ONE-NEEDS.md) contains the original FlowGuard/hybrid reasoning.
- [`FEASIBLE-TOOLS.md`](FEASIBLE-TOOLS.md) evaluates sponsor tools and alternatives.
- [`MEXICO-OPPORTUNITY-MAP.md`](MEXICO-OPPORTUNITY-MAP.md) contains the detailed Mexico research and ranked opportunities.
- [`CAPITAL-ONE-RAW.md`](CAPITAL-ONE-RAW.md) contains the initial sponsor-priority interpretation.

## 2. Challenge Tracks

The sponsor provides three tracks. A submission may target one track or deliberately blend two or three.

### Track 1 — Consumer Financial Autonomy & Credit Building

Develop intelligent agents that transform raw transaction streams into active financial well-being, such as automating micro-savings, identifying subscription leaks, or establishing cash-flow-based credit scoring for thin-file consumers.

### Track 2 — SMB Cash-Flow & Working Capital Intelligence

Build predictive treasury engines for small businesses that aggregate revenue and operating-expense streams to forecast 30-day liquidity, manage overhead, and recommend timely working-capital buffers.

### Track 3 — Real-Time Anomaly & Security Sentinel

Design behavioral anomaly-detection engines that analyze transaction ledgers in real time to flag unexpected transfer velocity, suspicious merchant-category changes, and abnormal account behavior.

### Sponsor-aligned design principles

The product should make the following visible:

1. Continuous transaction or behavioral events entering the system.
2. Low-latency enrichment, scoring, and state updates.
3. Specialized agent roles rather than one opaque LLM call.
4. A guarded, explainable output that helps the user take a bounded action.
5. Measurable impact, latency, false-positive behavior, and a clear failure path.
6. Cloud-ready architecture that can scale toward the owner-stated target of approximately 100 million users without requiring a rewrite.

The product does not need to be a Capital One-specific deployment. It may address Mexican consumers, independent workers, PYMES, financial institutions, wallets, remittance providers, or other participants in Mexico's financial ecosystem, provided it fits a challenge track.

## 3. Recommended Product Wedge

### SPEI Intent Guard

A pre-submission guard for a customer who is about to send an unusual SPEI transfer to a first-time or newly risky beneficiary while being manipulated by a scammer.

The system does not ask only, "Is this really the customer?" Authentication may succeed because the real customer is present and is pressing confirm. It asks a second question:

> **Is the authenticated customer being manipulated right now?**

The product observes the payer's own recent actions and transaction context, combines independent signals, explains the pattern in plain language, and offers reversible friction before the transfer is submitted. It does not declare the beneficiary a criminal or attempt to reverse money after settlement.

### Why this niche is stronger than a generic fraud detector

- It addresses a precise intervention moment: the last seconds before submission.
- It distinguishes authorized-push-payment/coercion from account takeover.
- It makes the data stream, decision, explanation, and guardrail visible in a short demo.
- It can be demonstrated with synthetic data without pretending to have production fraud labels.
- It is narrower and more defensible than a general-purpose financial coach.
- It aligns with the Real-Time Anomaly & Security Sentinel track while preserving a consumer financial-wellness experience.

### Core product thesis

> Combining the payer's own behavioral anomalies with transaction context can trigger a specific, reversible warning before SPEI submission, while allowing unusual legitimate payments to proceed.

### Target user

A Mexican bank or wallet customer preparing to authenticate an unusual SPEI transfer to a new or recently changed beneficiary.

### Primary problem statement

A customer can be fully authenticated yet still be manipulated into sending an irreversible transfer. Existing identity controls answer who is acting, but not whether the customer understands and intends the transfer at that moment.

### What the product should say

> "Detectamos una combinación poco habitual: aumentaste tu límite recientemente, este destinatario fue registrado hace poco y el monto supera tu comportamiento normal. Verifica la operación antes de continuar."

It should never say:

> "Este beneficiario es un estafador."

## 4. Product Scope

### MVP in scope

- Synthetic SPEI event stream.
- Payer/account baseline built from the payer's own history.
- Beneficiary creation and modification events.
- Transfer amount, balance share, velocity, frequency, and accumulation features.
- MTU or transfer-limit changes and timing relative to the transfer.
- Session and device context as secondary signals.
- Transparent rules plus a small interpretable anomaly model.
- Separate conceptual scores for account takeover context, payer intent, and recipient-network context.
- A policy/validation agent that can downgrade or block a proposed automated action.
- An explanation agent that produces structured, plain-language reasons in Spanish.
- A reversible pause, cancel option, verified-bank callback simulation, or deliberate continue action.
- Live event ticker, signal timeline, decision latency, and audit trail.
- Synthetic legitimate unusual transfers to demonstrate that the system does not block everything.
- Synthetic coerced transfers to demonstrate targeted friction before submission.
- Rules-only fallback if the LLM provider is unavailable.

### Explicitly out of scope

- Real movement of money.
- Automatic account freezing, permanent blocking, or irreversible rejection.
- Automatic reversal or recovery after SPEI settlement.
- A private blacklist or permanent reputation score for a person, CLABE, CURP, RFC, or beneficiary.
- Scraping CONDUSEF reports or treating complaints as confirmed fraud evidence.
- A public or cross-bank scammer registry.
- Capturing call audio, messages, contacts, clipboard contents, screenshots, or private communications.
- Using age, gender, ethnicity, nationality, neighborhood, disability, income level, or other protected/proxy attributes as fraud signals.
- A full fraud-investigation case-management product.
- A second dashboard that competes with the primary customer flow.
- A general budgeting coach, rewards optimizer, subscription manager, and credit-underwriting product all at once.
- Any action requiring an IFPE, banking, lending, money-transmission, or other regulated license.

### Automation boundary

The system can operate automatically during the transfer flow:

1. Observe events.
2. Compute features and combine signals.
3. Decide whether to show no friction, a warning, or a reversible pause.
4. Explain the decision.
5. Record a minimal technical audit event.

It does not need a human investigator in real time. Human investigation is an optional downstream institutional workflow for selected cases, not a required step for the customer-facing MVP. The system should decide whether to pause a transaction, not who is guilty.

## 5. Main Anomaly Signals

No single signal should label a transaction as fraud. A practical rule is: one signal informs, two correlated signals create attention, and three independent reinforcing signals may activate reversible friction.

### High-priority MVP signals

- Recent transfer-limit/MTU increase.
- New beneficiary created shortly before the transfer.
- First transfer to that beneficiary.
- Amount materially above the payer's personal baseline or recent maximum.
- Amount close to the configured limit.
- Repeated transfers just below the limit.
- Multiple transfers to the same beneficiary within a short interval.
- Short time between beneficiary creation, limit change, and transfer submission.
- Accumulated transfer amount that is unusual even when individual transfers are below the limit.
- Transfer that leaves the payer with an unusually low balance.

### Secondary context signals

- New device, browser, session, or network.
- Recent password, phone, email, SIM, or authentication-factor change.
- Unusual location, VPN/proxy, or channel change.
- Unusual hour or activity cadence.
- Rapid navigation between security settings, beneficiary management, and confirmation.
- Repeated cancellation, retry, or duplication of the same transfer.
- Several new beneficiaries created in one session.
- Destination data changed shortly before submission.

These are context, not proof. A device replacement, a night transfer, or one large payment can be legitimate.

### Signals for future institutional research, not MVP decisions

- Recipient fan-in and fan-out across accounts.
- Rapid cash-out or onward transfer after receiving funds.
- Device, phone, or funding-source relationships across multiple accounts.
- Cross-institution patterns.
- Confirmed fraud intelligence shared through lawful institutional arrangements.

These signals can be useful to a bank's investigation or welfare workflow, but they should not create a durable accusation. A high fan-in account may be a legitimate merchant, worker, or organization, or an unwitting mule victim.

### Signals deliberately excluded

- Unadjudicated CONDUSEF complaints.
- Number of reports against a person or CLABE.
- Names, locations, or institutions as proof of fraud.
- Age or vulnerability of a beneficiary as evidence of guilt.
- A single large transfer, single new device, or single nighttime event.
- A reputation score that can be poisoned by coordinated reports.

## 6. Abuse, Privacy, and Legal Safety

The central design correction from the sessions is:

> **Score the transaction and warn the payer; do not label the person.**

### Why reputation and complaint signals were removed

A report is cheap to manufacture. Ten coordinated people could submit reports against a legitimate business or account. Per-reporter rate limits do not solve a coordinated Sybil attack. A transaction-linked signal is harder to manufacture, but building a reputation system would still be a separate product with institutional data, appeals, governance, and legal responsibilities.

The MVP therefore does not scrape CONDUSEF or build a recipient-reputation database. The core thesis needs none of it: the strongest signals are observed actions by the payer on the system's own event stream.

### Key legal and operational risks

- **Personal-data profiling:** A tokenized identifier can still be personal data if it can be re-linked to a person.
- **Financial and patrimonial data:** Amounts, account relationships, beneficiaries, sessions, and transaction patterns require strict purpose limitation, lawful processing, access control, and retention discipline.
- **Banking confidentiality:** SPEI and bank-operation information cannot be casually aggregated across institutions or exposed to a third-party registry.
- **Automated decisions:** An automatic hold or rejection can materially affect access to money and create consumer-protection, transparency, and appeal concerns.
- **False positives:** Legitimate merchants, family transfers, emergencies, older users, rural users, and device replacements may look anomalous.
- **Security breach:** Transaction patterns and identifiers are high-value targets.
- **Regulatory perimeter:** Moving money, operating accounts, underwriting credit, sharing financial data, or providing regulated services may require a licensed or institutionally sponsored deployment.
- **Unsupported legal certainty:** The hackathon prototype must not present itself as legal advice or claim production compliance.

### MVP safeguards

- Use only synthetic data.
- Keep the output temporary and transaction-scoped.
- Use opaque/tokenized identifiers with no real-world identity data.
- Show reason codes and uncertainty.
- Use short retention and expiration/decay for technical events.
- Provide cancel, continue, and human-controlled override paths.
- Never claim the recipient is fraudulent.
- Test false-positive and challenge rates across synthetic user segments.
- Do not send raw personal documents or identifiers to an LLM.
- Keep credentials and API keys outside the repository.
- Treat all legal claims as `TODO: Verify` until reviewed for the actual deployment model.

### Relevant legal references to verify before production

- Mexico's private-sector data-protection law, including purpose, consent, transparency, security, and ARCO rights.
- Ley de Instituciones de Crédito, including confidentiality of banking operations.
- Ley para Regular las Instituciones de Tecnología Financiera, including transactional-data sharing and confidentiality requirements.
- Banco de México rules governing SPEI operations and participant responsibilities.

The prototype should be presented as a technology demonstration for a regulated institution, not as an independent service already authorized to delay or inspect bank transfers.

## 7. Demo Narrative

The demo should be a visible stream-to-decision story, ideally in three short beats:

1. **Legitimate unusual transfer:** A large transfer to a new beneficiary occurs, but the combined evidence is insufficient. It proceeds. This proves the product is not a wall.
2. **Manipulation sequence:** A simulated scam call or coaching context is represented by synthetic event labels, not recorded audio. The customer creates a beneficiary, raises the limit, and prepares an atypical transfer.
3. **Last-second guard:** The live stream shows beneficiary age zero, recent limit change, personal-baseline deviation, and rapid sequence timing. The system pauses the proposed submission, explains the pattern in Spanish, and offers cancel, verified callback, or deliberate continue.

Show the same or equivalent event stream with detection disabled or with the guard bypassed as a contrast only if time allows. Do not imply the system can recover settled funds; the value is the intervention before submission.

### Demo metrics

- Value-weighted recall of injected coercion/APP scenarios before submission.
- Genuine-payment challenge rate at the same threshold.
- Median and p95 decision latency.
- Time from event ingestion to visible explanation.
- Number of legitimate unusual transfers allowed through.
- Zero automatic blocks or irreversible actions.
- Synthetic subgroup false-positive rates and challenge-rate ceiling.

Production fraud prevalence, recovered pesos, and nationwide APP performance must not be claimed from synthetic data.

## 8. Architecture Direction (Post-MVP)

> **Status: deferred.** The canonical architecture for the hackathon build is
> the synchronous request-scoped path recorded in
> [`docs/architechture/ADR-0001-canonical-mvp-architecture.md`](../../architechture/ADR-0001-canonical-mvp-architecture.md).
> The event stream, the agent layer, and the SSE dashboard described in this
> section are the direction *after* that path works end to end. Do not build
> them first.

### Simple logical flow

```text
Synthetic event generator
        |
        v
Durable event intake / stream abstraction
        |
        v
Feature state + personal baseline + deterministic rules
        |
        v
Candidate anomaly event
        |
        v
Agent layer: understand -> validate policy -> explain
        |
        v
Customer confirmation UI: no friction / warning / reversible pause
        |
        v
Audit event and simulated action
```

The anomaly agent and any wellness agent must read the same enriched event stream. Do not create two independent products with separate pipelines.

### Architecture properties

- Start with the simplest durable stream that makes the flow visible.
- Prefer a Postgres-native event table plus `LISTEN/NOTIFY` or an equivalent queue boundary for the first prototype.
- Keep the stream interface replaceable by Redis Streams, Kafka/Kinesis, SQS/SNS, or EventBridge later.
- Keep services stateless and store persistent state in the database/cache layer.
- Use standard SQL where possible; isolate vendor-specific time-series features.
- Use environment variables for credentials, hosts, ports, and feature flags.
- Use containers as the deployment unit.
- Add health/readiness checks, graceful shutdown, and structured stdout/stderr logs.
- Avoid premature microservices and multi-region complexity.
- Use SSE for one-way live dashboard updates unless the chosen frontend already has a strong WebSocket pattern.

### Agent design

Use plain function calls with structured JSON output and one module per role:

- **Understanding/feature agent:** summarizes the event and available evidence.
- **Risk/policy validation agent:** checks whether a proposed action is permitted and can downgrade or block it.
- **Explanation agent:** converts validated reason codes into concise Spanish user messaging.
- **Optional action agent:** prepares a simulated callback, pause, or audit action; execution requires user approval.

Avoid a single mega-prompt. Avoid LangGraph, CrewAI, or AutoGen unless the team already has strong experience and the framework demonstrably removes work.

## 9. Sponsor Tools and Recommended Combination

The rule is simple: a tool earns a place only if it serves the stream-to-output loop, removes code, avoids duplication, and degrades safely during the demo.

### Recommended priority order

1. **Tiger Data:** Core time-series/relational store for event streams, baselines, and live aggregates. Use standard SQL and keep a local Postgres fallback.
2. **Gemini or another approved GenAI provider:** Agent explanation and structured validation layer. Keep the provider behind one interface and do not make the demo dependent on it.
3. **Auth0:** Optional second tier for real authentication and agent-consent framing. Timebox it; a demo-user fallback is acceptable.
4. **ElevenLabs:** Optional polish for a spoken high-priority nudge. Text is primary; audio must never block the demo.
5. **One hosting provider:** DigitalOcean or Vultr, selected by team familiarity, required GPU, and deployment simplicity. Do not deploy to two clouds.
6. **One domain:** `.Tech` or GoDaddy Registry, not both.

### Tool decisions and conditions

| Tool | Position | Reason / reversal condition |
|---|---|---|
| Tiger Data | Core candidate | Direct fit for high-frequency financial events and time-series aggregates. Replace with plain Postgres if unavailable. |
| Gemini | Core candidate | Good fit for structured, low-latency explanation and agentic function calls. Provider must remain swappable. |
| Auth0 | Optional tier 2 | Adds credible auth and consent. Skip if it delays the core loop. |
| ElevenLabs | Optional tier 3 | Memorable voice output, but text must work without it. |
| Snowflake | Conditional | Strong analytics and legitimate REST/LLM API story, but do not run it alongside Tiger Data unless required. Use it only if mandated or if Tiger Data is dropped. |
| Backboard | Conditional | Useful for chat-first persistent memory, RAG, embeddings, and model routing. It overlaps with a time-series event store and adds a critical external hop, so use only if long-term conversational memory becomes the core feature. |
| Vultr | Conditional | Good if GPU/self-hosted inference or existing team familiarity matters. Otherwise it is redundant with one simpler cloud deployment. |
| DigitalOcean | Conditional | Good for simple hosting and managed deployment. Pick it or Vultr, not both. |
| MongoDB Atlas | Skip by default | A second database is unnecessary for relational/time-series ledger data. Reconsider if the domain becomes document/RAG-heavy. |
| Presage | Skip | Biometric/emotion sensing is privacy-sensitive, fragile in a banking demo, and off-thesis. Reconsider only for an explicitly approved wellbeing/biometric track. |
| Solana | Skip | Adds blockchain rails, wallets, keys, and RPC failure modes without strengthening the selected product. Reconsider only if the challenge requires a crypto/payment rail. |
| `.Tech` / GoDaddy | Choose one | Domain prize is low-cost polish; do not spend product time on two registrars. |

### Important prize caveat

The pasted MLH list contains prize windows that may not match the current event date. Confirm the official event-specific eligibility before using a sponsor tool for prize strategy. Technical fit should decide the architecture; prize eligibility is a secondary benefit.

## 10. Alternatives and Fallbacks

### Alternative product directions

| Direction | Track | Assessment | Role |
|---|---|---|---|
| Quincena Collision Guard | Track 1 | Forecast minimum safe balance through the next paydays and prevent timing collisions. Strong household evidence, safe MVP, less novel. | Best consumer backup. |
| Cobro-30 | Track 2 | Match CFDIs/payment complements to deposits and forecast 30-day receivables-to-runway. Strong Mexico-specific data advantage, more integration work. | Best B2B backup. |
| Volatility-aware emergency buffer | Track 1 | Estimate a conservative safe-to-save amount for informal/gig workers. High feasibility, but cash visibility and action safety are difficult. | Secondary consumer option. |
| RemesaGuard Sur | Track 3 | Detect unusual remittance-to-cash-out behavior with accessible/offline UX. Differentiated, but narrower evidence and high fairness sensitivity. | Specialized security option. |
| Dimo rebinding guard | Track 3 | Protect the first transfer after phone/account relinking. Clear state machine and Mexico-specific rail, but fraud prevalence is unknown. | Focused technical backup. |
| IVA Guard | Track 2 | Separate collected cash from booked revenue and reserve for taxes. Useful module, not the initial product wedge. | Later module for Cobro-30. |
| Net-pay deduction integrity | Track 1/3 | Reconcile payroll documents, deposits, and deductions. Safe and explainable, but not the strongest real-time story. | Research alternative. |
| Cash-flow evidence passport | Track 1 | Produce explainable transaction evidence for thin-file applicants. High regulatory/fairness risk and not suitable for automated denial. | Do not prioritize for MVP. |
| ReconcileMX | Track 2/3 | Reconcile POS, wallet, SPEI/CoDi, cash, refunds, and deposits. Feasible with CSVs, but provider coverage is unverified. | Possible B2B fallback. |
| Subscription optimizer | Track 1 | Easy to build but close to existing Eno-like functionality and less agentic. | Safety-net only. |
| Credit/rewards optimizer | Track 1 | Needs a real product catalog and reward rules. Do not invent them. | Use only if an official catalog exists. |
| Customer-journey observability | Internal/engineering | Strong time-series fit but weaker customer story and demo emotion. | Use only if rubric favors internal engineering. |

### Stack fallbacks

- **Network or managed database failure:** Local Postgres/time-series container with identical SQL and synthetic data.
- **No Tiger Data:** Plain Postgres with materialized views or scheduled aggregates; isolate time-series extensions behind a thin adapter.
- **No LLM quota/network:** Deterministic rules plus templated Spanish explanations and, only for presentation, a cached transcript clearly labeled as fallback.
- **Auth failure:** Demo user with consent state represented locally.
- **ElevenLabs failure:** Text-only alert.
- **Deployment failure:** Localhost demo or approved tunnel; never discover this on presentation day.
- **Snowflake requirement:** Use Snowflake as the primary store or LLM API, not as a second analytical database alongside Tiger Data.
- **Backboard requirement:** Use it for conversational memory only and keep transaction truth in the primary ledger store.

### Sequencing rule

Build the thin core loop first:

> generator -> durable events -> features/rules -> visible live decision -> explanation

Only after this works end to end should the team add Auth0, audio, cloud deployment, domain polish, or optional memory/RAG.

## 11. Evidence Baseline and Research Discipline

The Mexico opportunity research reviewed consumers, salaried households, PYMES, informal workers, investors, regional inclusion, remittances, and fraud/security.

The evidence supports these broad conclusions:

- Formal financial-product access is not the same as active credit, formal saving, or financial resilience.
- Income informality and cash-heavy behavior make fixed-payday and always-online assumptions incomplete.
- Mexican microbusinesses are numerous, and CFDI/payment-complement state creates a locally distinctive B2B data opportunity.
- SPEI is a large, fast rail where a pre-submission intervention has clearer timing than post-settlement recovery.
- Fraud statistics, complaints, victimization surveys, and unauthorized-transfer categories measure different things and must not be combined.
- Public data do not establish national APP-scam prevalence, unique victims, successful loss, recovery, or a universal open-banking feed.
- A transaction-based lending study may show predictive value in one Mexican lender/sample, but it does not validate nationwide automated underwriting.
- Regional, rural, gender, disability, language, connectivity, and cash-use differences require fairness and accessibility testing.

### Evidence labels

Every claim in the pitch or documentation should be labeled mentally as one of:

- **Fact:** directly supported by a cited source.
- **Hypothesis:** product or causal proposition still requiring user, partner, or model validation.
- **Anecdote:** individual or vendor-reported experience, never population evidence.
- **TODO: Verify:** date, API access, legal interpretation, prize eligibility, or production capability not yet established.

Relevant detailed sources are collected in [`MEXICO-OPPORTUNITY-MAP.md`](MEXICO-OPPORTUNITY-MAP.md). No forum anecdote or unverified complaint statistic should become a ranking claim.

## 12. Open Decisions Before Implementation

1. Confirm whether the owner wants the repository's recorded hybrid to remain the formal product direction or wants the SPEI Intent Guard to supersede it as the official wedge.
2. Confirm the official judging rubric, weights, demo format, deadline, and prize eligibility.
3. Confirm whether any Capital One/Nessie-style sandbox or sponsor transaction API is required or available.
4. Confirm team size, skills, working time, and ownership of data, backend, agents, UI, and evaluation.
5. Choose the deployment assumption: local demo, one cloud provider, or approved hosted environment.
6. Confirm LLM provider, API key scope, quota, cost coverage, latency, and outbound network access.
7. Set acceptable latency, genuine-payment challenge rate, and accessibility targets for the demo.
8. Decide whether synthetic recipient-network features are worth the complexity; the MVP can work without them.
9. Define synthetic labels and scenarios without presenting them as real fraud ground truth.
10. Decide whether Auth0 and ElevenLabs fit after the core loop is stable.
11. Obtain a privacy/legal review for any device, call-state, recipient-network, or cross-institution signal before implementation.
12. Keep all sponsor credentials in environment variables or ignored local configuration.

## 13. Implementation Gate

Do not begin broad implementation until the following minimum contract is accepted:

- One named target user and one primary moment.
- One track framing, with any second track explicitly serving the same pipeline.
- One input event schema and one durable stream boundary.
- One scoring policy with visible reason codes.
- One reversible customer action.
- One evaluation dataset generated from synthetic scenarios.
- One demo metric and one false-positive metric.
- One documented fallback path.
- No real personal or financial data.

The first implementation slice should be small and executable: generate events, persist them, compute the core signals, and show a live decision. Everything else is secondary until that loop is demonstrable.

## 14. Related Documents

- [`docs/ai/knowledge/challenge-brief.md`](docs/ai/knowledge/challenge-brief.md) — canonical tracks and recorded repository direction.
- [`docs/ai/knowledge/aws-scalability.md`](docs/ai/knowledge/aws-scalability.md) — AWS-ready architecture constraints.
- [`CAPITAL-ONE-NEEDS.md`](CAPITAL-ONE-NEEDS.md) — sponsor context and original hybrid reasoning.
- [`FEASIBLE-TOOLS.md`](FEASIBLE-TOOLS.md) — sponsor-tool evaluation, alternatives, and fallback stacks.
- [`MEXICO-OPPORTUNITY-MAP.md`](MEXICO-OPPORTUNITY-MAP.md) — detailed research, evidence, ranking, and sources.
- [`CAPITAL-ONE-RAW.md`](CAPITAL-ONE-RAW.md) — raw sponsor-priority notes.
