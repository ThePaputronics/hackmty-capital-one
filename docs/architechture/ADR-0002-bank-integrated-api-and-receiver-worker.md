# ADR-0002: Bank-Integrated API with a Continuous Receiver-Side Worker

- **Status:** Accepted
- **Date:** 2026-09-12
- **Scope:** `apps/spei-intent-guard-api` and every architecture document in `docs/`
- **Supersedes:** [`ADR-0001`](ADR-0001-canonical-mvp-architecture.md)
- **Driven by:** `docs/ai/knowledge/spei-guard-direction.md` (owner's direction of
  record, 2026-09-12) plus owner decisions taken the same day and recorded in
  section 6 below.

## 1. Decision

The system is **an API that a banking institution integrates**, backed by a
**continuous worker** that maintains receiver-side risk scores.

```text
   payer taps "enviar" in their bank's app
                │
                ▼
   bank POSTs transfer context ──────▶  Intent Guard API  ──┐
     amount, beneficiary CLABE,          payer-side signals │
     payer history, session, MTU state        +             │
                                        receiver-side score │
                ◀───────────────────────────────────────────┘
   decision + reason codes + Spanish explanation
                │
                ▼
   bank renders the warning in its own UI
                │
                ▼
   payer: cancel / verified callback / deliberate continue
                │
                └── outcome POSTed back ──▶ registry + metrics

   ┌──────────────────────────────────────────────┐
   │  worker, continuous, off the request path    │
   │  sweeps settled data for pass-through        │
   │  maintains per-CLABE scores + evidence       │
   └──────────────────────────────────────────────┘
```

Two consumer-visible surfaces:

- `POST /api/v1/risk/evaluate` — institution-authenticated. The bank sends
  transfer context and receives `allow` / `warn` / `pause` with reason codes and
  a Spanish explanation. Synchronous, sub-second.
- `GET /api/v1/clabe/{clabe}` — institution-authenticated, and answered **only
  in the context of a pending transfer held by the calling institution**.
  Returns the worker's precomputed score with its contributing factors.

The scam is stopped at the bank's own interface, by the payer, before
submission. The product sells **transparency** (a decomposable score, not a
black box) and **ease of use** (one endpoint, no model for the bank to train).

## 2. What changed since ADR-0001, and why

ADR-0001 stated: *"No component runs ahead of the API in the call graph."* That
is now false, and deliberately so. It was written before
`spei-guard-direction.md` was visible on `main` — that document was untracked
until `29d10b0` — so ADR-0001 reasoned from the superseded 2026-09-11 framing.

Three things moved:

1. **Receiver-side detection is in scope.** ADR-0001 assumed a purely
   payer-centered model, because that is what the data model and
   `HACKMTY-CONTEXT.md` described. The owner's direction adds Layer 2, a
   CLABE-scoped registry, and the cold start for it is behavioral detection
   contributed by institutions rather than user reports
   (`spei-guard-direction.md` §11). A worker computing those detections is
   therefore required, not optional.
2. **The audience is the rail operator.** Pitched to Banco de México with
   Capital One evaluating in that role. Seeing inbound flows across
   institutions is precisely what a single bank cannot do and the operator
   can, which is what makes receiver-side analysis legitimate here rather
   than an overreach.
3. **The caller is a bank, not an end user.** This resolves the question
   ADR-0001 could not: the API is a product consumed by institutions, which is
   what `docs/architechture/reference-architecture-api-as-product.png` and the
   "API as a product" framing always meant.

**What ADR-0001 got right and this ADR keeps:** the bank-facing call is
synchronous and request-scoped, the API is the entry point for it, and no LLM
agent runtime, event stream, `LISTEN/NOTIFY`, or SSE dashboard is in the MVP.
The worker is a batch path *beside* the request path, not a queue in front of
it.

## 3. Alternatives considered

- **A — Payer-side only (ADR-0001).** Ship the intent guard, no registry. Still
  the fallback if the worker does not finish: the direction note says plainly,
  *"If only one ships cleanly, ship Layer 1."*
- **B — Receiver-side only.** The worker and the lookup, no payer-side guard.
  Produces evidence but nothing that makes it actionable without blocking
  someone, which the governance rules forbid.
- **C — Both, unified behind one bank-facing call.** Chosen.
- **D — Two separate products.** Rejected: it splits the demo and doubles the
  integration cost for the first adopter.

## 4. Rationale

C is chosen because the registry only becomes safe when something consumes it
without blocking. The payer-side guard is that consumer: receiver-side evidence
enters as **one signal among the payer's own behavioral ones**, and the output
is an explanation shown to a human who can still proceed. Neither half is
sufficient alone — B has no safe delivery mechanism, A has no network effect and
no systemic pitch.

