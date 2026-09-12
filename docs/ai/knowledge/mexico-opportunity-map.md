# Mexico Opportunity Map — Ranked Niche Selection (Discovery, 2026-09-11)

## Status and scope

Product discovery only. No implementation. This document ranks candidate niches
for the Capital One challenge against evidence gathered from Mexican primary
sources, and recommends one niche plus two backups.

**This document does not change the targeted track.** `docs/ai/knowledge/challenge-brief.md`
remains authoritative. The owner requested this discovery round explicitly, and
its recommendation *does* diverge from the direction recorded there (see
"Tension with the recorded direction" below). Treat that divergence as a decision
the owner must make, not as a decision this document makes.

Raw research reports: `docs/ai/research/mexico-discovery-2026-09/` (7 reports,
each with its own citation table and explicit UNVERIFIED list).

## Evidence-quality rules used here

- **VERIFIED** = traced to a primary institutional document (INEGI, CNBV, Banxico,
  CONDUSEF, SAT, DOF) that a researcher actually opened.
- **INDUSTRY-REPORTED** = a company's own transactional data or press release.
  Directionally credible, not government-verified.
- **UNVERIFIED** = could not be traced to a primary source. Excluded from the
  evidence column of every opportunity below.

Statistics deliberately **excluded** after failing verification (do not put these
in a pitch deck):

| Claim | Why excluded |
| --- | --- |
| "26.5% of PYMEs die of lack of liquidity" (and competing "35%") | Traces through media aggregation to an inaccessible El Economista piece; the two figures contradict each other. INEGI's EDN 2023 counts business deaths but never asks why. |
| "65% of CONDUSEF complaints are unrecognized charges" | Tabasco regional office figure, not national. |
| "44% of households spend over half their income on debt" | Sourced to an **Argentina** study, not Mexico. |
| "94% credit rejection rate for thin-file" | A single 2019 CEO quote, not a regulator statistic. |
| "30% of adults affected by gota-a-gota" (attributed to ENIF 2024) | Does not appear in the ENIF 2024 report when pulled and converted to text. |
| Finerio user/savings counts; Kueski 1.8M users; $4.56B BNPL market | Self-published marketing claims, no independent audit. Kueski/Stori counts conflict across outlets. |

## The three constraints that shape every option

1. **Open Finance transactional APIs do not exist in Mexico.** CNBV published
   Ley Fintech Art. 76 secondary rules for the *open data* tier only (DOF,
   4 June 2020). The *aggregated* and *transactional* tiers have never been
   published and were still unpublished as of February 2026. VERIFIED, three
   independent corroborations. Consequence: never pitch "we use Mexico's Open
   Finance API." Correct framing is "via a Belvo/Prometeo-style aggregator,
   while the transactional-data rules remain pending at CNBV."
2. **The prototype cannot move money.** Holding or moving client funds requires
   CNBV IFPE authorization (12–18 month timeline). Everything we build must stay
   in the analytics / forecast / nudge / flag lane.
3. **Cash blinds the stream for the largest segment.** Labor informality is 54.8%
   (32.6M workers, Q1 2026) and cash was still ~88% of transactions in 2023.
   Any niche whose users are predominantly cash-based has no stream to process.
   This disqualifies "serve the informal economy" as a *primary* framing, however
   attractive it sounds.

## Ranked opportunity map

### O1 — Pre-settlement scam interception for SPEI transfers `RECOMMENDED`

- **Primary segment:** salaried workers and households (all banked consumers).
- **Track:** 3 primary, 1 secondary.
- **Pain:** SPEI identifies a payment only by CLABE — the displayed beneficiary
  name is not a verifying identifier — and a settled transfer is firm,
  irrevocable and enforceable against third parties. When a victim is socially
  engineered into authorizing the transfer themselves, neither bank is liable
  and the victim absorbs the loss.
