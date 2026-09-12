# Research 05 — Mexican Salaried Households: Debt, Recurring Expenses, Budgeting, Payroll-Linked Credit

Scope: consumer-finance discovery for a HackMTY / Capital One challenge team. Angle = salaried
workers and households in Mexico. All figures are dated; VERIFIED FACT items carry a working URL
consulted directly (or via a cached PDF extracted with `pdftotext`). Items without a source I could
verify are explicitly marked UNVERIFIED.

---

## Top pain points (ranked)

### 1. Non-bank payroll/personal-loan APRs are extremely high and poorly disclosed (nómina + personales)
- **Population**: ~5.1 million active bank payroll (nómina) credits (Jun 2024, comparable portfolio) — a
  subset of Mexico's ~22.5 million IMSS-formal workers who are the addressable base for payroll-deducted
  credit. [Banxico RIB Nómina, jun-2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7BDE287CA8-3D16-FACA-2AAB-D8B88728C998%7D.pdf); [IMSS employment, Dec-2025](https://www.imss.gob.mx/prensa/archivo/202512/616).
- **Pain**: weighted-average contract interest rate on payroll loans was **26.9–27.0%** in Jun-2024
  (balance = 349.9 billion pesos), but individual banks charge far more for smaller loan segments — one
  segment averaged **32.9%** weighted rate. Personal loans (non-payroll) are worse: 80% of the
  outstanding balance sits between **24.0% and 65.0%** interest (Feb-2024), and delinquency (IMOR) for
  personal loans was **12.9%**, the highest of any consumer-credit type Banxico tracks. [Banxico RIB
  Nómina](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7BDE287CA8-3D16-FACA-2AAB-D8B88728C998%7D.pdf) (pp. 17-18, 24); [Banxico RIB Créditos Personales, feb-2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-personales/%7B01469D83-2BB3-A5CB-95E4-6B11ABEE2DED%7D.pdf) (pp. 15-16, 6).
- **Why unsolved**: CAT/rate disclosure exists (Banxico publishes it bimonthly) but it's a static PDF
  report and a developer-only API (`comparador.banxico.org.mx`), not something surfaced to a borrower at
  the moment of decision inside their banking app. No consumer tool translates "your payroll loan's real
  cost vs. what you could get" into an actionable nudge.
- **Mexico-specific**: Yes — payroll deduction directly from the wage-deposit account, offered by the
  same bank that runs the employer's payroll dispersal, is a distinctly Mexican consumer-credit
  mechanism (see mechanics section).

### 2. Revolving credit-card debt: ~4 in 10 cardholders pay ~38% effective interest
- **Population**: Dec-2024 comparable card portfolio = 25.8 million cards; **41.3% (10.7 million cards)**
  are "no-totaleros" (revolvers) carrying 348.5 billion pesos in balances (63.4% of total card balance
  concentrated in these accounts). [Banxico RIB Tarjetas de Crédito, dic-2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-tarjetas-de-credito/%7BB30B21EE-FC4A-34AC-FC8E-60307C8C5E63%7D.pdf) (pp. 9, 11).
- **Pain**: the weighted-average effective rate (TEPP) paid by no-totaleros was **37.7%** — 13.8pp above
  the blended system average — because totaleros pay 0%. Of revolvers who paid at least the minimum,
  **24.9%** paid only the minimum due (i.e., are structurally rolling debt forward every cycle). [same
  source], pp. 9-11.
- **Why unsolved**: banks' own apps show statement balance and minimum due but rarely show "at this
  rate, paying only the minimum will cost you X and take Y months" at the point of payment. This is a
  known dark pattern globally, but no Mexican PFM tool I found closes it with real transaction/statement
  data.
- **Mexico-specific mechanics but generic problem**: revolving-debt psychology is universal; the totalero/
  no-totalero framing and CAT disclosure regime are Mexico/Banxico-specific.

### 3. Debt-collection harassment and multi-loan over-indebtedness are a top consumer complaint
- **Population/frequency**: REDECO (CONDUSEF's collection-agency registry) logged **27,752 complaints**
  in 2020 covering 114,887 individual grievances from 16,151 complainants against 395 institutions
  (most recent aggregate figure found with a public breakdown). [CONDUSEF REDECO](https://www.condusef.gob.mx/?p=redeco) — UNVERIFIED for 2023-2024 aggregate totals (see below). More recent partial data: complaints against
  banks tied to collection management reached **3,254 in Jan-Feb 2024 alone**, up 9.7% YoY; February 2024
  alone had 1,522 complaints (+5% YoY). [El Informador, dic-2024](https://www.informador.mx/mexico/Condusef-Estos-fueron-5-bancos-con-mayor-numero-de-quejas-por-cobranza-en-2024-20241224-0070.html).
- **Pain**: top complaint causes historically are collection contact with third parties not party to the
  debt (15%) and threats/intimidation (12.1%) [CONDUSEF REDECO 2020 data via search summary — **UNVERIFIED**, could not open a primary CONDUSEF PDF with this exact breakdown; treat as directionally indicative only].
  "Bicicleteo" (paying one card with another / carousel debt) is acknowledged as a common, CONDUSEF-flagged
  risky behavior, but I found no hard incidence statistic — this is **UNVERIFIED as a quantified
  phenomenon**, only qualitatively documented. [Expansión, 2023](https://expansion.mx/finanzas-personales/2023/05/12/pagar-tarjeta-credito-con-otra); [RappiCard blog, 2026](https://rappicard.mx/2026/01/14/pagar-tarjeta-de-credito-con-otra/).
- **Why unsolved**: REDECO is a complaint registry, not a preventive/early-warning tool for the
  over-indebted consumer; nothing surfaces "you now hold N simultaneous debt products, service ratio is
  rising" to the household in real time.

### 4. Unrecognized/recurring charges ("cargos no reconocidos") are a leading complaint category
- **Population/severity**: CONDUSEF states unrecognized-charge claims "head" the most frequent banking
  complaints nationally; a regional (Tabasco) CONDUSEF office reported **65% of local complaints** are
  for unrecognized card charges — **this 65% figure is regional, not national; do not generalize it**.
  [Xevt/Tabasco, n.d.](https://www.xevt.com/tabasco/65-de-quejas-son-por-cargos-no-reconocidos-en-tarjetas-bancarias-condusef/366968). Nationally, of unrecognized-charge complaints, credit card ≈53% / debit
  card ≈47% of cases, and **74% of credit-card complaints and 73% of debit-card complaints** cite
  "consumption not actually performed" as the cause, with point-of-sale terminals responsible for 40% of
  cases and e-commerce for 26%. [CONDUSEF](https://www.condusef.gob.mx/?p=contenido&idc=492&idcat=1); [CONDUSEF](https://www.condusef.gob.mx/?p=contenido&idc=811&idcat=1).
- **Why unsolved**: subscription/recurring-charge cancellation friction and cardholder inability to
  identify which merchant a charge belongs to (common cause of "unrecognized" disputes) is a recurring,
  low-severity-but-high-frequency annoyance that no consumer tool proactively flags or explains using
  transaction-level merchant enrichment.
- **Mexico-specific?** Generic problem (seen worldwide); the CONDUSEF complaint channel and process are
  Mexico-specific.

### 5. Households have essentially no slack between quincenas and thin emergency buffers
- **Population**: ENIF 2021 (CNBV/INEGI, national financial-inclusion survey) found only **58% of
  adults** can cover expenses with current income, and only **43%** could face an economic emergency using
  savings equivalent to one month's income. [BBVA Research summary of ENIF 2021](https://www.bbvaresearch.com/wp-content/uploads/2022/05/2022-05-23-ENIF-2021.pdf); [La Silla Rota on CNBV ENIF](https://lasillarota.com/negocios/2025/5/26/de-cada-10-mexicanos-utilizan-ahorros-para-emergencias-segun-la-cnbv-537942.html) (~4 in 10 use savings for emergencies).
- **Pain**: ENIGH 2024 (INEGI) shows average quarterly household spending of 47,674 pesos against average
  quarterly current income of 77,864–81,920 pesos nationally — but this masks a **poorer-household deficit**:
  INEGI/press coverage explicitly notes lower-decile households' spending exceeds income, forcing debt to
  cover basic needs. [INEGI ENIGH 2024 press release](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enigh/ENIGH2024_RR.pdf); [El Universal, 2025](https://www.eluniversal.com.mx/opinion/julio-alejandro-millan/enigh-2024-mas-ingreso-menos-bienestar-el-falso-alivio-para-los-hogares-mexicanos/).
- **Why unsolved**: no bank app I found translates "quincena spending velocity" into a forward-looking
  cash-crunch warning before the 13th/28th day of the cycle.
- **Mexico-specific**: Yes, strongly — the quincena rhythm and the specific ENIF/ENIGH instruments are
  Mexican institutional facts, even though "living paycheck to paycheck" itself is a global phenomenon.

### 6. BNPL debt growth outside the traditional bureau/underwriting picture
- **Population/scale**: Mexican BNPL market value reached **USD 4.56 billion in 2024**, projected to
  grow ~25-27.6% CAGR toward 2026 (~USD 5.08–6.0B). Kueski Pay reports **1.8 million unique users**
  (2024 figure, secondary source). Millennial/Gen-Z adoption: **38% of millennials, 31% of Gen Z** report
  BNPL as a preferred payment method. [Vanguardia/dineroenimagen roundups, 2025](https://vanguardia.com.mx/vida/en-este-buen-fin-2025-podras-aplicar-el-esquema-compra-ahora-paga-despues-DL17491046); [marketing4ecommerce, 2025-2026](https://marketing4ecommerce.mx/kueski-pagos-de-servicios-y-recargas-en-quincenas-en-mexico/) — **treat exact user/market-value figures as UNVERIFIED-grade** (derived from AI-summarized secondary/marketing sources, not a primary CNBV/Banxico statistical release).
- **Bureau visibility**: Kueski reports its loans/Kueski Pay activity to Círculo de Crédito (which feeds
  Buró de Crédito); late payments generate negative reports typically after 30-60 days. [Kueski help
  center](https://preguntas.frecuentes.kueski.com/hc/es/articles/20618937778459) — **this is Kueski's own
  claim about itself; I could not independently verify from Círculo de Crédito/Buró de Crédito that ALL
  BNPL providers (Aplazo, MercadoPago cuotas, Nelo) report consistently — mark as UNVERIFIED for the
  sector as a whole.**
- **Regulatory status**: No BNPL-specific law as of 2025; providers operate mostly as SOFOMs regulated
  indirectly by CNBV/CONDUSEF under general fintech/consumer-protection rules. CNBV's September 2025
  update to Fintech Law secondary provisions (effective Jan 2026) tightens capital/governance rules for
  fintech institutions generally, not a BNPL-specific regime. [Secondary summary source](https://www.puntored.mx/en/bnpl-en-mexico-oportunidades-retail-finanzas/) — **UNVERIFIED against a primary CNBV circular; I did not find the actual DOF/CNBV text confirming this.**
- **Why unsolved**: because BNPL splits across several small non-bank apps, a consumer/lender has no
  single place to see "total BNPL exposure across providers" the way a bureau aggregates bank debt — this
  is the core information gap a Capital One-style aggregator could fill, *if* the underlying bureau
  reporting claim above is verified with a primary source before building on it.

---

## Key statistics table

| Figure | Year | Source URL |
|---|---|---|
| Payroll (nómina) comparable portfolio: 5.1M credits, 349.9bn pesos, weighted avg. rate 26.9-27.0% | Jun 2024 | https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7BDE287CA8-3D16-FACA-2AAB-D8B88728C998%7D.pdf |
| Payroll loan delinquency (IMOR) 2.7%; adjusted delinquency (IMORA) 10.9%; CR2 concentration 59.6%, CR5 97.3%, HHI 2,438 (highest of consumer credit) | Jun 2024 | same as above |
| Personal-loan segment: 80% of balance carries 24.0-65.0% interest; delinquency (IMOR) 12.9%, highest among consumer credit types | Feb 2024 | https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-personales/%7B01469D83-2BB3-A5CB-95E4-6B11ABEE2DED%7D.pdf |
| Credit cards: 25.8M comparable cards, 549.8bn pesos balance; 58.7% totaleros / 41.3% no-totaleros | Dec 2024 | https://www.banxico.org.mx/publicaciones-y-prensa/rib-tarjetas-de-credito/%7BB30B21EE-FC4A-34AC-FC8E-60307C8C5E63%7D.pdf |
| No-totaleros: 10.7M cards, 348.5bn pesos balance (63.4% of total balance); weighted effective rate (TEPP) 37.7% | Dec 2024 | same as above |
| Of no-totaleros making ≥minimum payment: 24.9% pay only the minimum | Dec 2024 | same as above |
| ENIF: only 58% of adults can cover expenses with current income; only 43% could cover an emergency with ≥1 month of savings | 2021 | https://www.bbvaresearch.com/wp-content/uploads/2022/05/2022-05-23-ENIF-2021.pdf |
| ENIGH: avg. quarterly household income 81,920 pesos (current income 77,864); avg. quarterly spend 47,674 pesos; income +10.1%, spend +8.7% vs 2022 | 2024 | https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enigh/ENIGH2024_RR.pdf |
| IMSS formal employment (addressable base for payroll products) ≈22.5-22.8 million jobs | Dec 2025 | https://www.imss.gob.mx/prensa/archivo/202512/616 |
| REDECO collection complaints: 27,752 complaints / 114,887 grievances / 16,151 complainants / 395 institutions | 2020 | https://www.condusef.gob.mx/?p=redeco |
| Collection-related bank complaints: 3,254 in Jan-Feb 2024 (+9.7% YoY) | 2024 | https://www.informador.mx/mexico/Condusef-Estos-fueron-5-bancos-con-mayor-numero-de-quejas-por-cobranza-en-2024-20241224-0070.html |
| BNPL market value ≈USD 4.56bn, ~40% YoY growth (secondary source, not primary CNBV data) | 2024 | https://vanguardia.com.mx/vida/en-este-buen-fin-2025-podras-aplicar-el-esquema-compra-ahora-paga-despues-DL17491046 |
| Kueski Pay ≈1.8M unique users (secondary source) | 2024 | https://marketing4ecommerce.mx/kueski-pagos-de-servicios-y-recargas-en-quincenas-en-mexico/ |
| Finerio PFM: 250k+ users, reported ~20-21% spend reduction within 3 months of use (self-reported, no independent audit found) | ~2019-2022 | https://blog.finerioconnect.com/personal-finance-management-o-pfm-finanzas-personales-en-tu-celular/ |
| Fintonic exited the Mexico market | 2025 | https://www.df.cl/mercados/banca-fintech/nuestro-viaje-ha-terminado-fintech-espanola-fintonic-cierra-sus-operaciones-en-chile (re: pattern; Mexico exit reported in secondary aggregator, cross-check before citing precisely) |

---

## Mexico-specific mechanics worth designing around

- **Nómina payroll deduction**: Banks that run a company's payroll dispersion also typically offer the
  payroll loan to that company's employees, deducting repayment directly from the wage-deposit account
  before the employee ever sees the cash — reducing default risk and information asymmetry for the
  lender, but also meaning the borrower's *effective* take-home pay silently shrinks each pay period.
  Confirmed mechanic description: [Banxico RIB Nómina](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7BDE287CA8-3D16-FACA-2AAB-D8B88728C998%7D.pdf), Section 2. "Portabilidad de nómina" (payroll portability — moving your payroll deposit to
  a different bank) is a named, regulated concept in the same report — a hook for a product that helps
  users understand/exercise this right.
- **Quincena (15th/30th) pay cycle**: multiple qualitative/secondary sources describe cash-flow structured
  tightly around the biweekly cycle — e.g., a Research Land study cited via Publimetro claims 86% of a
  quincena goes to food/rent/services with only ~14% flexible, and a Kueski-linked marketing piece frames
  quincena as "the rhythm that organizes millions of Mexican families' lives." **Both of these are
  marketing-adjacent secondary sources, not an academic or Banxico/INEGI primary study — treat the exact
  percentages as HYPOTHESIS-grade, though the underlying quincena-driven cash-flow-cliff pattern is widely
  and consistently described.** [Publimetro/Research Land](https://www.publimetro.com.mx/noticias/2026/08/16/la-quincena-ya-llega-gastada-86-se-va-en-comida-renta-y-servicios/); [marketing4ecommerce](https://marketing4ecommerce.mx/kueski-pagos-de-servicios-y-recargas-en-quincenas-en-mexico/).
- **Aguinaldo**: Mexican year-end mandatory bonus (legally ≥15 days' salary) — I did **not** get to
  independently pull a primary Banxico/INEGI/retail study quantifying an aguinaldo spending spike in this
  session; **flag as an assumed-but-not-directly-verified mechanic in this pass** — worth a follow-up
  search specifically on "efecto aguinaldo" retail sales data (ANTAD, Banxico) before relying on it.
- **CAT (Costo Anual Total) disclosure regime**: Banxico is legally required (Ley para la Transparencia y
  Ordenamiento de los Servicios Financieros, Art. 4 Bis 2) to publish bimonthly rate/CAT comparability
  reports for nómina, personales, tarjetas, automotriz, vivienda, and PyME credit. This is a rich,
  structured, machine-readable-ish (PDF + an internal comparator API) data source unique to the Mexican
  regulatory environment that a product could ingest to show users "your real cost vs. market" — but note
  the API (`comparador.banxico.org.mx`) appears to require specific request parameters I could not
  successfully query in this session; would need further technical investigation before assuming it's
  freely consumable. [Banxico comparador](https://comparador.banxico.org.mx/ComparadorCrediticio/apiHtml/scnr-credito-de-nomina-cat-y-tasas.jsp).
- **Totalero/no-totalero framing** is a Banxico-standard, Mexico-specific taxonomy (not just "revolver"
  vs. "transactor" as used in the US) with its own regularly-published statistics — good vocabulary and
  a ready-made benchmark for a product's own risk segmentation.

---

## Existing players and their gaps

- **Finerio (Finerio Connect)**: pivoted from consumer PFM app to B2B open-banking/data-aggregation
  infrastructure ("Connect") sold to financial institutions; self-reported historical consumer numbers
  (250k+ users, ~20% savings in 3 months, 4th most-downloaded fintech app in Mexico in 2019) are
  **self-published marketing claims**, not independently audited. [Finerio blog](https://blog.finerioconnect.com/personal-finance-management-o-pfm-finanzas-personales-en-tu-celular/). Gap: now primarily an infra vendor,
  not a consumer product competing directly in this space anymore.
- **Fintonic**: exited Latin America (Chile 2023, then Mexico reportedly ~2025) citing unsustainable
  funding costs for its lending business; reverted to a Spain-only operation. Gap/lesson: a lending-driven
  PFM model was not viable in the Mexican funding-cost environment — a pure-insight/no-balance-sheet
  product may be a more durable wedge. [df.cl](https://www.df.cl/mercados/banca-fintech/nuestro-viaje-ha-terminado-fintech-espanola-fintonic-cierra-sus-operaciones-en-chile) (Chile exit, directly confirmed); Mexico-specific exit date is from a
  secondary aggregator and **should be re-verified** before citing precisely.
- **Coru**: mentioned in the brief as an existing Mexican PFM/financial-education play; I did not
  independently verify current user base or specific claims in this session — **UNVERIFIED, not
  researched in depth this pass**.
- **Bank-native budgeting features** (BBVA México's own educational content on quincena budgeting,
  "apartados"/savings pockets, spend-control dashboards): these exist and are actively marketed by BBVA
  México, but they are static educational content plus basic categorization — no evidence found of
  predictive quincena-cliff alerts or cross-bank aggregation. [BBVA México education hub](https://www.bbva.mx/educacion-financiera/ahorro/ahorro/apartados-organiza-tu-pago-quincenal.html).
- **General adoption-barrier hypothesis** (not independently verified this pass, carried from general
  fintech-adoption knowledge): low PFM adoption in Mexico is commonly attributed to distrust of connecting
  bank credentials to third parties, low smartphone-banking penetration among lower-income/cash-heavy
  segments (marketing4ecommerce notes 75-85% of transactions still cash), and lack of open-banking
  account-aggregation rails comparable to Plaid — **mark this explanation as HYPOTHESIS**, it was not
  confirmed against a dedicated adoption study.

---

## What is UNVERIFIED (explicit list)

- Exact national (not regional) percentage of CONDUSEF complaints attributable to "cargos no
  reconocidos" — only a Tabasco-specific 65% figure and category-level breakdowns (74%/73% "consumption
  not performed") were found with a URL; no single verified *national* headline percentage.
- REDECO complaint volumes for 2023/2024 in the same structured format as the 2020 figures (27,752
  complaints) — only partial, differently-scoped figures (e.g., "3,254 complaints Jan-Feb 2024") were found.
- Any quantified incidence rate of "bicicleteo" (revolving debt between cards) — only qualitative/
  advisory content confirming the practice is known and cautioned against by CONDUSEF and banks.
- BNPL market size (USD 4.56B, 2024) and Kueski Pay's 1.8M-user figure — sourced via AI-summarized
  secondary/marketing articles, not a primary CNBV, Banxico, or company financial disclosure.
- Whether *all* major Mexican BNPL providers (not just Kueski) report to Círculo de Crédito/Buró de
  Crédito — only Kueski's self-description was found.
- Any specific CNBV/CONDUSEF *regulation* naming BNPL directly (a specific circular, rule, or bill) — I
  found only general commentary that BNPL sits in a "regulatory gray area" and that the Fintech Law's
  secondary provisions were updated (effective Jan 2026) for fintech institutions broadly; I did not
  locate primary DOF/CNBV text confirming BNPL-specific rules.
- Aguinaldo spending-spike data (retail sales, Banxico, or ANTAD figures around December) — not
  retrieved in this session; treat the aguinaldo cash-flow-spike premise as plausible-but-unconfirmed.
- The Mexican card-on-file/subscription cancellation rule (e.g., a right to cancel recurring charges
  purely online without contacting the merchant) — not confirmed to exist in this session; do not assume
  a "click to cancel" rule is in force in Mexico without further verification.
- Coru's user base, product scope, and current market position — not researched in this pass.
- Precise Fintonic Mexico exit date/details — derived from a secondary aggregator article, not a primary
  company announcement.

---

## Product opportunity hypotheses

1. **Quincena cash-flow forecaster + pre-emptive nudge.** Using continuous transaction data (not just a
   monthly statement snapshot), a product could detect each user's actual payday cadence (many salaried
   workers are quincenal, some are weekly/monthly) and forecast, days in advance, the point at which
   discretionary balance will hit zero before the next deposit — then suggest deferring a specific
   discretionary purchase or moving a bill's due date. Continuous data enables the day-level curve that a
   single ENIGH/ENIF snapshot cannot: those surveys show the *average* income/spend gap (e.g., 47,674 vs.
   77,864-81,920 pesos quarterly) but not the *within-cycle* shape, which is exactly the quincena-cliff
   pattern this angle targets.

2. **"Real cost of your revolving balance" simulator fed by live statement/transaction data.** Given a
   user's actual current balance, minimum-due pattern, and the Banxico-published TEPP for no-totaleros
   (37.7% weighted, Dec-2024) or their own bank/segment's published rate, show a live, personalized
   payoff-time and total-interest projection, updated every statement cycle — and flag the 24.9% who are
   minimum-payment-only before it becomes chronic. Continuous data is what turns a one-time "you're a
   no-totalero" label into an ongoing trend line (is utilization rising cycle over cycle) that a static
   Banxico report cannot provide for an individual.

3. **Payroll/personal-loan CAT benchmark and refinance alert.** Ingest a user's actual payroll-loan or
   personal-loan contract rate (from transaction/loan-servicing data) and continuously compare it against
   the Banxico RIB Nómina/Personales bimonthly published distribution (e.g., "your rate is in the top
   quartile; the median for your loan size/term is X"), prompting a portability/refinance conversation.
   This directly operationalizes CAT-disclosure data that today sits in a static PDF nobody reads at the
   point of decision. Requires solving the (unverified) question of whether the comparador API is
   practically consumable, or building a periodic ETL off the published PDFs instead.

4. **Cross-provider BNPL + revolving-debt exposure aggregator.** If (and only if, pending verification)
   BNPL providers report to Círculo de Crédito/Buró de Crédito inconsistently or with a lag, a product
   that pulls live transaction data across bank accounts could reconstruct a user's *actual* current BNPL
   exposure across Kueski Pay, Aplazo, MercadoPago cuotas, etc. faster than the bureau does, giving an
   early over-indebtedness signal (relevant to the REDECO/collections pain point) before it surfaces as a
   delinquency. This hypothesis is the most speculative of the four and rests on an unverified premise
   about bureau-reporting completeness/timeliness that should be checked before committing engineering
   effort to it.

---

### Session notes / working files
- Primary Banxico PDFs were downloaded and parsed locally with `pdftotext` because `WebFetch` cannot read
  binary PDF content directly; the extracted text (and cached copies) is what several figures above are
  quoted from. Local scratch copies used: `/tmp/nomina2024.pdf`, `/tmp/tarjetas2024.pdf`,
  `/tmp/personales.pdf` (session-local, not part of the deliverable).