Unifying them behind a single call also answers the adoption question left open
in `spei-guard-direction.md` §13 ("who joins first, and what is their incentive
absent a mandate"): a bank integrates one endpoint, trains nothing, and reduces
its own complaint volume.

## 5. The merchant discriminator

`spei-guard-direction.md` §12 names this as failure mode 4: *"A legitimate
merchant looks like a mule on fan-in alone. Must be solved or the design flags
most small businesses in Mexico."*

Resolved by **weighting pass-through above fan-in**. Fan-in with repeated
identical amounts describes a gym, a school, a tanda, or any merchant with fixed
pricing. What distinguishes a mule is that funds do not rest: money arrives and
leaves within minutes and the residual balance sits near zero, whereas a
merchant accumulates and pays suppliers and payroll.

The receiver ruleset therefore weights `rapid_pass_through` and
`residual_balance_near_zero` at roughly 60% combined, and
`repeated_identical_amounts` at roughly 10%. A taquería with heavy fan-in and
identical amounts does not reach a high band on those weights alone.

## 6. Owner decisions recorded here

Two decisions taken on 2026-09-12, after `spei-guard-direction.md` was authored.
They override parts of its §7, and are recorded here rather than edited into
that document so the original reasoning stays intact.

**6.1 — The lookup returns a risk score, not an evidence count alone.**
§7 said *"Evidence counts, never verdicts"* and §6 contrasted Brazil's verdict
with a Mexican evidence count. The owner directed that the worker's ruleset
produce a numeric score.

Mitigation, and the reason this remains defensible: the score is never returned
bare. It carries `ruleset_version` and a `factors` array giving each contributing
rule with its `risk_points`, `weight`, `observed_value`, `baseline_value`, and a
plain-language explanation. A number alone is a black box; a number that
decomposes into named, reproducible rules with observed-versus-baseline values
is auditable and contestable. The transparency claim rests on the decomposition,
not on withholding the number.

**6.2 — Brazil's DICT is precedent, not a governance constraint.**
The owner clarified that Brazil is a success story establishing that
account-level fraud marking works at national scale. It is cited as validation
and as a design contrast. It does not bind Mexican design choices, and
`spei-guard-direction.md` §5's verified/unverified split still governs what may
be asserted about it on a slide.

**Retained from §7 unchanged:** no free burn-check — queries are
institution-authenticated and answered only against a pending transfer the
caller holds; a flag never blocks an account and never propagates as an
instruction to a bank; tiered decay windows; the right to know and contest;
CLABE only, never a person; and an innocent-receiver pattern routes to welfare
outreach rather than restriction.

## 7. Consequences

- Receiver-side entities are needed and do not exist yet. The schema has no
  global CLABE identity, no link from a payer-scoped beneficiary to an
  observable receiving account, and no cash-out or onward-transfer event. Fan-in
  cannot be computed and pass-through cannot be detected until these are added.
- `signal_results` and `risk_evaluations` are reused for receiver-side rows, so
  both halves speak one vocabulary: `risk_points` 1–5, `weight`,
  `observed_value`, `baseline_value`, `risk_level`, `ruleset_version`.
- The worker is stateless and horizontally scalable; per-CLABE state lives in
  the database. `computed_at` is distinct from `queried_at` in the lookup
  response because the GET is a cache read, which is what makes it fast at rail
  scale.
- Customer-facing copy is Spanish. Repository documentation, code, and commit
  messages stay English per `AGENTS.md`.
- Documents corrected alongside this ADR: `HACKMTY-ARCHITECTURE.md`,
  `HACKMTY-CONTEXT.md` §4 and §5, `spei-intent-guard-data-model.md`, and the
  app README.

## 8. Risks

- **Scope.** Two halves in the time remaining. Mitigation: Layer 1 is the
  fallback and ships alone if the worker does not land.
- **No ground truth.** `spei-guard-direction.md` §12 failure mode 1 — no public
  APP-fraud labels exist for Mexico. Synthetic labels, stated first, every time.
- **Score misread as a verdict.** Mitigated by 6.1's factor decomposition, by
  `blocks_account: false` in the payload, and by the contest path.
- **Absence read as endorsement.** A zero score must never mean "safe". The
  lookup response carries `absence_is_not_endorsement` explicitly.

## 9. Follow-up work

1. Receiver-side schema: CLABE identity, observable inbound flows, cash-out
   events, windowed aggregates.
2. Payer-side baseline service and signal engine, with the 1/2/3-signal policy.
3. `POST /api/v1/risk/evaluate`.
4. Receiver ruleset worker, weighted per section 5.
5. `GET /api/v1/clabe/{clabe}` with institution auth and pending-transfer
   context.
6. Spanish explanation templates, with an interface an LLM can implement later
   and a rules-only fallback.
7. Demo surface and metrics, reporting challenge rate as prominently as
   detection rate.

Carried forward from ADR-0001 and still open: extract `classify_seed_case` out
of the seed fixtures into the application, add an API Dockerfile, replace
lifespan `create_all()` with a real Alembic revision, and change monetary
columns from `Float` to `Numeric`.
