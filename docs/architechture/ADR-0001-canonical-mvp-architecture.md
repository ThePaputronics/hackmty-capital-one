# ADR-0001: Canonical MVP Architecture for SPEI Intent Guard

- **Status:** Superseded by
  [`ADR-0002`](ADR-0002-bank-integrated-api-and-receiver-worker.md) (2026-09-12)
- **Date:** 2026-09-12
- **Scope:** `apps/spei-intent-guard-api` and every architecture document in
  `docs/`
- **Supersedes:** the conflicting flows previously described in
  `docs/architechture/HACKMTY-ARCHITECTURE.md` and
  `docs/ai/engineers-discussion/HACKMTY-CONTEXT.md` section 8. Both have been
  corrected to match this decision; the table in section 2 records what they
  said beforehand.

> **Superseded.** This ADR was written before the owner's direction of record
> (`docs/ai/knowledge/spei-guard-direction.md`) was visible on `main`, and so
> reasoned from the superseded 2026-09-11 framing. Its central claim — *"No
> component runs ahead of the API in the call graph"* — no longer holds: a
> continuous receiver-side worker now runs beside the request path. Read
> [`ADR-0002`](ADR-0002-bank-integrated-api-and-receiver-worker.md) instead.
> What this ADR got right and ADR-0002 keeps: the bank-facing call is
> synchronous and request-scoped, and no agent runtime, event stream, or SSE
> dashboard is in the MVP. Retained for the reasoning trail.

## 1. Decision

The canonical architecture for the hackathon MVP is the **synchronous
request-scoped risk path** described in
`docs/ai/knowledge/mvp-stack-flow.html`:

```text
Bank/client  ──POST──>  FastAPI  ──>  Pydantic  ──>  risk engine  ──>  decision
                           │            (validate)      (score)       allow /
                           │                                │          warn /
                           └────────> SQLAlchemy + Postgres <┘          pause
                                      (context, evaluation, audit)
```

The API is the product surface and the entry point. Risk scoring is a function
the API calls inside the request, not a pipeline stage that feeds the API. No
component runs ahead of the API in the call graph.

Everything else currently drawn in the repository's architecture documents —
the LLM agent layer, the durable event stream, `LISTEN/NOTIFY`, SSE dashboards,
worker queues — is **deferred**, not cancelled. It is recorded in section 7.

## 2. Context, constraints, and forces

Three architecture descriptions entered the repository within one day and did
not agree with one another. This table records what each said when this
decision was taken; two of the three were corrected as part of it (section 6):

| Source | Commit | Flow it describes |
| --- | --- | --- |
| `docs/ai/knowledge/mvp-stack-flow.html` | `b28a6f7` (Gadiel) | API → Pydantic → Postgres → scikit-learn → decision |
| `docs/ai/engineers-discussion/HACKMTY-CONTEXT.md` §8 | `6415258` (Gerardo) | generator → event intake → features/rules → candidate anomaly → LLM agent layer → confirmation UI → audit |
| `docs/architechture/HACKMTY-ARCHITECTURE.md` | `e258cda` (Gerardo) | ML ingests → writes DB → DB feeds rules service → API is terminal |

These are not three zoom levels of one design. They disagree on three load-bearing
points:

1. **Whether an LLM agent runtime is in the MVP.** The context document
   specifies four agent roles (understanding, policy validation, explanation,
   optional action). The stack flow states the opposite rule verbatim: *"No
   Redis, no worker queues, no observability stack, no LLM agent runtime until
   the basic SPEI risk flow works end to end."*
2. **Call direction.** The mermaid diagram makes ML the front door and the API
   terminal, which is a batch pipeline. The stack flow makes the API the front
   door and ML a callee, which is an API-as-a-product. Only the second matches
   the data model and the code that exists.
3. **Async boundary.** The context document wants a durable stream with
   `LISTEN/NOTIFY` and SSE. Neither exists in the build, and the stack flow
   excludes both for now.

Forces acting on the decision:

- **Time.** The submission deadline is days away. The scoring path — the part
  that makes this a product rather than a schema — is entirely unbuilt.
- **What already exists.** `b28a6f7` shipped the API, schemas, CRUD layer, 13
  tables, and three seeded demo cases. It implements the first three boxes of
  the stack flow and nothing from the other two documents.
- **Judging criteria.** `docs/ai/knowledge/aws-scalability.md` makes AWS
  replicability a top evaluation priority, and `AGENTS.md` requires that
  checklist be applied from the start.
- **Track targeting.** `docs/ai/knowledge/challenge-brief.md` records a
  deliberate blend of sponsor tracks 1 and 3, and instructs that neither half be
  dropped unilaterally. This ADR changes no track targeting.
