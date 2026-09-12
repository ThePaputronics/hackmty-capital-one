# Mexico Opportunity Map: Continuous Financial Intelligence

**Evidence cutoff:** September 11, 2026  
**Purpose:** Product discovery for the HackMTY Capital One challenge; no product implementation is specified or implied.

## A. Executive recommendation and research scope

### Recommendation

Build a **pre-submission SPEI Intent & Recipient Guard** for authorized-push-payment (APP) scams and coercion. The narrow user moment is a genuine customer preparing an unusual transfer to a first-time or newly risky beneficiary while being manipulated by a scammer. The system combines payer behavior, session context, beneficiary history, and recipient-network signals; explains the risk; and offers reversible, user-controlled friction before the transfer enters SPEI.

This is stronger than a generic fraud detector because normal authentication can succeed when the customer is deceived. It is stronger than a generic financial coach because it has a precise event, a seconds-level intervention window, bounded actions, and measurable outcomes. It also best expresses the sponsor theme: continuous event flow, real-time scoring, agentic explanation, a visible guardrail, and human approval.

The two strongest backups are:

1. **Quincena Collision Guard** for salaried households: forecast payday-to-due-date shortfalls and propose reversible actions without issuing new credit.
2. **Cobro-30** for small B2B suppliers: combine CFDIs, payment complements, bank deposits, and obligations to predict 30-day liquidity and prioritize collections.

### Scope

This synthesis combines six Mexico research streams: retail investors, salaried households, PYMES and informal businesses, regional inclusion, consumer credit, and fraud/security. It evaluates opportunities across:

1. **Consumer Financial Autonomy & Credit Building**
2. **SMB Cash-Flow & Working-Capital Intelligence**
3. **Real-Time Anomaly & Security Sentinel**

The solution may serve consumers, businesses, banks, lenders, remittance providers, or payment institutions. The recommended prototype uses synthetic/public data and simulated actions; it does not assume a universal Mexican open-banking feed.

### Evidence rules

- **Fact** means a directly supported observation from the cited source. Official Mexican sources are preferred.
- **Hypothesis** means a product, behavioral, or causal proposition requiring user research or partner transaction data.
- **Anecdote** means an individual or vendor-reported experience that is not population evidence.
- Complaint counts are not treated as unique victims, confirmed fraud, attempted fraud, or successful loss unless the source explicitly says so.
- Correlations and group differences are not presented as causes.
- Conflicting denominators are kept separate. For example, ENIF product ownership, CONDUSEF complaints, bank claims, and ENVIPE victimization are not combined.
- Public laws authorizing data-sharing categories are not treated as proof that a universal production API exists.
- No community/forum anecdote is used in ranking. One ethnography is retained only as design context, not prevalence evidence.
- Any date, access condition, or production capability not established by the source is marked **TODO: Verify**.

---

## B. Mexico evidence baseline

### Verified facts

