# F.R.E.D: open SPEI detection engine positioning

Decision recorded on 2026-09-12 from the user's product clarification.

## Product direction

F.R.E.D is the product identity for the existing Sentinel detection engine.
It detects risk associated with destination CLABEs and authorized-transfer
manipulation using transaction, recipient-network, and session context.
It is not a CLABE search product or a public account certification service.

The user clarified the operating model: F.R.E.D is API as a Service backed
by a worker that continuously processes SPEI transactions, correlates suspicious
activity by CLABE, and updates a persistent risk database. API consumers read
already-processed signals. A customer's transfer or API read does not start
the analysis. Keep processing and serving paths separate in all diagrams.

The proposed central operator is Banco de México. Participating institutions
consume the risk state and can warn customers before they send money. National
operation, data agreements, and institutional adoption remain proposals.
Financing remains undefined, as explicitly selected by the user.

The user confirmed open APIs and rules, protected data, and a proposed standard
for Banxico. The proposition is open interoperability and transparency of criteria,
inspired by Open Banking, with protected transaction data. FastAPI's OpenAPI
contract exists today. Institutional standard adoption, governance, and an
open-source license are not established by that fact.

## Presentation decisions

- Keep the large-type, slide-by-slide web format and the sober editorial style.
- Lead with public protection: a final warning before a scam transfer.
- Make cross-payer concentration toward a CLABE a central differentiator,
  while requiring corroboration and avoiding accusations about accounts.
- Show bank warnings using risk already processed by the worker. Existing
  `allow`, `challenge`, `pause` outcomes illustrate bank handling, not a new
  request-triggered computation or an implemented per-CLABE API contract.
- Treat F.R.E.D and Sentinel as product name and code name, not two products.
- Remove per-bank license pricing and service-revenue proposals. The user
  explicitly selected leaving financing undefined and focusing on public
  impact. Do not invent a funding model to fill the judging rubric.
- Frame scale as potential coverage, not an unsupported number of fraud victims.
- Use the executed synthetic benchmark; do not equate local speed with
  national capacity or claim a comparative advantage absent from its results.

This direction supersedes the earlier consultation framing in the web pitch
and the enterprise per-bank sales framing for this presentation. Existing
historical Sentinel pitch documents remain preserved.

## Evidence and next work

See `site/sources.md` for sources, exact implementation references, validation,
and the remaining governance, integration, data, security, and capacity work.
The scorer already counts distinct payers funding the same destination in
24 hours over available events. Cross-bank coverage depends on data inclusion
and payer identity; national visibility is not demonstrated.

The checked-out implementation has a background simulation worker in
`apps/generator/src/generator/server.py` / `player.py` that ingests events and
calls synchronous evaluation. It persists events and evaluations. Do not
misrepresent that finite simulator as proof of a production continuous risk
materializer or invent a per-CLABE read endpoint. The clarified product model
is the presentation contract; this implementation distinction belongs in
technical notes and sources.

No backend API, rules, production configuration, license, or deployment was
changed as part of this presentation revision.

## Five-minute executive revision

The user requested numbers first, removal of the fictional-persona slide and
repeated content, high-level value for PMs, and low-level cloud scalability.
The seven-slide version leads with SPEI scale and the executed synthetic
benchmark, then covers continuous processing, business outcomes, AWS scaling,
migration and the pilot ask. The timed notes total five minutes.

ECR, ECS/Fargate, ALB and RDS are a deployment proposal, not existing infra.
Dockerfiles and PostgreSQL/Alembic provide a portable base. Do not claim a
completed or adjustment-free migration. Horizontal scaling requires separate
API/worker services, coordinated work assignment and idempotency, shared state,
database capacity planning, and controlled single-run migrations. No cloud
resources, IaC, backend behavior or container build results were introduced.