- **Evidence:** CONDUSEF/BEF logged 1.515M fraud complaints in Q1 2026 (+31.5%
  YoY), ~75% of all complaints against financial institutions; 5.201bn pesos
  claimed, 1.265bn returned (**24.3%**). Full-year 2023: 33,329M pesos claimed,
  ~15% returned. VERIFIED via El Universal / El Informador reporting CONDUSEF
  data. The CLABE/irrevocability rule is VERIFIED as CONDUSEF's own public
  explanation; the exact Banxico circular article is `TODO: Verify`.
- **Why it matters:** millions of claims per year, three quarters of all banking
  complaints, and a legal structure that guarantees the user eats the loss.
- **Existing alternatives and limits:**
  - *MTU* (Monto Transaccional del Usuario) — mandatory on banks since
    1 Oct 2025, default 1,500 UDIs (~12,800 MXN), user configuration mandatory
    from 1 Jan 2026. Caps **damage**, not **incidence**; a scammer can coach the
    victim into raising their own MTU.
  - *Nu México "Fraud Alert"* — real pre-settlement destination-risk scoring, but
    single-bank and proprietary.
  - *OTP / device binding* — authenticates that the real customer pressed
    confirm, which is exactly what happens in this fraud.
  - *CONDUSEF fraud portal* — a lookup tool the victim must think to consult
    before transferring; not in the payment flow.
- **Product direction:** a risk layer that scores the transfer in the seconds
  before confirmation and inserts proportionate friction with a plain-language
  explanation naming the specific scam pattern.
- **Use of continuous data:** per-user beneficiary graph and payment-pattern
  baseline; deviation in amount / hour / frequency / destination; session and
  device change; velocity; destination-CLABE reputation.
- **Agentic actions:** hold and step-up verify; explain the matched pattern in
  human language; propose a temporary MTU reduction; pre-draft the CONDUSEF
  complaint if the user proceeds anyway. Every action human-overridable.
- **Mexico-specific signal worth building:** a transfer sized *just under the
  user's own MTU* is a plausible scammer-coaching tell that only exists because
  of the Oct 2025 rule. No incumbent can have a mature model for it yet.
- **Responsible AI / privacy / regulatory:** false positives block legitimate
  money movement, so the model must be explainable and appealable; never
  auto-freeze real funds; no protected-class proxies; synthetic data only for
  the demo, stated on stage.
- **Hackathon feasibility:** HIGH. Labeled fraud signal from IEEE-CIS / PaySim
  (disclosed as US/EU-shaped), Mexican-shaped synthetic SPEI stream, Nessie for
  transaction shape.
- **Differentiation:** HIGH. Consumer-facing, explainable, real-time anomaly
  detection was not found as a repeated HackMTY or BBVA winner pattern.
- **Demo potential:** the strongest of any option — a live stream, an alert
  firing in seconds, and a running "pesos saved vs. pesos lost" counter.

### O2 — The day-17 tax-date liquidity trap for PYMEs `BACKUP A`

- **Primary segment:** formally incorporated PYMEs under the general regime
  (Título II of the LISR).
- **Track:** 2.
- **Pain:** provisional ISR is computed on *ingresos nominales* — accrued and
  invoiced revenue — not cash collected, and is due by the 17th of the following
  month. A supplier therefore owes tax on money it has not received. RESICO's
  cash-basis carve-out exists precisely because this trap is recognized.
- **Evidence:** tax mechanics VERIFIED against SAT/LISR sources (HIGH confidence
  on the mechanism; no official quantification of how many firms it strains).
  DSO of ~66 days, 16% collected within 30 days, ~20% only after 90+ days —
  INDUSTRY-REPORTED (Xepelin transactional data on 17,300+ firms, via IDC 2026),
  not a government statistic. ENAPROCE 2018 (VERIFIED, primary PDF): 7 of 10
  MIPyMES would refuse bank credit at market terms, 57.9% because it is too
  expensive; only 8% had financing access in 2017; rejection reasons were no
  collateral 18.6%, bad credit history 17.2%, unprovable income 13.6%.