1. **Formal access is broader than active credit or formal saving.** In 2024, 76.5% of adults ages 18–70 had at least one formal financial product, 63.0% had a formal savings account, and 37.3% had formal credit. In the prior year, 36.6% saved only informally and 33.6% did not save. These categories describe product use and saving behavior, not credit-bureau file depth ([INEGI/CNBV, ENIF 2024, published 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

2. **Financial fragility is material.** In ENSAFI 2023, 30.5% of adults reported insufficient money to cover expenses; 27.3% of adults with debt reported falling behind on a loan or credit payment; and 35.9% said savings could cover an emergency equal to one month of income. These are self-reported adult estimates, not salaried-worker-only measures ([INEGI/CONDUSEF, ENSAFI 2023, published 2024](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf)).

3. **Payroll is a useful but incomplete entry point.** ENIF 2024 found that 36.2% of adults had a payroll or pension account and that payroll was the first formal account for 46.5% of people who had ever held one ([INEGI/CNBV, 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

4. **Irregular income is not an edge case.** In July 2026, 56.2% of employed people were in labor informality and 13.6 million people worked independently or on their own account. Informality is not equivalent to being unbanked or risky, but it makes fixed-payday assumptions incomplete ([INEGI, ENOE July 2026, published 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf)).

5. **Regional and cash-use gaps are large.** In Mexico's South region, 67.7% of adults had any formal product, 55.5% an account, and 29.9% credit. For purchases above MXN 500, 82.0% usually used cash, and only 29.8% believed all or almost all businesses accepted cards or transfers ([INEGI/CNBV, ENIF 2024, published 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

6. **Connectivity is improving but uneven.** Internet use in 2025 was 88.9% in urban areas and 75.2% in rural areas; household internet access was 90.5% in Mexico City, 64.0% in Oaxaca, and 53.9% in Chiapas. These figures do not measure connection reliability, device sharing, or financial-app usability ([INEGI, ENDUTIH 2025, published 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf)).

7. **Remittances create a distinctive digital-to-cash journey.** Mexico received USD 61.791 billion in remittances in 2025. Electronic transfers represented 99.1% of value, but 49.6% of electronically sent remittances were paid out in cash. Aggregate flows do not identify recipient demographics, control of funds, or retention behavior ([Banco de México, 2025 remittances, published 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf)).

8. **Microbusinesses dominate the establishment base.** Of 5,468,180 establishments covered by the 2024 Economic Census, 95.4% had 0–10 workers. A separate census classification found 64.3% of covered establishments informal; this is not the same denominator or definition as informal employment ([INEGI, Economic Censuses 2024 definitive report, updated 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf); [INEGI, national minimonograph, 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/ce2024_mn00.pdf)).

9. **Business churn is high, but its cause is not established.** INEGI estimated 1.7 million MIPYME establishment births and 1.4 million deaths between May 2019 and May 2023 in covered urban sectors. The study does not attribute deaths to liquidity, late payment, or any single cause ([INEGI, EDN 2023, published 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf)).

10. **Late B2B payment is observable, though the best recent measure is commercial.** Atradius reported that 48% of surveyed Mexican B2B invoices were overdue, payment averaged 38 days after the due date, and bad debt equaled 6% of B2B credit sales. This is a commercial survey, not a census of all PYMES ([Atradius, Mexico Payment Practices 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024)).

11. **Mexico's CFDI system exposes invoice-payment state.** Payment Complement 2.0 is mandatory for relevant partial or deferred payments and is designed to show whether an invoice has been paid, creating a Mexico-specific receivables signal ([SAT, Payment Complement, mandatory since 2023; page current through the cutoff](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm)).

12. **SPEI is ubiquitous and fast.** In 2025, SPEI processed 7,308.1 million transfers; 7,302.4 million were user transactions, 94.6% of user transactions were at or below 1,500 UDIS, and approximately 82.9 million individuals participated in at least one SPEI transfer in Q4 2025. Volume and participation are not fraud measures ([Banco de México, 2025 Financial Market Infrastructures Report, published September 11, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)).

13. **Fraud is material, but official measures answer different questions.** ENVIPE estimated 8,290 fraud incidents per 100,000 adults in 2025, combining bank and consumer fraud and counting incidents rather than unique victims ([INEGI, ENVIPE 2026](https://www.inegi.org.mx/contenidos/programas/envipe/2026/doc/envipe2026_presentacion_nacional.pdf)). Separately, CONDUSEF received 37,582 “possible fraud” matters in January–June 2025, including 7,045 unrecognized electronic-transfer complaints; those are complaints, not confirmed frauds, attempts, or unique victims ([CONDUSEF, H1 2025 self-evaluation report](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)).

14. **APP scams are a measurement blind spot.** CONDUSEF's unrecognized-operation categories and Banco de México's Rule 43 collaboration mechanism focus principally on transactions the customer says they did not request. A customer who personally authenticates a transfer while deceived may not fit that framing ([CONDUSEF, 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf); [Banco de México, Circular 14/2017 compiled through 2026](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf)).

15. **Transaction data can improve no-score lending in a specific Mexican sample.** A 2026 study of RappiCard applicants lacking a conventional bureau score reported AUC 0.791 for its benchmark model; removing transaction data reduced AUC by 0.137. This is strong evidence for that lender/sample, not a national estimate or permission for automated denial ([Chioda, Gertler, Higgins and Medina, 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf)).

16. **Data access and privacy constrain every opportunity.** Article 76 of the Fintech Law recognizes categories including transactional data and requires express customer authorization for sharing, but it does not prove universal production connectivity ([Cámara de Diputados, Fintech Law, current through 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf)). Financial and patrimonial data generally require express consent under Mexico's private-sector data-protection law ([Cámara de Diputados, LFPDPPP, enacted 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)).

### Hypotheses requiring validation

- Combining payer-intent and recipient-network signals can identify APP scams at a sufficiently low intervention rate to be acceptable.
- Forecasting the lowest balance before the next payroll deposit will prevent more arrears than retrospective budgeting.
- CFDI/payment-complement state plus bank deposits can predict B2B collection timing better than invoice due date alone.
- Conservative, volatility-aware micro-savings can grow emergency buffers without causing missed essential payments.
- A portable cash-flow evidence passport can preserve some predictive value of proprietary platform data while remaining explainable and fair.

### Anecdotes and qualitative evidence

No forum, Reddit, Facebook, TikTok, or other community anecdotes are used. A one-community Oaxaca ethnography is relevant only as a warning not to treat women receiving remittances as passive users or to override household/community practices; it is not used for prevalence or ranking ([Smyth, University of Kentucky dissertation, 2022](https://uknowledge.uky.edu/geography_etds/83/)).

---

## C. Ranked opportunity map

### 1. SPEI Intent & Recipient Guard

- **Primary user segment:** Bank or wallet customer sending an unusual SPEI transfer to a first-time beneficiary.
- **Relevant challenge track:** Real-Time Anomaly & Security Sentinel.
- **Specific Mexican pain point:** SPEI settles rapidly, while a genuine customer under social engineering may pass authentication. Existing unauthorized-transfer categories do not cleanly capture manipulated-but-authenticated intent.
- **Evidence/citations:** SPEI scale and rapid operating rules are documented by [Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf) and [Circular 14/2017](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf). CONDUSEF complaint categories show substantial unauthorized-payment harm but an APP measurement gap ([CONDUSEF, 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)).
- **Why it matters:** The most useful intervention is before submission; after settlement, recovery cannot be promised.
- **Existing alternatives and limitations:** Authentication, device risk, transaction limits, alerts, CONDUSEF warnings, SIPRES, and interbank assistance address identity, amount, education, or unauthorized payments. They do not necessarily test whether an authenticated user is acting under deception.
- **Proposed product direction:** Produce separate `account takeover`, `payer intent`, and `recipient network` scores, then intervene only when multiple signals reinforce one another.
- **Continuous transaction/behavioral data used:** Amount as a share of balance, first-seen beneficiary, transfer history, beneficiary-creation time, session/device continuity, coarse active-call or remote-access indicator with permission, and recipient fan-in/fan-out risk.
- **Potential agentic/automated actions:** Explain the anomaly; ask a scam-specific question; offer verified-bank callback, step-up authentication, or a user-selected cooling pause; assemble an analyst case. Never submit, cancel, reverse, freeze, blacklist, or report automatically.
- **Responsible-AI, privacy, security and regulatory considerations:** Do not capture call audio, messages, contacts, clipboard contents, or screenshots. Use purpose limitation, short retention, reason codes, subgroup false-positive testing, appeal, and human override. Any hold or cross-bank sharing requires institution-specific authority.
- **Hackathon feasibility:** **High.** Stream synthetic payer/session/beneficiary/recipient-graph events through transparent rules plus an interpretable model.
- **Differentiation from common fintech ideas:** It asks “is the authenticated customer being manipulated?” rather than “is this the customer?” and couples payer intent to recipient graph risk.
- **Demo potential and measurable impact:** Show a legitimate unusual transfer proceeding and a coerced first-time transfer receiving targeted friction. Primary metric: value-weighted APP recall at a fixed genuine-payment challenge rate; also show latency and false-positive rate.
- **Evidence label:** The intervention design is a **hypothesis**; the payment scale, speed, and official measurement gap are **facts**.

### 2. Quincena Collision Guard

- **Primary user segment:** Salaried workers and households paid weekly or at intervals up to 15 days.
- **Relevant challenge track:** Consumer Financial Autonomy & Credit Building.
- **Specific Mexican pain point:** Bills, card payments, payroll-loan debits, and household transfers can collide before the next deposit even when monthly income appears sufficient.
- **Evidence/citations:** National adult fragility and arrears are documented by [INEGI/CONDUSEF, ENSAFI 2023](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf); payroll-account reach by [INEGI/CNBV, ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf); and payroll-loan direct-debit structure and 2024 loan indicators by [Banco de México](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf).
- **Why it matters:** Preventing a late payment or emergency loan is more actionable than showing a retrospective spending chart.
- **Existing alternatives and limitations:** Bank alerts are reactive; BBVA Apartados separates funds manually; earned-wage-access products provide liquidity but can shift the shortfall into the next pay cycle ([BBVA México, date not displayed](https://www.bbva.mx/personas/productos/cuentas/apartados.html); [Minu, date not displayed](https://www.minu.mx/salario-on-demand)).
- **Proposed product direction:** Forecast the minimum safe balance through the next two paydays and explain the exact obligations producing a deficit.
- **Continuous transaction/behavioral data used:** Payroll deposits, balance, recurring debits, due dates, loan installments, card minimums, household transfers, and optional cash obligations.
- **Potential agentic/automated actions:** Reserve funds in a bucket, draft a due-date-change request, propose pausing a nonessential recurring payment, or schedule a reminder. Any transfer, cancellation, or creditor contact requires approval.
- **Responsible-AI, privacy, security and regulatory considerations:** Display uncertainty; never guarantee payroll timing; do not sell credit through a fear-based nudge; do not initiate borrowing; use explicit consent and revocable access.
- **Hackathon feasibility:** **Very high.** Synthetic payroll, bill, loan, medical-shock, and duplicate-debit events are sufficient.
- **Differentiation from common fintech ideas:** Forward-looking collision prevention tied to Mexican pay cadence, not generic budgeting or another cash advance.
- **Demo potential and measurable impact:** Detect a labeled shortfall 3–7 days early and show a reversible intervention that removes it. Metrics: shortfall recall, false-alert rate, forecast error, and simulated late fees or penalty interest avoided.
- **Evidence label:** Fragility and payroll access are **facts**; the prevalence of payday-specific collisions and intervention effect are **hypotheses**.

### 3. Cobro-30: CFDI Receivables-to-Runway Copilot

- **Primary user segment:** Formal or transitioning-to-formal B2B suppliers with recurring customers, banked collections, and limited treasury staff.
- **Relevant challenge track:** SMB Cash-Flow & Working-Capital Intelligence.
- **Specific Mexican pain point:** Invoice due dates do not equal cash receipt dates, while payroll, suppliers, rent, tax, and debt create dated obligations.
- **Evidence/citations:** Microbusiness scale and churn come from [INEGI Economic Censuses 2024](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf) and [EDN 2023](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf). Late-payment estimates come from [Atradius, 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024). Structured payment state comes from [SAT's Payment Complement](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm).
- **Why it matters:** A dated warning can trigger collection or rescheduling before a business automatically reaches for expensive financing.
- **Existing alternatives and limitations:** NAFIN documents its Cadenas Productivas offering, but this research did not verify feature coverage across accounting and treasury products. **Hypothesis:** target users lack one action queue spanning collection, dispute resolution, rescheduling, and financing. **TODO: Verify** current competitor capabilities ([NAFIN](https://nafin.com/portalnf/content/cadenas-productivas/cadenas_productivas.html)).
- **Proposed product direction:** Match CFDIs and payment complements to deposits, estimate receipt windows, and forecast a daily 30-day cash-balance distribution.
- **Continuous transaction/behavioral data used:** CFDI XML, PUE/PPD status, payment complements, cancellations, bank deposits, invoice due dates, payer history, payroll, rent, suppliers, debt, and tax dates.
- **Potential agentic/automated actions:** Draft an invoice-specific collection reminder; produce a dispute checklist; simulate early-payment discounts; compare factoring with non-debt actions; prepare supplier-rescheduling language. Human approval is mandatory.
- **Responsible-AI, privacy, security and regulatory considerations:** Never store a taxpayer's raw e.firma private key. A late invoice is not fraud. Show prediction intervals and provenance; disclose financing referral conflicts; prohibit autonomous financing or customer contact.
- **Hackathon feasibility:** **High.** Use synthetic CFDIs, complements, deposits, and obligations; no live SAT credentials are required.
- **Differentiation from common fintech ideas:** Mexico-specific invoice-payment state plus a forward action queue, rather than a generic SMB dashboard or loan offer.
- **Demo potential and measurable impact:** Predict the first negative-cash day, match deposits to invoices, and show which approved action removes the gap. Metrics: payment-date error, seven-day shortfall recall, match rate, and projected shortfall days avoided.
- **Evidence label:** Late-payment and CFDI mechanics are **facts**; payment prediction performance is a **hypothesis**.

### 4. Volatility-Aware Emergency-Buffer Autopilot

- **Primary user segment:** Informal, gig, independent, or seasonally paid workers who have an account but do not save formally and consistently.
- **Relevant challenge track:** Consumer Financial Autonomy & Credit Building.
- **Specific Mexican pain point:** Fixed recurring transfers assume stable income and complete digital visibility, while many workers have variable deposits and cash-heavy spending.
- **Evidence/citations:** Labor informality and self-employment are measured by [INEGI, ENOE July 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf). Saving-method and cash-use distributions come from [INEGI/CNBV, ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf).
- **Why it matters:** The product can build resilience without extending credit, provided it never creates a missed essential payment.
- **Existing alternatives and limitations:** Fixed recurring savings and card round-ups do not adapt to income volatility or unobserved cash. Cetesdirecto supports recurring saving but is not a cash-flow affordability engine ([Cetesdirecto](https://www.cetesdirecto.com/sites/portal/invertir-en-cetes.ahorro-recurrente)).
- **Proposed product direction:** Continuously estimate a conservative “safe to save today” amount, protected balance, emergency-buffer days, and missing-cash confidence.
- **Continuous transaction/behavioral data used:** Deposits, SPEI receipts, platform payouts, cash deposits, ATM withdrawals, essentials, debt payments, and optional cash-income/obligation entries.
- **Potential agentic/automated actions:** Propose or execute a capped, reversible micro-sweep under explicit standing consent; pause before low-cash periods; return funds if a critical bill becomes endangered; ask for confirmation when cash visibility drops.
- **Responsible-AI, privacy, security and regulatory considerations:** Default to the lower forecast bound, provide one-tap pause and immediate reversal, never create overdraft or lock essential funds, and distinguish insured deposits from investments.
- **Hackathon feasibility:** **Very high.** Fully synthetic irregular-income streams are sufficient.
- **Differentiation from common fintech ideas:** The agent sometimes decides **not** to save and explains why; it is not a round-up feature or fixed monthly target.
- **Demo potential and measurable impact:** Compare 90 simulated days with fixed recurring saving. Metrics: buffer growth, missed critical payments, sweeps causing negative balance (target zero), and forecast-interval coverage.
- **Evidence label:** Segment scale is a **fact**; improved retained savings is a **hypothesis**.

### 5. RemesaGuard Sur

- **Primary user segment:** Rural and small-locality remittance recipients in the South and Center-South/East, especially older adults and users needing accessible or low-connectivity interaction.
- **Relevant challenge track:** Real-Time Anomaly & Security Sentinel.
- **Specific Mexican pain point:** Digitally transmitted remittances frequently convert to cash in regions with lower product use and connectivity; generic always-online card-fraud UX does not fit this journey.
- **Evidence/citations:** Remittance volume and cash payout are from [Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf); regional financial behavior from [ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf); connectivity from [ENDUTIH 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf); and accessibility barriers from [CNBV/GIZ, 2023](https://www.gob.mx/cnbv/articulos/inclusion-financiera-de-las-personas-con-discapacidad?idiom=es).
- **Why it matters:** A loss immediately after remittance receipt may remove funds intended for food, health, or household obligations.
- **Existing alternatives and limitations:** Remittance providers, banks, Banco del Bienestar, and fraud education move or protect money within their own channels, but do not necessarily provide an accessible, cash-out-aware, offline-capable behavioral sentinel.
- **Proposed product direction:** Learn remittance cadence and flag an unusual transfer or withdrawal combination without treating cash use, rurality, age, or disability as suspicious.
- **Continuous transaction/behavioral data used:** Remittance deposits, cash withdrawals, new beneficiaries, transfer velocity, amount relative to recent remittance, connectivity state, and user-confirmed expected cash-out.
- **Potential agentic/automated actions:** Explain the anomaly; offer confirm, reduce, pause, verified callback, or in-person verification. Cache the decision locally when offline and synchronize minimal data later.
- **Responsible-AI, privacy, security and regulatory considerations:** Never require a family member or trusted contact; coercion may come from the household. Test false positives by sex, age, rurality, disability, language, and connectivity. Do not block based on geography or cash behavior.
- **Hackathon feasibility:** **High.** Synthetic remittance/cash-out events plus an offline queue and accessible UI are enough.
- **Differentiation from common fintech ideas:** Remittance cadence, digital-to-cash behavior, accessibility, and intermittent connectivity—not a generic fraud alert.
- **Demo potential and measurable impact:** Stop a simulated scam transfer while allowing a legitimate medical transfer. Metrics: prevented loss per 1,000 alerts, subgroup false-positive ceiling, offline decision latency, and successful recovery-flow completion.
- **Evidence label:** Regional, remittance, and access patterns are **facts**; predictive usefulness of cadence is a **hypothesis**.

### 6. Dimo Rebinding and First-Transfer Guard

- **Primary user segment:** Dimo users sending to a phone number shortly after a phone-to-account relink, device change, or authentication reset.
- **Relevant challenge track:** Real-Time Anomaly & Security Sentinel.
- **Specific Mexican pain point:** Phone-number-addressed transfers create a narrow identity-binding risk around relinking and the first subsequent payment.
- **Evidence/citations:** Banco de México reported 16.4 million registered Dimo users and 3.1 million inter-institution transfers totaling MXN 3.7 billion in 2025; those usage figures do not establish a fraud rate ([Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)).
- **Why it matters:** The state transition creates a precise intervention point before the first material transfer after a changed binding.
- **Existing alternatives and limitations:** Dimo displays recipient initials and requires enrollment consent, but public evidence does not establish a dedicated cross-event rebinding sentinel ([Banco de México, 2024 infrastructure report, published 2025](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BE0085475-B1D7-DED0-60AF-05ED88153BDC%7D.pdf)).
- **Proposed product direction:** Use a transparent state machine: stable → rebind → new-device confirmation → first inbound/outbound transfer → burst.
- **Continuous transaction/behavioral data used:** Link/unlink/relink events, time since relink, device/authentication change, recipient initials confirmation, sender-recipient history, amount, and receipt burst.
- **Potential agentic/automated actions:** Require out-of-band confirmation on the previously trusted channel, emphasize recipient initials, or propose a cooling period for a high-risk first transfer.
- **Responsible-AI, privacy, security and regulatory considerations:** Do not treat number portability or device replacement as fraud; do not ingest address books; provide lost-phone recovery; disclose data used.
- **Hackathon feasibility:** **High.** A state machine and synthetic transition stream are simple and visually clear.
- **Differentiation from common fintech ideas:** A Mexico-specific identity-binding sequence rather than generic account-takeover scoring.
- **Demo potential and measurable impact:** Show legitimate phone replacement and malicious relink side by side. Metric: injected redirect attacks stopped before first transfer at a fixed false-challenge rate.
- **Evidence label:** Dimo usage is a **fact**; fraud prevalence and detector value are **unknown hypotheses**.

### 7. IVA Guard: Safe-to-Spend and Tax-Reserve Assistant

- **Primary user segment:** RESICO/personas físicas and small service merchants with mixed cash, SPEI, POS, and invoiced sales.
- **Relevant challenge track:** SMB Cash-Flow & Working-Capital Intelligence.
- **Specific Mexican pain point:** Booked sales, collected cash, payment complements, creditable IVA, retentions, and upcoming obligations create a misleading bank balance and tax-date risk.
- **Evidence/citations:** CFDI payment-state mechanics come from [SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm). IVA collection and monthly-payment rules are in the [Ley del Impuesto al Valor Agregado](https://www.diputados.gob.mx/LeyesBiblio/pdf_mov/Ley_del_Impuesto_al_Valor_Agregado.pdf); the exact taxpayer treatment depends on regime and transaction.
- **Why it matters:** A “safe to spend” figure can prevent the business from consuming funds likely needed for tax and essential operating obligations.
- **Existing alternatives and limitations:** SAT tools and accounting software support compliance and records but do not necessarily provide a continuous, uncertainty-aware liquidity guardrail.
- **Proposed product direction:** Estimate a range for IVA obligations and separate booked revenue from collected cash while reserving payroll, rent, and a user-defined buffer.
- **Continuous transaction/behavioral data used:** Bank deposits, SPEI/CoDi, POS settlements, user-entered cash close, issued/received CFDIs, payment complements, known deductions/retentions, and deadline calendar.
- **Potential agentic/automated actions:** Recommend a reserve amount, draft a missing-complement task, generate an accountant-ready reconciliation, and remind before deadlines. Never file, cancel a CFDI, classify uncertain tax items, or transfer funds without approval.
- **Responsible-AI, privacy, security and regulatory considerations:** Clearly state that estimates are not a return or legal opinion; separate verified and user-entered data; require accountant review for classifications; never encourage unreported cash sales.
- **Hackathon feasibility:** **High.** Official schemas and a labeled synthetic ledger are sufficient.
- **Differentiation from common fintech ideas:** Mexico-specific cash-basis IVA and payment-complement status integrated with liquidity, not a generic bookkeeping dashboard.
- **Demo potential and measurable impact:** Metrics: projected-liability error on synthetic ground truth, missing-complement detection, and tax-date deficits avoided.
- **Evidence label:** Tax and CFDI rules are **facts**; market demand and estimate accuracy are **hypotheses**.

### 8. Net-Pay & Deduction Integrity Agent

- **Primary user segment:** Salaried workers with variable deductions, payroll loans, overtime, commissions, or suspected net-pay discrepancies.
- **Relevant challenge track:** Consumer Financial Autonomy & Credit Building, with a Security Sentinel crossover.
- **Specific Mexican pain point:** Payroll CFDI, expected compensation, bank deposit, and loan debits can disagree, but workers must reconcile them manually.
- **Evidence/citations:** Mexican labor law gives workers rights to detailed pay concepts and deductions and limits permissible deductions by category ([Cámara de Diputados, Federal Labor Law, current through 2026](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf)). Payroll loans are commonly debited from payroll accounts ([Banco de México, payroll-credit indicators, data through 2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf)).
- **Why it matters:** A factual discrepancy package reduces cognitive and administrative burden and can distinguish cash-flow stress from an unexplained deduction.
- **Existing alternatives and limitations:** Payroll portals, bank statements, HR, PROFEDET, lenders, and CONDUSEF each hold a piece of the workflow; the user performs the reconciliation.
- **Proposed product direction:** Reconcile gross pay → taxes/statutory deductions → voluntary/loan deductions → expected net pay → deposited net pay.
- **Continuous transaction/behavioral data used:** Payroll CFDI XML/PDF, historical net pay, expected terms, bank deposits, payroll-loan schedules, and account debits.
- **Potential agentic/automated actions:** Highlight material unexplained differences, draft a factual HR/payroll inquiry, create a discrepancy timeline, and route the user to the appropriate official or lender channel. Never contact an employer without approval.
- **Responsible-AI, privacy, security and regulatory considerations:** Payroll files expose income, employer, RFC, and other identifiers. Minimize retention, redact identifiers from model prompts, and label findings “unexplained” rather than “fraud” until verified.
- **Hackathon feasibility:** **High.** Synthetic payroll CFDIs and bank entries can include missing overtime, duplicate deductions, delays, and legitimate tax adjustments.
- **Differentiation from common fintech ideas:** Document-to-deposit reconciliation and recourse, not budget categorization.
- **Demo potential and measurable impact:** Metrics: discrepancy precision/recall, reconciliation time, traceable-source coverage, and zero unsupported fraud accusations.
- **Evidence label:** Legal and payroll-debit mechanics are **facts**; discrepancy prevalence is **unknown**.

### 9. Cash-Flow Evidence Passport for No-Score Applicants

- **Primary user segment:** New-to-credit or no-score applicants with consented bank, wallet, platform, or commerce transaction history.
- **Relevant challenge track:** Consumer Financial Autonomy & Credit Building.
- **Specific Mexican pain point:** Active formal credit reaches only part of the adult population, while conventional bureau depth may be insufficient even when transaction history is informative. The national no-file/thin-file population is unknown.
- **Evidence/citations:** Product and credit ownership come from [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/enif2024_RR.pdf). The predictive value of platform transactions for one Mexican lender/sample comes from [Chioda et al., 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf).
- **Why it matters:** Portable, explainable evidence could help a consumer reach human-reviewed prequalification without invasive social or device surveillance.
- **Existing alternatives and limitations:** Credit bureaus and accessible-card issuers already serve parts of the market; proprietary alternative-data models keep evidence inside one platform and can be opaque.
- **Proposed product direction:** Produce income regularity, concentration, essential-payment consistency, residual-cash-flow range, data sufficiency, uncertainty, and reason codes—not a universal “worthiness” score.
- **Continuous transaction/behavioral data used:** Consented deposits, SPEI receipts, platform payouts, utilities, rent proxies, food/transport, cash-deposit events, and optional verified commerce history. Exclude contacts, messages, social graphs, precise location, and device price.
- **Potential agentic/automated actions:** Wait for sufficient evidence, request only material missing data, simulate a small safe limit and aligned due date, and send borderline/adverse cases to human review. No automated denial.
- **Responsible-AI, privacy, security and regulatory considerations:** Highest-risk consumer opportunity. Test calibration and error by sex, locality, rurality, disability, and other relevant groups; prevent proxy discrimination; provide correction, deletion, revocation, appeal, and purpose-limited sharing.
- **Hackathon feasibility:** **Medium-high** for a transparent synthetic demonstration; low for claiming production underwriting validity.
- **Differentiation from common fintech ideas:** User-controlled evidence portability and a data-sufficiency gate, not opaque alternative scoring.
- **Demo potential and measurable impact:** On explicitly synthetic labels, report model lift over a transaction-free baseline, calibration, approval at fixed simulated delinquency, subgroup gaps, and reason-code stability. Do not claim real credit performance.
- **Evidence label:** The single-lender study is a **fact** for its sample; national generalizability and lender acceptance are **hypotheses**.

### 10. ReconcileMX: Multi-Rail Settlement and Leakage Monitor

- **Primary user segment:** Small retailers and service businesses using two or more POS, wallet, marketplace, SPEI/CoDi, and cash rails.
- **Relevant challenge track:** SMB Cash-Flow & Working-Capital Intelligence, with a Security Sentinel crossover.
- **Specific Mexican pain point:** Sales, fees, holds, refunds, chargebacks, cash closes, and bank deposits are fragmented; the problem is reconciliation and available-cash visibility, not a blanket claim that all digital rails settle slowly.
- **Evidence/citations:** The Economic Census found cash, transfers, and cards all used by businesses, with multiple answers permitted ([INEGI, CE 2024 payment methods](https://inegi.org.mx/contenidos/programas/ce/2024/doc/ro_infmpn_ce24.pdf)). SPEI and CoDi operating characteristics are documented by [Banco de México](https://www.banxico.org.mx/services/spei_-transfers-banco-mexico.html) and [CoDi](https://www.banxico.org.mx/sistemas-de-pago/codi-cobro-digital-banco-me.html).
- **Why it matters:** Missing or short settlements directly distort today's available cash and tomorrow's ability to pay suppliers or payroll.
- **Existing alternatives and limitations:** Clip and Mercado Pago document provider offerings, but their cited pages do not establish the absence of cross-provider functionality. **Hypothesis:** cross-provider, cash-inclusive matching remains unmet. **TODO: Verify** current exports, APIs, and competitor coverage ([Clip](https://www.clip.mx/soluciones); [Mercado Pago](https://www.mercadopago.com.mx/blog/mercado-pago-para-negocios)).
- **Proposed product direction:** Forecast expected net settlement by provider and surface unmatched sales, short deposits, duplicate refunds, unexpected fees, or cash-close variance.
- **Continuous transaction/behavioral data used:** POS/acquirer sales, fees, refunds, chargebacks, wallet balances, SPEI/CoDi receipts, bank deposits, cash close, and CFDIs where available.
- **Potential agentic/automated actions:** Assemble an evidence packet, draft provider support messages, and prompt the owner to resolve a cash variance. Do not autonomously charge back, freeze, or accuse.
- **Responsible-AI, privacy, security and regulatory considerations:** Tokenize card references; never retain PAN/CVV; label events “needs review”; require human approval before provider/customer contact; distinguish provider settlement from Banxico rail timing.
- **Hackathon feasibility:** **Medium-high.** CSV and synthetic feeds can produce a credible demo without live provider APIs.
- **Differentiation from common fintech ideas:** Cross-rail available-cash intelligence and evidence packaging, not another sales dashboard.
- **Demo potential and measurable impact:** Metrics: settlement-match rate, anomaly precision/recall, dispute-packet preparation time, and simulated pesos of leakage detected.
- **Evidence label:** Mixed-rail use is a **fact**; prevalence of settlement errors and product adoption are **unknown**.

---

## D. Transparent scoring matrix

### Scale and method

Every criterion has equal weight because the challenge requires both problem quality and demonstrability, and no verified judging weights were available. Each opportunity receives **1–5 points** on nine criteria, for a maximum of **45**:

- **1:** weak, absent, or materially constrained
- **2:** below average; major evidence, safety, or feasibility gap
- **3:** credible but mixed
- **4:** strong
- **5:** exceptional and directly supported

**Scoring protocol:** Each score must cite the evidence supporting it and apply the
criterion-specific interpretation above. A score of **5** for Evidence requires direct
evidence for the opportunity's narrow pain point, not only evidence for the broader
population or problem area. Equal totals are resolved, in order, by Evidence strength,
Safety/privacy/regulatory feasibility, Real-time data-to-output demonstration, and
Mexico-specific data advantage. If all tie-breakers remain equal, opportunities retain
the same rank rather than being forced into an unsupported order.

Criteria:

1. **Magnitude/urgency**
2. **Evidence strength**
3. **Affected population**
4. **Challenge-track relevance**
5. **Differentiation**
6. **Real-time data-to-output demonstration**
7. **Technical feasibility with synthetic/public data**
8. **Safety/privacy/regulatory feasibility**
9. **Scalability**

| Rank | Opportunity | Mag. | Evidence | Population | Track | Diff. | Real-time demo | Tech | Safety | Scale | Total /45 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | SPEI Intent & Recipient Guard | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **43** |
| 2 | Quincena Collision Guard | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | **41** |
| 3 | Cobro-30 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | **41** |
| 4 | Volatility-Aware Buffer Autopilot | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | **41** |
| 5 | RemesaGuard Sur | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | **39** |
| 6 | Dimo Rebinding Guard | 3 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | **38** |
| 7 | IVA Guard | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 4 | **38** |
| 8 | Net-Pay & Deduction Integrity | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | **37** |
| 9 | Cash-Flow Evidence Passport | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 5 | **37** |
| 10 | ReconcileMX | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 4 | **36** |

### Score uncertainty

- Scores are ordinal judgments, not measured market values. A one-point difference is not decisive.
- APP scam evidence is strong on payment scale, fraud context, and the pre-transfer logic, but weak on nationwide APP incidence and public ground truth; its evidence score is therefore 4, not 5.
- Quincena Guard has strong population evidence, but payday-specific collision prevalence has not been measured directly; its Evidence score is therefore 4, not 5.
- Cobro-30's actionability is strong because CFDI/payment complements exist, but the best recent B2B lateness estimate is commercial and not representative of all PYMES.
- Quincena Guard, Cobro-30, and the Volatility-Aware Buffer Autopilot tie at 41. Quincena is placed second because its safety score is 5; Cobro-30 is placed third because its differentiation score is 5 versus 4 for the buffer autopilot. These are documented tie-breaks, not evidence of meaningful one-point superiority.
- Dimo Rebinding Guard and IVA Guard tie at 38. Dimo is placed sixth because its real-time demonstration score and safety score are higher.
- Net-Pay & Deduction Integrity and Cash-Flow Evidence Passport tie at 37. Net-Pay is placed eighth because its safety score is higher.
- Cash-Flow Evidence Passport scores poorly on safety feasibility because a hackathon cannot validate production underwriting fairness or regulatory compliance.
- RemesaGuard's affected-population score is 3 because aggregate remittance data do not identify the narrower accessible/rural recipient beachhead.
- A verified hackathon rubric, partner data access, and five to ten target-user interviews could change ranks by several points. **TODO: Verify** official judging weights and available sandbox data before implementation.

---

## E. Three strongest niches and tradeoffs

### 1. First choice: SPEI Intent & Recipient Guard

**Why it wins:** It has the clearest continuous event stream, the shortest and most valuable intervention window, a highly visible guardrail, and a narrow failure mode that existing authentication can miss. It can be demonstrated credibly with synthetic data without claiming that a hackathon model is production-ready.

**Tradeoffs:** Public Mexican data do not isolate APP scams, unique victims, successful loss, or recovery. Recipient-network data would require an institutional partner. False positives could delay essential payments. The MVP must therefore demonstrate targeted, reversible friction—not account blocking—and report the challenge rate as prominently as detection.

### 2. Consumer backup: Quincena Collision Guard

**Why it is strong:** Official evidence for insufficient liquidity, arrears, limited emergency cover, and payroll-account reach is stronger than the prevalence evidence for most consumer-fintech concepts. The prototype is easy to understand and can measure shortfall prevention without extending credit.

**Tradeoffs:** The research did not verify a broad Mexican “spend immediately after payday” effect among salaried workers. The thesis must remain timing mismatch plus shocks, not behavioral blame. It is less novel than APP intent detection unless payroll CFDI/deduction reconciliation is included.

### 3. B2B backup: Cobro-30

**Why it is strong:** It has the most Mexico-specific data advantage in the SMB track: CFDIs and payment complements expose invoice and collection state. It also supports multiple bounded actions before financing and creates a direct business metric.

**Tradeoffs:** It intentionally excludes many cash-only informal firms. Commercial late-payment evidence is less representative than national household surveys. Production ingestion, authentication, payer-specific history, and credential handling require partner validation.

### Retail-investor disposition

Investor-specific concepts were reviewed but were not separately ranked. The research
found that an investment-scam transfer guard was the only strong track fit, and that
scenario is subsumed by the **SPEI Intent & Recipient Guard**. Suitability assessment,
personalized securities recommendations, portfolio management, and trading remain out
of scope pending **TODO: Verify** of licensing, suitability, recordkeeping, and
broker-integration requirements.

### Explicit comparison of the three named candidates

| Candidate | Evidence assessment | Stronger than alternatives? | Decision |
|---|---|---|---|
| **APP scam/coercion sentinel** | Strong evidence for SPEI scale, speed, broader fraud harm, impersonation/social engineering, and an authorization-versus-intent gap; no national APP prevalence or public labels. | **Yes, overall.** Stronger than generic ATO, card anomaly, merchant drift, or investment-only scam tools because it addresses a distinct control gap at a precise intervention moment. | **First choice**, narrowly scoped to first-time/newly risky SPEI beneficiaries and reversible pre-submission friction. |
| **Quincena-aware cash-flow autopilot** | Strong official evidence for fragility, arrears, emergency-savings limits, payroll-account reach, and payroll-loan debits; no direct estimate of payday-collision frequency. | **Yes, for Track 1.** Stronger than subscription detection, generic budgeting, annual aguinaldo planning, or a general coach. The opportunity becomes more defensible when framed as collision forecasting rather than presumed overspending. | **Best consumer backup.** |
| **PYME tax/payables/liquidity sentinel** | Strong official evidence for microbusiness scale and CFDI/tax mechanics; medium evidence for late B2B payment; no verified national “30 days of cash” statistic. | **Yes, for Track 2, if narrowed to receivables.** Cobro-30 is stronger than an all-purpose tax/payables/liquidity sentinel because receivable state and action are clearer. IVA Guard is a module or second product, not the initial wedge. | **Best B2B backup: Cobro-30 first; tax reserve later.** |

The ranking is evidence-based rather than an assumption that fraud is always the largest problem. Quincena Guard has the strongest direct household evidence, and Cobro-30 has the strongest Mexico-specific B2B data structure. The APP sentinel still ranks first because urgency, track fit, intervention timing, differentiation, and demo clarity offset its weaker prevalence measurement.

---

## F. Final decision

1. **Recommended niche and first-choice rationale:** Build a pre-submission **SPEI Intent & Recipient Guard** for APP scams/coercion involving first-time or newly risky beneficiaries; it is narrow, real-time, differentiated from authentication, and supports a measurable human-controlled intervention.
2. **Two credible backup niches:** **Quincena Collision Guard** for salaried households and **Cobro-30** for small B2B suppliers.
3. **Target user and core problem statement:** A Mexican bank or wallet customer is about to authenticate an unusual SPEI transfer to a new beneficiary while being deceived; normal identity checks may pass, and settlement can occur before a generic warning helps.
4. **One-sentence product thesis:** Combining payer-intent anomalies with recipient-network risk can trigger a specific, reversible warning before SPEI submission while allowing unusual legitimate payments to proceed.
5. **Minimum viable prototype:** A synthetic event generator, streaming risk service with separate ATO/intent/recipient scores, explanation and policy guardrail, live confirmation UI, simulated verified callback/cooling pause, and audit/fairness dashboard.
6. **Data stream, real-time outputs, automated actions:** Stream payer history, session/device continuity, amount/balance share, beneficiary age, entry behavior, coarse permissioned call/remote-access state, and synthetic recipient graph; output risk type, reasons, latency, and recommended friction; automate only explanation, step-up orchestration, and case preparation—not payment, blocking, freezing, reversal, or reporting.
7. **Best demo success metric:** Value-weighted recall of injected APP scams **before submission** at a fixed genuine-payment challenge rate, with median decision latency and subgroup false-positive rates shown beside it.
8. **Next decisions before implementation:** Verify the official rubric and sandbox; choose the institutional deployment assumption; define acceptable challenge and latency budgets; approve the synthetic scenario/label methodology; obtain privacy/legal review for device/call/recipient signals; decide whether to include recipient-graph data; conduct target-user and fraud-operations interviews; and assign owners for event stream, scoring, guardrail, UI, and evaluation.

---

## G. Sources

### Official and government

- [INEGI/CNBV — ENIF 2024 results, published March 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)
- [INEGI — ENIF 2024 Reporte de Resultados, March 13, 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/enif2024_RR.pdf)
- [INEGI/CONDUSEF — ENSAFI 2023 presentation, published June 25, 2024](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf)
- [INEGI — ENOE July 2026, published August 27, 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf)
- [INEGI — ENDUTIH 2025, published June 16, 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf)
- [INEGI — Economic Censuses 2024 definitive micro/PYME report, updated 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf)
- [INEGI — Economic Censuses 2024 national minimonograph, updated September 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/ce2024_mn00.pdf)
- [INEGI — Economic Censuses 2024 payment-method report, 2025](https://inegi.org.mx/contenidos/programas/ce/2024/doc/ro_infmpn_ce24.pdf)
- [INEGI — EDN 2023, published January 31, 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf)
- [INEGI — ENVIPE 2026, published September 10, 2026](https://www.inegi.org.mx/contenidos/programas/envipe/2026/doc/envipe2026_presentacion_nacional.pdf)
- [Banco de México — Financial Market Infrastructures Report 2025, published September 11, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)
- [Banco de México — Financial Market Infrastructures Report 2024, published May 23, 2025](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BE0085475-B1D7-DED0-60AF-05ED88153BDC%7D.pdf)
- [Banco de México — Circular 14/2017 compiled through Circular 9/2026](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf)
- [Banco de México — SPEI overview](https://www.banxico.org.mx/services/spei_-transfers-banco-mexico.html) — **TODO: Verify** page publication date.
- [Banco de México — CoDi](https://www.banxico.org.mx/sistemas-de-pago/codi-cobro-digital-banco-me.html) — **TODO: Verify** page publication date.
- [Banco de México — 2025 remittances, published February 3, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf)
- [Banco de México — Basic Payroll Credit Indicators, data through December 2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf) — **TODO: Verify** PDF publication date.
- [CONDUSEF — H1 2025 self-evaluation report, PDF metadata August 26, 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)
- [CNBV/GIZ — Financial inclusion of people with disabilities, May 3, 2023](https://www.gob.mx/cnbv/articulos/inclusion-financiera-de-las-personas-con-discapacidad?idiom=es)
- [SAT — Payment Complement 2.0](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm) — mandatory since April 1, 2023; **TODO: Verify** page publication date.
- [Cámara de Diputados — Federal Labor Law, current through May 14, 2026](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf)
- [Cámara de Diputados — Fintech Law, current through November 14, 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf)
- [Cámara de Diputados — LFPDPPP, enacted March 20, 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)
- [Cámara de Diputados — Ley del Impuesto al Valor Agregado](https://www.diputados.gob.mx/LeyesBiblio/pdf_mov/Ley_del_Impuesto_al_Valor_Agregado.pdf) — **TODO: Verify** exact consolidation date before production use.
- [NAFIN — Cadenas Productivas](https://nafin.com/portalnf/content/cadenas-productivas/cadenas_productivas.html) — **TODO: Verify** page publication date and current eligibility.

### Academic and industry

- [Chioda, Gertler, Higgins and Medina — *FinTech Lending to Borrowers with No Credit History*, February 28, 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf)
- [Atradius — B2B Payment Practices Trends, Mexico 2024, October 28, 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024)
- [Smyth — *Gender and Remittances: Lived Experiences of Women in Oaxaca, Mexico*, 2022](https://uknowledge.uky.edu/geography_etds/83/)
- [BBVA México — Apartados](https://www.bbva.mx/personas/productos/cuentas/apartados.html) — **TODO: Verify** page publication date and current functionality.
- [Minu — Salary On-Demand](https://www.minu.mx/salario-on-demand) — **TODO: Verify** page publication date and terms.
- [Cetesdirecto — Recurring Saving](https://www.cetesdirecto.com/sites/portal/invertir-en-cetes.ahorro-recurrente) — **TODO: Verify** page publication date and current product terms.
- [Clip — Business solutions](https://www.clip.mx/soluciones) — **TODO: Verify** current exports/API availability.
- [Mercado Pago — Business product overview](https://www.mercadopago.com.mx/blog/mercado-pago-para-negocios) — **TODO: Verify** current exports/API availability and publication date.

### Journalism and community

No journalism or community/forum source is used as quantitative evidence or as a basis for ranking. The research reports contained limited press and vendor anecdotes, but the final recommendation does not depend on them. No unsupported community anecdote is presented.

### Cross-cutting unknowns before implementation

- **TODO: Verify** current production availability and coverage of consented transactional APIs institution by institution.
- **TODO: Verify** partner authority and policy for delaying, challenging, or reviewing a customer-authorized transfer.
- **TODO: Verify** nationwide APP scam incidence, attempted versus completed events, unique victims, loss, recovery, and time-to-drain.
- **TODO: Verify** access to recipient-network or confirmed-scam beneficiary intelligence under lawful inter-institution arrangements.
- **TODO: Verify** acceptable false-positive, abandonment, latency, and accessibility targets with users and fraud operations.
- **TODO: Verify** current SAT delegated-access, mass-download, and credential-handling requirements before any production fiscal integration.
- **TODO: Verify** whether the hackathon provides a transaction sandbox, cloud credits, or specific sponsor APIs.
