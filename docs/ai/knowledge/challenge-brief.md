# Capital One Challenge Brief (HackMTY)

## Purpose

This document records the sponsor-provided problem statement this repository is
built for, so every specialist plans against the real evaluation target instead
of a reconstructed one. It captures the challenge tracks as stated by the
sponsor, the direction the repository owner selected, and the owner-stated
constraints that shape architecture decisions. It does not define the solution
design; that belongs in `docs/ai/changes/` once a direction is approved.

**This document is authoritative for the challenge statement.**
`CAPITAL-ONE-NEEDS.md`, `CAPITAL-ONE-RAW.md`, and `FEASIBLE-TOOLS.md` are a raw
exploratory draft written before the canonical statement was available. They
remain useful as background research and as the reasoning behind the selected
direction, but where they disagree with this document, this document wins. Do
not treat their reconstructions of what the sponsor wants as requirements.

## Sponsor tracks

The following three tracks are the sponsor's canonical problem statement,
provided verbatim by the repository owner. All three take raw transaction
streams as the primary input and ask for agentic, intelligent processing on top
of them.

**A submission may target one track, or blend two or three.** The sponsor does
not require covering all of them, and a deliberate combination is a legitimate
submission rather than a scope compromise that needs justifying.

### 1. Consumer Financial Autonomy & Credit Building (B2C focus)

Develop intelligent agents that transform raw transaction streams into active
financial well-being — automating micro-savings, identifying subscription
leaks, or establishing cash-flow-based credit scoring for thin-file consumers.

### 2. SMB Cash-Flow & Working Capital Intelligence (B2B focus)

Build predictive treasury engines for small businesses that aggregate revenue
and operational expense streams to forecast 30-day liquidity, manage overhead,
and recommend timely working capital buffers.

### 3. Real-Time Anomaly & Security Sentinel (Risk & security focus)

Design behavioral anomaly detection engines that analyze transaction ledgers in
real time to flag unexpected transfer velocity, suspicious merchant category
hops, or abnormal account behaviors.

## Sponsor scope clarification (2026-09-12)

The owner relayed a clarification from Capital One: the submission **does not
need to solve a Capital One problem, or target Capital One as the customer.** It
should be innovative and capable of changing the Mexican financial system.

This resolves an ambiguity in the tracks below, and changes the target audience.
The submission is now pitched **to Banco de México**, with Capital One evaluating
in the role of the central bank / rail operator. See
[`spei-guard-direction.md`](spei-guard-direction.md) for what follows from that.

## Selected direction (2026-09-12) — supersedes the 2026-09-11 hybrid

The active direction is a **two-layer SPEI fraud-interception proposal**: a
pre-submission intent guard as the product surface and demo, plus a CLABE-scoped
flag registry as the proposed national standard. It blends tracks 3 and 1, which
the sponsor permits.

This **inverts** the emphasis of the 2026-09-11 decision rather than abandoning
it: interception leads, and coaching becomes the explanation surface rather than
the headline. The evidence behind the inversion, the Brazil/DICT precedent, the
MTU-evasion thesis, the governance requirements, and the settled scope boundaries
are recorded in [`spei-guard-direction.md`](spei-guard-direction.md), which is
authoritative for the direction. Ranked alternatives are in
[`mexico-opportunity-map.md`](mexico-opportunity-map.md).

Owner-directed, 2026-09-12.

## Prior direction (2026-09-11) — superseded, retained for history

The direction below was the decision of record until 2026-09-12. It is kept
because the reasoning still explains why both tracks remain in scope.

The active direction is the **hybrid** described in
[`CAPITAL-ONE-NEEDS.md` §4.2](../../../CAPITAL-ONE-NEEDS.md): a consumer
financial-wellness coach as the product surface, with real-time anomaly and
fraud detection as one agent inside it. The owner confirmed this on 2026-09-11,
reconciling two inputs that pointed in different directions:

- the owner's working note (`capitalOne.md`, untracked) named the **Risk &
  Security focus** track (track 3, Real-Time Anomaly & Security Sentinel);
- `CAPITAL-ONE-NEEDS.md` §4.1 recommended a wellness coach ("FlowGuard"),
  closer to track 1, and ranked a pure anomaly co-pilot as its first
  alternative because the theme is crowded.

The hybrid carries both themes without doubling scope. It means:

- the demo's primary surface is consumer-facing financial wellness — proactive
  nudges, runway forecasting, subscription and recurring-spend detection;
- anomaly and transfer-velocity detection is a first-class agent in that
  pipeline, not a separate product, and its alerts surface through the same
  coach interface;
- this blend of tracks 1 and 3 is explicitly permitted — the sponsor allows a
  submission to mix two or three tracks — so there is no requirement to collapse
  the work onto a single track before submitting, and no need to under-build
  either half to keep the entry "clean".

Do not drop either half, or re-scope to a single track, on your own initiative.
Raise a blocker instead.

## Owner-stated constraints

- **Scale target: ~100 million users.** The owner's note calls scalability the
  dominant requirement. This reinforces, and does not replace, the
  cloud-readiness checklist in `docs/ai/knowledge/aws-scalability.md`: design
  every service, data store, and API so it can be replicated onto AWS managed
  services without a redesign. Track 3 in particular implies a streaming,
  high-throughput ingestion path rather than request-scoped batch processing.
- **Stack direction: machine learning plus an AI API layer.** The owner's note
  names the Gemini API as the AI component alongside conventional ML.
  `TODO: Verify` — confirm the model provider before building against a
  specific SDK; the note is informal and no integration exists in this
  repository yet.
- **"Fit for purpose."** The owner's note flags fitness for purpose as an
  evaluation concern. Prefer a narrow, demonstrably working slice of the track
  over broad partial coverage of several tracks.

## Working rules derived from this brief

- Detection and scoring logic must be able to run on a transaction stream in
  real time, so it belongs behind a queue or stream abstraction rather than in
  request-scoped background threads (see `docs/ai/knowledge/aws-scalability.md`).
- The anomaly agent and the coaching agents read the same enriched event
  stream. Design the pipeline so detection is a consumer of that stream rather
  than a parallel path, or the hybrid degrades into two products.
- Transaction ledgers are sensitive financial data. Apply
  `.agents/skills/security-baseline/SKILL.md` and route privacy-affecting
  decisions through the `privacy-compliance` role before they are implemented.
- Sponsor-issued credentials and API keys must never be committed. Keep them in
  environment variables or an ignored local file, per the externalized
  configuration rule in `docs/ai/knowledge/aws-scalability.md`.

## Sources

- Challenge tracks and the one-or-more-tracks rule: sponsor's canonical problem
  statement, relayed verbatim by the repository owner on 2026-09-11. Authoritative.
- Constraints and the initial track signal: `capitalOne.md`, the owner's
  untracked working note at the repository root.
- Candidate directions and the hybrid framing: `CAPITAL-ONE-NEEDS.md`, itself
  synthesized from `CAPITAL-ONE-RAW.md`; tooling feasibility in
  `FEASIBLE-TOOLS.md`. Owner-designated raw draft, subordinate to this document.
- Hybrid selection: owner decision, 2026-09-11.
