# Capital One Challenge Brief (HackMTY)

## Purpose

This document records the sponsor-provided problem statement this repository is
built for, so every specialist plans against the real evaluation target instead
of a reconstructed one. It captures the challenge tracks as stated by the
sponsor, the track the repository owner indicated, and the owner-stated
constraints that shape architecture decisions. It does not define the solution
design; that belongs in `docs/ai/changes/` once a direction is approved.

## Sponsor tracks

The Capital One challenge offers three tracks. All three take raw transaction
streams as the primary input and ask for agentic, intelligent processing on top
of them.

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

## Selected direction

The repository owner's working note (`capitalOne.md`, untracked) states the
problem being worked as the **Risk & Security focus** track (track 3,
Real-Time Anomaly & Security Sentinel). Treat track 3 as the active direction
and raise a blocker rather than silently switching tracks if a task implies a
different one.

`TODO: Verify` — this is taken from an informal owner note, not a written
submission decision. Confirm with the owner before any commitment that is
expensive to reverse.

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
- Transaction ledgers are sensitive financial data. Apply
  `.agents/skills/security-baseline/SKILL.md` and route privacy-affecting
  decisions through the `privacy-compliance` role before they are implemented.
- Sponsor-issued credentials and API keys must never be committed. Keep them in
  environment variables or an ignored local file, per the externalized
  configuration rule in `docs/ai/knowledge/aws-scalability.md`.

## Sources

- Challenge tracks: sponsor-provided problem statement, relayed verbatim by the
  repository owner in the session that created this document.
- Selected track and constraints: `capitalOne.md`, the owner's untracked
  working note at the repository root.