- **A stated privacy position.** `docs/ai/knowledge/spei-intent-guard-data-model.md`
  states under *Purpose* that the system "must not estimate whether a person or
  beneficiary is fraudulent," and its first modeling principle is "Score the
  transfer, not the receiver as a person." `HACKMTY-CONTEXT.md` §6 documents why
  reputation and complaint signals were deliberately removed.

## 3. Alternatives considered

### Option A — Synchronous request-scoped risk path (the stack flow)

The API receives a proposed transfer, validates it, loads payer context and
baseline from Postgres, scores it in-process, persists the evaluation, and
returns `allow` / `warn` / `pause` in the same response.

### Option B — Event-stream pipeline with an agent layer (the context document)

A synthetic generator writes to a durable event table. A feature/baseline/rules
stage consumes it, emits candidate anomalies, and hands them to four LLM agents
that understand, validate policy, explain, and optionally act. The UI reads via
SSE.

### Option C — ML-first batch pipeline (the mermaid diagram)

Person records enter an ML component, which writes detected anomalies to the
database. A rules service reads "anomalous persons" from the database and the
API serves the stored result.

### Option D — Keep all three documents and let the code decide

The current state. No document is authoritative; each teammate builds against
whichever one they read.

## 4. Trade-offs

| Dimension | A (sync path) | B (stream + agents) | C (ML-first batch) |
| --- | --- | --- | --- |
| **Complexity** | One process, one datastore, no broker | Stream, consumers, agent runtime, SSE | Pipeline stages plus a separate serving path |
| **Reliability by demo day** | High — three of five boxes already built and tested | Low — nothing built; four new failure surfaces | Low — nothing built |
| **Latency story** | Real. `risk_evaluations.latency_ms` is measurable and demoable at the moment of transfer | Poor. Async by construction; cannot answer "before you confirm" | Poor. Scores are precomputed, so the decision is stale |
| **Fits the product thesis** | Yes. The thesis is intervention *at the moment of transfer* | Partly. The confirmation UI is right; the pipeline in front of it is not | No. Precomputation cannot evaluate an intent that does not exist yet |
| **Security / privacy** | Neutral | Neutral | **Violates the stated position** — scores persons, persists "anomalous person" records |
| **AWS replicability** | Good. Stateless container behind an ALB, RDS behind it | Good eventually, but the queue boundary must be real before it maps to SQS/EventBridge | Poor. Batch state and serving state diverge |
| **Cost** | One service | Broker plus agent inference cost per event | Two runtimes |
| **Migration** | B remains reachable: extract the scorer behind an interface and the stream slots in front | Cannot be reduced to A without deleting work | Dead end for a real-time product |
| **Team ownership** | One backend owner, one clear seam for the scorer | Needs a stream owner and an agent owner concurrently | Unassigned |

## 5. Recommendation and rationale

**Adopt Option A.**

1. **It is the only one consistent with the code, the data model, and the
   product thesis simultaneously.** `spei-intent-guard-data-model.md` describes
   evaluating a transfer at the moment of submission against a payer baseline.
   That is a request-scoped operation. The `transfers` → `risk_evaluations` →
   `signal_results` → `decision_audits` chain in `src/app/models.py` is shaped
   for exactly that, down to `latency_ms` on the evaluation row.
2. **It is the shortest path to a working demo.** Option A needs one new module
   and one new endpoint. Options B and C need an entire runtime that does not
   exist, with two days left and the scoring logic still unwritten.
3. **It does not foreclose Option B.** If the scorer sits behind an interface
   and the API stays stateless, the event stream and the agent layer attach
   later without rewriting the request path. That is the property
   `aws-scalability.md` asks for, and it is why B is deferred rather than
   rejected.
4. **Option C is rejected on substance, not just timing.** A batch pipeline
   cannot score an intent that has not been expressed yet, and its data model
   contradicts a privacy position the team adopted deliberately.

## 6. Consequences

### Accepted

- `docs/ai/knowledge/mvp-stack-flow.html` is the authoritative architecture for
  the hackathon build. Architecture questions resolve against it.
- The risk engine moves into the application as `src/app/risk/`, exposed as
  `POST /api/v1/risk/evaluate`. It is called in-request and persists
  `risk_evaluations`, `signal_results`, and `decision_audits`.
- `classify_seed_case` in `scripts/demo_cases/seed_helpers.py` is scoring logic
  living in test fixtures. It moves into `src/app/risk/`, and the seed scripts
  call the real engine. Until that happens the demo outcomes are true by
  construction, which will not survive a judge's question.