- **Existing alternatives and limits:** NAFIN Cadenas Productivas only reaches
  suppliers of enrolled large buyers; Xepelin/Konfío/Covalto price the
  receivable and need a confirming buyer; Clip Capital only covers merchants
  already processing card payments. **No reviewed product targets "tax due date
  collides with unpaid AR" as a distinct problem.**
- **Product direction:** a forward cash calendar built from the company's own
  CFDI feed that names the exact week the collision bites, plus per-invoice
  financing-eligibility triage (NAFIN-eligible / factoring-eligible / nobody).
- **Use of continuous data:** rolling DSO by buyer, forward 30/60/90-day cash
  position, alerting tied to the day-17 deadline.
- **Known weakness:** CFDI is **not** a real-time feed. SAT's Descarga Masiva is
  credential-gated (e.firma/CIEC), capped at 2,000 XML/day, limited to two
  full-content requests per date range, with 48-hour processing. The "constant
  data flow" half of the challenge theme would have to come from bank/POS data,
  not SAT.
- **Regulatory:** recommendation engine only — brokering or extending the
  financing would cross into licensed territory.
- **Differentiation:** HIGHEST of any option. Nobody is building this.
- **Demo potential:** weaker than O1 — a monthly cycle does not animate like a
  live interception.

### O3 — Cash-flow graduation and inclusion-premium repricing `BACKUP B`

- **Primary segment:** thin-file consumers; gig workers with platform income.
- **Track:** 1.
- **Pain:** thin-file is the majority condition, and the users who can only
  qualify for small tickets pay dramatically more for them.
- **Evidence:** ENIF 2024 (VERIFIED, INEGI/CNBV): only **37.3%** of adults 18–70
  hold any formal credit product — **62.7% hold none**; 15.7% have a bank credit
  card. Banxico rate disclosures (VERIFIED, primary PDFs): credit-card effective
  rate **53.9%** for limits ≤MXN 5,000 vs **21.3%** for limits >MXN 500,000
  (Jun 2023); individual microcredit averages **72.7%**, group microcredit up to
  **88.2%** (Aug 2024). ENIF 2021 rejection reasons: bureau problems 36%,
  insufficient income 27%, no credit history 19%.
- **Existing alternatives and limits:** Stori, Klar and Kueski already underwrite
  on alternative data; Compartamos and Banco Azteca already reach this segment at
  scale — they solved **access** but not **cost**. Palenca supplies gig-platform
  income verification but only for platform-active workers.
- **Product direction:** continuous re-scoring that *lowers price* as behavior
  proves out, rather than a one-time approval decision.
- **Honest caveat from the research:** the causal chain (informal work → no
  verifiable income → no bureau file → rejection) is **generic to emerging
  markets**. Mexico's distinguishing feature is the *scale* of informality, not a
  unique structural quirk. Do not claim Mexico-specificity here.
- **Differentiation:** MEDIUM-LOW — commercially crowded.
- **Risk:** credit scoring carries the heaviest fairness and explainability
  exposure of any option.

### O4 — Montadeudas early-warning

Mexico-specific and vivid (1,073 illegal lending apps per Excélsior; 5,800+ CDMX
reports Jan–Feb 2026), but the actual harm — contact-list extortion, doctored
images — happens entirely **off the transaction rail**. The loan disbursements
and aggressive repeat debits are partially visible. Best used as a *detector
inside* a larger product, never as the product.

### O5 — Quincena runway forecasting

Mexico's 15th/30th pay rhythm is a real institutional fact, and ENIF 2021 found
only 43% of adults could face an emergency with one month's savings. But this
sits directly adjacent to the single most repeated hackathon cliché (the
budgeting dashboard). Viable as a **component**, not as a headline.

### O6 — Total BNPL exposure aggregator

A genuine information gap: BNPL debt is split across Kueski, Aplazo, Nelo and
Mercado Pago with no single view. But the claim that all providers report to the
bureaus is UNVERIFIED sector-wide, and the market-size figures failed
verification. Needs primary confirmation before anyone builds on it.

### O7 — Micro-merchant "books from payments"

66% of ~8.1M microenterprises keep no accounting records at all (MODERATE
confidence — CNBV study located but PDF not re-read). Real problem, but Clip
Capital and Mercado Crédito already monetize exactly this signal commercially.

### O8 — Retail investor tooling

Ranked last on an honest fit verdict from the research itself: AFORE choice
inertia and GAT nominal-vs-real disclosure are point-in-time enrollment and
disclosure problems, not patterns that unfold in a transaction stream. Only two
sub-angles are stream-native (Ponzi early-warning from outbound-transfer
patterns; a realized real-yield translator), and both are narrower versions of
O1. Recommend not forcing this angle.

## Ranking table

| # | Opportunity | Magnitude | Evidence | Differentiation | Real-time demo | Feasibility | Regulatory safety | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O1 | SPEI scam interception | 5 | 5 | 5 | 5 | 5 | 4 | **34** |
| O2 | PYME day-17 trap | 4 | 4 | 5 | 2 | 3 | 4 | **26** |
| O3 | Thin-file graduation | 5 | 5 | 2 | 3 | 4 | 2 | **25** |
| O5 | Quincena runway | 4 | 4 | 2 | 4 | 5 | 5 | **24** |
| O7 | Micro-merchant books | 4 | 3 | 2 | 3 | 4 | 4 | **20** |
| O6 | BNPL exposure | 3 | 2 | 3 | 3 | 2 | 3 | **16** |
| O4 | Montadeudas warning | 3 | 4 | 4 | 2 | 2 | 2 | **17** |
| O8 | Retail investor | 2 | 3 | 2 | 1 | 3 | 2 | **13** |

Scores are the author's judgment on a 1–5 scale against the owner's stated
criteria, not a measured quantity.

## Resolved 2026-09-12 — direction moved past this document

The tension described below was resolved in favour of inverting the emphasis, and
then went further: a sponsor scope clarification (Capital One confirmed the work
need not target Capital One, and should be able to change the Mexican financial
system) reframed the submission as a **proposal to Banco de México**.

The direction of record is now [`spei-guard-direction.md`](spei-guard-direction.md).
This document remains valid as the **ranked evidence base** — the eight
opportunities, the scoring, and especially the rejected-statistics table are
unchanged and still govern what may be cited. Its recommendation section is
superseded.

## Tension with the recorded direction

`challenge-brief.md` records a 2026-09-11 owner decision for a hybrid: a consumer
wellness coach as the product surface, with anomaly detection as one agent inside
it. The evidence gathered here supports **inverting that emphasis** rather than
abandoning it:

- the anomaly/fraud half rests on the strongest evidence in the entire research
  set, and is the least crowded territory found;
- the coaching half — subscription leaks, budgeting nudges, spend categorization
  — maps onto four of the five documented hackathon clichés, including a pattern
  that already **won** BBVA's 2019 Mexico hackathon.

Inverting keeps the permitted tracks 1+3 blend intact and drops nothing. The
coach becomes the explanation and recovery surface for interception events rather
than the headline. **This requires an owner decision and an update to
`challenge-brief.md`; it is not taken unilaterally here.**

## Open decisions before implementation

1. Confirm the inversion above, or reaffirm the recorded coach-led hybrid.
2. Confirm the sponsor-issued API key's scope and quota, and the model provider
   (the brief names Gemini as `TODO: Verify`).
3. Decide whether to wire a Belvo or Prometeo sandbox for demo credibility, or
   run entirely on a self-authored synthetic generator.
4. Decide the stream substrate (Kafka / Kinesis / Redis Streams / in-process
   queue) against `docs/ai/knowledge/aws-scalability.md`.
5. Settle team split across generator, stream processor, agent layer, and UI.