- The API stays stateless. Per-request and per-evaluation state goes to
  Postgres, never to process memory.
- `src/app/sklearn_model.py` stays unused scaffolding until the rule-based
  scorer works end to end. A learned model is an enhancement to a working path,
  not a prerequisite for one.

### Corrections applied with this ADR

- **`docs/architechture/HACKMTY-ARCHITECTURE.md` was redrawn.** Its input node
  was `Personas (datos de entrada)` and one database edge was labelled
  `persona anomala`. Both described person-level risk scoring, which the data
  model forbids and which §6 of the context document records as deliberately
  removed for legal and abuse reasons. This was a documentation defect, not a
  code defect — nothing built scores persons — but it was the artifact most
  likely to end up on a slide. The diagram now enters at the API, scores a
  transfer, and carries an explicit scope constraint.
- The same file was written in Spanish; `AGENTS.md` and `CLAUDE.md` both
  require English for documentation unless the user asks otherwise. It has been
  translated.
- **`HACKMTY-CONTEXT.md` §8 is retitled "Architecture Direction (Post-MVP)"**
  with a deferred-status note linking here, so its agent layer reads as a
  roadmap rather than a build instruction.

### Risks

- Deferring the agent layer weakens any sponsor-prize argument that depends on
  demonstrating agentic behavior. Mitigation: the explanation step already
  produces customer-facing text and reason codes from
  `decision_audits`; it can be upgraded to an LLM call behind the same
  interface if time allows, without touching the request path.
- A rules-only scorer may read as unsophisticated next to an ML submission.
  Mitigation: explainability is the differentiator here, and per-signal
  `risk_points` with reason codes explains a decision in a way a black-box
  score cannot.
- Writing evaluations synchronously puts scoring latency in the user's request.
  Mitigation: record `latency_ms` per evaluation from the first version, so the
  cost is measured rather than assumed.

### Rejected alternatives

- **Option B** — deferred, not rejected. Revisit after the synchronous path
  works end to end.
- **Option C** — rejected permanently. Wrong call direction for a real-time
  product and incompatible with the privacy position.
- **Option D** — rejected. Three authoritative documents mean none is
  authoritative.

## 7. Deferred, explicitly

Not in the MVP. Not cancelled. Do not build these before the synchronous path
works end to end:

- LLM agent runtime (understanding, policy validation, explanation, action
  agents)
- Durable event stream and `LISTEN/NOTIFY` queue boundary
- SSE or WebSocket live dashboard
- Redis, worker queues, background job runners
- Observability stack beyond structured stdout logging
- Learned anomaly model replacing the rule-based scorer
- Public CLABE lookup and the two bank-app interfaces shown as optional in
  `HACKMTY-ARCHITECTURE.md`

## 8. Follow-up work

Ordered by what blocks the demo:

1. Extract `classify_seed_case` into `src/app/risk/` and add
   `POST /api/v1/risk/evaluate`.
2. Add a Dockerfile for the API. `compose.db.yaml` starts Postgres only, so the
   service that matters is unpackaged, and "containers as the deployment unit"
   is a required item in `aws-scalability.md`.
3. Replace lifespan `create_all()` with a real Alembic revision.
   Alembic is scaffolded but has no `migrations/versions/` directory at all, and
   concurrent replicas currently race to build the schema on boot.
4. Change monetary columns from `Float` to `Numeric`. They feed threshold
   comparisons such as `amount_near_mtu`.
5. Rename `docs/architechture/` to `docs/architecture/` once no in-flight branch
   is touching it.

## 9. Placement note

`.agents/skills/architecture-decisions/SKILL.md` directs cross-project decisions
to a global `decisions/` directory and project-specific ones to
`projects/<project>/decisions/`. Neither directory exists in this repository,
which is single-project and keeps architecture under `docs/architechture/`. This
ADR is filed alongside the document it supersedes. If a `decisions/` directory
is later adopted, move this file there.

## 10. References

- `docs/ai/knowledge/mvp-stack-flow.html` — adopted architecture
- `docs/ai/knowledge/spei-intent-guard-data-model.md` — entity model and
  scoring constraints
- `docs/ai/knowledge/aws-scalability.md` — cloud-readiness checklist
- `docs/ai/knowledge/challenge-brief.md` — sponsor tracks and scope constraints
- `docs/ai/engineers-discussion/HACKMTY-CONTEXT.md` — product context; §6
  privacy position, §8 deferred direction
- `docs/architechture/HACKMTY-ARCHITECTURE.md` — high-level diagram, corrected
  to match this decision
- `apps/spei-intent-guard-api` — current implementation (`b28a6f7`)
