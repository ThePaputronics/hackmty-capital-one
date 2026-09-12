# Informal Workers, Micro-Merchants, Gig Workers & the Cash Economy in Mexico
Research brief for HackMTY Capital One challenge — product discovery angle: income volatility and financial inclusion in the informal/cash economy.

Date of research: 2026-09-11. All figures dated individually below.

---

## Top pain points (ranked)

### 1. Income is structurally invisible because the worker is informal, not because tools are missing
- **Population:** 32.6 million workers in informal employment, 54.8% of the employed population, per INEGI ENOE Q1 2026 (boletín 301/26, published May 2026) — up 0.5 pp and +583,000 people vs Q1 2025. [INEGI boletín](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/enoe/enoe2026_05.pdf) · [Forbes México](https://forbes.com.mx/la-tasa-de-informalidad-laboral-en-mexico-aumenta-a-54-8-en-el-primer-trimestre-de-2026/) · [Infobae](https://www.infobae.com/america/agencias/2026/05/26/la-tasa-de-informalidad-laboral-en-mexico-aumenta-a-548-en-el-primer-trimestre-de-2026/)
- **The pain:** More than half of working Mexicans have no payroll record, no IMSS record, no employer-verified income — the two primary "legibility" rails (payroll data, formal payment rails) simply don't exist for them.
- **Severity/frequency:** This is not a fringe segment — it is the majority of the workforce, and the rate has been rising, not falling, into 2026.
- **Why unsolved:** Every credit-scoring or income-verification product that leans on payroll, tax, or bank-transaction data structurally excludes this group by construction. BBVA Research notes informal, non-poor adults have only 11% debit card ownership and 21% credit/store-card ownership vs. formal workers — the formal financial system barely touches them even when they're not poor. [BBVA Research](https://www.bbvaresearch.com/en/publicaciones/mexico-access-to-financial-inclusion-poverty-vs-labor-informality/)

### 2. Cash is still the default rail for exactly the transactions that matter most to low-income households
- **Population:** Effectively the entire adult population, but concentrated among lower-income/informal households for whom cash is often the *only* option (19% of cash users cite no other option available). [Expansión / Banxico survey, published May 2024](https://expansion.mx/economia/2024/05/11/reduce-el-porcentaje-de-personas-que-paga-con-efectivo)
- **The pain:** 88% of Mexicans used cash as a payment method in 2023 (down from 92% in 2022 — a slow decline, not a shift). Cash use by purchase type in 2023: 85% for utility bills (light/water/phone), 69% for supermarket, 68% for convenience stores. Debit card use was only 17% in 2023 (vs 15% in 2022). [Expansión, citing Banxico](https://expansion.mx/economia/2024/05/11/reduce-el-porcentaje-de-personas-que-paga-con-efectivo)
- **Severity/frequency:** Daily — this is the default state of commerce, not an edge case.
- **Why unsolved:** Reasons for using cash are structural, not habitual: 43% say it's more practical/faster, 19% say it's their only option, 11% say it's the safest. Digital rails have to beat cash on all three axes simultaneously for the low-income cash-dependent segment, which none currently do at the point of sale for small-value purchases.

### 3. Informal savings/credit is the norm, and it's inefficient and sometimes predatory
- **Population:** 36.6% of the Mexican population saves *exclusively* through informal means (tandas, cash at home, loans from acquaintances) vs. only 8.2% who save exclusively through formal channels, per ENIF 2024. [ENIF 2024 press release](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) (numbers as reported in secondary coverage — see note on PDF access below)
- **The pain:** Roughly 30% of the population is exposed to "gota a gota" (day-to-day predatory microloans, 500–2,000 MXN principal, 10–40% *daily* interest, often with harassment on default). [Meridiano.mx, citing ENIF 2024](https://meridiano.mx/2025/09/03/mas-de-un-tercio-de-los-mexicanos-estan-atrapados-en-prestamos-informales/) — **treat the "gota a gota" figure and its exact %-value as needing independent primary-source confirmation; it is repeated in secondary press but I could not verify it against the raw ENIF tables (see Unverified section).**
- **Why unsolved:** Tandas/ROSCAs work on trust and social proximity, not creditworthiness data, so they don't scale credit access or build a portable credit history. Digital tanda apps (Tandapp, Tanda+) exist but are *organizers/trackers*, not payment processors or lenders — they explicitly don't hold funds. That means they solve coordination friction, not the underlying problem (no data trail usable by a lender). [Tandapp](https://tandapp.com.mx/) · [Tanda+](https://www.tandamas.mx/)

### 4. Gig/platform-worker earnings are volatile, partially formalizing, and contested
- **Population:** ~700,000 delivery/ride-hailing workers directly affected by Mexico's 2025 platform-worker IMSS reform (see below); a broader estimate of ~2.5 million people worked via Uber/DiDi/Rappi in 2023 (these are not the same denominator — see Unverified). [La Silla Rota](https://lasillarota.com/metropoli/2025/6/19/la-reforma-que-divide-los-repartidores-que-dice-la-ley-sobre-trabajadores-de-uber-didi-rappi-541474.html) · [Mundo Contact, 2023 figure](https://mundocontact.com/uber-didi-y-rappi-emplearon-a-casi-2-5-millones-de-mexicanos-en-2023/)
- **The pain:** Reported earnings vary hugely by source and methodology — weekly averages cited around 4,500–6,500 MXN in some trade press, while a CIDE-cited figure gives ~186 MXN/day (~4,000 MXN/month) for average delivery workers, and another outlet cites ~6,346 MXN/month (24% below minimum wage, no IMSS pre-reform). [traccionmedia](https://traccionmedia.com/articulo/un-repartidor-de-rappi-uber-eats-o-didi-food-en-mexico-gana-6346-al-mes-despues-de-gastos-24-menos-que-el-salario-minimo-y-sin-imss/) — this spread itself is evidence of volatility and of inconsistent measurement, not a single reliable number.
- **Why unsolved:** Platforms hold exact per-trip earnings data, but that data has historically not been portable to lenders. Palenca (a Mexican-founded, 2021, fintech) now offers an API that pulls Uber/DiDi/Rappi/InDrive (and IMSS) income/activity data for underwriting — a real but young and third-party-dependent solution. [Palenca blog](https://blog.palenca.com/como-verificar-ingresos-de-trabajadores-gig-para-originacion-de-credito-en-mexico/) The June–July 2025 LFT/IMSS reform is itself a live shock to this population's net income (workers report income loss from mandatory social-security contributions), so any product modeling "typical" gig income needs to account for a structural break at mid-2025. [Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/mexico/repartidores-y-conductores-de-uber-rappi-y-didi-acusan-perdida-de-ingresos-ante-reforma-de-seguridad-social/)

### 5. Micro-merchants have growing digital payment footprints, but usable "financial records" and credit access lag
- **Population:** More than 2,879,492 merchants in Mexico accept card payments via aggregators (Clip, Mercado Pago, Billpocket), concentrated in CDMX, Estado de México, and Jalisco; more than 6.3 million active POS terminals nationally by end-2024 (+60% in 5 years, driven by mPOS). [source article aggregating industry data](https://www.publimetro.com.mx/comercial/2025/11/11/el-nuevo-movimiento-que-esta-redefiniendo-como-se-vende-en-mexico-cuando-la-tecnologia-la-confianza-y-la-facilidad-giran-en-la-misma-direccion/) — **note: I could not trace this figure to a single named primary source (e.g., Banxico or CNBV); treat the exact numbers as secondary-press level of confidence, direction is credible.**
- **The pain:** Over 40% of merchants using mPOS reportedly did not accept any digital payment before 2020 — i.e., real financial-record creation is happening, but only for the ~40%+ minority of merchants who have adopted a terminal, and typically only for the *card* share of their sales, not their (still-dominant) cash sales.
- **Why unsolved:** Clip and Mercado Pago do lend against transaction history (see Existing Players below), but only to merchants who already use their terminal frequently and consistently — a chicken-and-egg gate that excludes the least-digitized, most cash-reliant micro-merchants, i.e. the ones who'd benefit most.

---

## Key statistics table

| Figure | Year | Source (URL) |
|---|---|---|
| Tasa de informalidad laboral (TIL): 54.8%, 32.6 million workers | Q1 2026 | [INEGI ENOE boletín 301/26](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/enoe/enoe2026_05.pdf) |
| TIL up 0.5 pp YoY / +583,000 people vs Q1 2025 | Q1 2026 vs Q1 2025 | [Infobae](https://www.infobae.com/america/agencias/2026/05/26/la-tasa-de-informalidad-laboral-en-mexico-aumenta-a-548-en-el-primer-trimestre-de-2026/) |
| 88% of Mexicans used cash as payment method (vs. 92% in 2022) | 2023 (survey published May 2024) | [Expansión, citing Banxico](https://expansion.mx/economia/2024/05/11/reduce-el-porcentaje-de-personas-que-paga-con-efectivo) |
| Cash use by purchase type: 85% utilities, 69% supermarket, 68% convenience store | 2023 | [Expansión, citing Banxico](https://expansion.mx/economia/2024/05/11/reduce-el-porcentaje-de-personas-que-paga-con-efectivo) |
| Debit card use: 17% (vs 15% in 2022) | 2023 | [Expansión, citing Banxico](https://expansion.mx/economia/2024/05/11/reduce-el-porcentaje-de-personas-que-paga-con-efectivo) |
| Cash use for purchases <500 MXN: ~85.2%; >500 MXN: ~73.5% | reported as 2023/2024 | UNVERIFIED — figure repeated across secondary aggregator summaries; I could not confirm a single primary URL. Treat as directionally plausible, not confirmed. |
| 76.5% of adults (18–70) have ≥1 formal financial product (record high) | 2024 | [INEGI/CNBV ENIF 2024 comunicado](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) |
| 63.0% have a formal savings account (+18.9 pp since 2015) | 2024 | [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) |
| Gender gap in financial products: 72.8% women vs 80.9% men | 2024 | [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) |
| AFORE gender gap: 34.2% women vs 51.4% men (17.2 pp) | 2024 | [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) |
| Rural AFORE 27.9% vs urban >42% | 2024 | [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_CP.pdf) |
| Rural financial-product penetration 56%→66% (+10pp, 2021→2024) vs urban +8pp | 2021–2024 | [ENIF 2024 secondary coverage](https://www.snieg.mx/2025/03/14/resultados-de-la-enif-2024/) |
| 36.6% save only informally; 8.2% save only formally | 2024 | [ENIF 2024, secondary coverage](https://meridiano.mx/2025/09/03/mas-de-un-tercio-de-los-mexicanos-estan-atrapados-en-prestamos-informales/) |
| Informal, non-poor workers: 11% debit card, 21% credit/store card ownership | undated (recent) | [BBVA Research](https://www.bbvaresearch.com/en/publicaciones/mexico-access-to-financial-inclusion-poverty-vs-labor-informality/) |
| 9,833,040 adults (10.4% of adults) receive remittances; 61.8% are women | 2024 (ENIF 2024 microdata via CEMLA) | [CEMLA analysis](https://www.cemla.org/foroderemesas/notas/2025-05-notas-de-remesas.pdf) |
| Remittances = ~30.5% of average recipient household income | 2022 | cited via CEMLA/Banxico secondary analysis (search-derived; primary CEMLA note not individually confirmed) |
| Annual remittances ~$64.8 billion (through Feb 2025 12-month figure) | 2025 | search-derived from Banxico monthly series |
| 2025 annual remittances projected ~$61 billion (-5.8% YoY) | 2025 | [BBVA](https://www.bbva.com/es/mx/las-remesas-en-mexico-podrian-caer-5-8-al-cierre-de-2025-y-alcanzar-los-61-mil-millones-de-dolares/) |
| US "One Big Beautiful Bill Act": 1% excise tax on cash/money-order-funded remittances, effective for transfers from Jan 1, 2026; electronic transfers (≈99% of flows to Mexico) exempt | signed July 2025, effective Jan 2026 | [RSM](https://rsmus.com/insights/tax-alerts/2025/excise-tax-on-cross-border-remittances.html) · [Niskanen Center](https://www.niskanencenter.org/the-1-u-s-remittance-levy-impacts-on-mexico-india/) |
| >2.88 million merchants accept card payments via aggregators (Clip/Mercado Pago/Billpocket); >6.3 million active POS terminals (+60% in 5 yrs) | end 2024 | secondary trade press, not independently traced to a named primary report — see caveat above |
| CoDi: >18 million registered users | early 2025 | secondary trade press (Banxico is the CoDi operator; figure not independently confirmed against a Banxico primary release) |
| Clip Capital/Presta Clip: cash-advance lending against terminal sales history; requires ≥2 sales/week for 3 consecutive months, min. 3,000 MXN/month sales, no collateral/credit-bureau check, repayment as % of daily sales | ongoing (product launched 2021) | [Clip blog](https://blog.clip.mx/articulo/como-sacar-prestamo-para-negocio) |
| Mercado Crédito: lending to Mercado Pago merchants based on proprietary sales-history scoring; up to $1,250,000 MXN; CAT 69.4%–132.2% | current (2026) | [Mercado Libre institutional page](https://www.mercadolibre.com.mx/institucional/hacemos/prestamos-a-vendedores) · [prestamoya.mx review](https://prestamoya.mx/resenas/mercado-credito) |
| Mexico platform-worker LFT reform in force; IMSS mandatory affiliation for platform delivery/drivers | LFT reform: June 22, 2025; IMSS scheme: July 1, 2025 | [Infobae](https://www.infobae.com/mexico/2025/06/28/nuevas-reglas-del-imss-para-repartidores-de-plataformas-digitales-entran-en-vigor/) |
| ~700,000 delivery/ride-hail workers affected by reform | 2025 | [La Silla Rota](https://lasillarota.com/metropoli/2025/6/19/la-reforma-que-divide-los-repartidores-que-dice-la-ley-sobre-trabajadores-de-uber-didi-rappi-541474.html) |
| Workers with full social security access grew 55.5% (Jul–Dec 2025) | 2025 | search-derived, cites government/IMSS reporting; not independently traced to a primary IMSS bulletin |
| Global Findex 2025: 79% global account ownership (up from 74% in 2021); Mexico named among 8 countries holding the majority of the world's 1.3 billion unbanked adults | 2024 survey / 2025 report | [World Bank Global Findex 2025](https://www.worldbank.org/en/publication/globalfindex/report) |
| Palenca: income-verification API covering Uber/DiDi/Rappi/InDrive/IMSS in Mexico | current (founded 2021) | [Palenca blog](https://blog.palenca.com/como-verificar-ingresos-de-trabajadores-gig-para-originacion-de-credito-en-mexico/) |

---

## The cash-visibility problem: who IS and ISN'T digitally legible

**Digitally visible (some continuous transaction stream exists):**
- Merchants who actively use a card-acceptance terminal/app (Clip, Mercado Pago Point, Billpocket, Getnet, SumUp) — but only for the *card-paid* share of their revenue; cash sales alongside the same register are invisible unless manually reconciled.
- Gig/platform workers (Uber, DiDi, Rappi, Uber Eats, InDrive) — the platform has exact per-trip records; visibility depends entirely on a worker consenting to share via something like Palenca, or the platform itself lending/reporting.
- Remittance recipients using a bank account or fintech wallet to receive transfers — visible on that channel, though many still cash out immediately.
- CoDi/DiMo users making QR-based transfers — a real record, but adoption (18M registered users, unconfirmed primary source) has not displaced cash for everyday purchases per the Banxico cash-use survey above.

**NOT digitally visible (cash-only or largely so):**
- The ~54.8% / 32.6 million informally employed workers, most of whom are paid in cash by informal or semi-formal employers/clients — no payroll trail exists at all.
- Any household paying for utilities, groceries, or convenience-store purchases the way the 2023 Banxico survey shows most Mexicans still do (85% cash for utilities, 69% supermarket, 68% convenience store) — this is the *majority* of day-to-day spending even for banked people.
- The 36.6% of the population saving exclusively through informal channels (tandas, cash at home, private loans) — by definition no institution sees this money move.
- Micro-merchants who have not adopted any card/QR terminal — an unknown but clearly large residual, since even 2.88 million aggregator-merchants and 6.3 million terminals are a fraction of Mexico's estimated 4+ million micro and small businesses (informal-sector count alone is in the tens of millions of workers).

**Bottom line:** any product premised on "read the transaction stream and infer creditworthiness/cash-flow-smoothing needs" only reaches the *already-partially-digitized* slice of each population — merchants with terminals, gig workers who opt into data-sharing, remittance recipients using formal rails. It structurally cannot reach cash-paid informal workers, cash-only micro-merchants, or informal-savings-only households, who are demonstrably the majority by several of the measures above. Any hackathon pitch that assumes "we'll ingest their transactions" must specify *which* sub-segment it targets and admit the rest stays invisible.

---

## Existing players and their gaps

| Player | What it does | Gap |
|---|---|---|
| Clip (Presta Clip / Clip Capital) | POS/mPOS terminal + payment links; cash-advance lending against terminal sales history, no collateral/bureau check | Only reaches merchants already transacting ≥2x/week for 3 months on Clip — excludes low-frequency and cash-first merchants; doesn't see cash sales at all |
| Mercado Pago / Mercado Crédito | POS ("Point"), online payments, tap-to-pay; lending against Mercado Pago sales-history scoring | Same adoption gate as Clip; reported CAT of 69–132% is expensive credit; ecosystem-locked (must sell/transact within Mercado Libre/Pago) |
| Billpocket, Getnet, SumUp | mPOS card acceptance for small merchants | Primarily payment acceptance, not credit/data products (no confirmed lending-against-transactions product found in this research) |
| CoDi / DiMo (Banxico) | Free QR/interbank transfer rails | Adoption undercut by the same cash-preference dynamics the Banxico survey documents; doesn't structure a lendable transaction history the way a POS log does |
| Palenca | Aggregates gig-platform (Uber/DiDi/Rappi/InDrive) + IMSS income data via API for lenders | Third-party/consent-dependent; only covers workers active on covered platforms; young company, no confirmed scale figures for Mexico found in this research |
| Tandapp / Tanda+ | Digitize tanda coordination and record-keeping | Explicitly do not hold funds or process payments — solve social/coordination friction only, generate no data usable for external credit underwriting |
| Traditional banks / AFORE | Formal savings, retirement accounts | Rural and gender gaps persist (see table); require formal onboarding (ID, sometimes proof of address/income) that's a real barrier for informal workers |

---

## What is UNVERIFIED

- **Exact cash-share-by-transaction-value figures (85.2% under 500 MXN / 73.5% over 500 MXN)** — repeated in secondary aggregator text, but I could not trace it to a specific, fetchable Banxico or ENIF page/table. Treat the *existence* of a large gap between small- and large-purchase cash intensity as plausible (consistent with the utility/supermarket cash-share data that *is* sourced) but do not cite the precise percentages as confirmed.
- **"31% of the population actively participates in a tanda"** — this figure surfaced from a general/Wikipedia-adjacent source in search results, not a primary ENIF table I could open. The ENIF-sourced "36.6% save only informally" figure is better evidenced and should be preferred.
- **"30% of the population affected by gota-a-gota loans"** — attributed to ENIF 2024 by secondary press (Meridiano.mx) but I was unable to open the primary ENIF PDF (binary/non-extractable in this session) to confirm the exact figure or its definition.
- **Merchant/terminal counts (2.88M merchants, 6.3M terminals, 18M CoDi users)** — plausible, consistent with independent reporting on Mexico's POS market growth, but not traced to one named primary source (e.g., a specific Banxico or CNBV report) in this session.
- **Total number of platform/gig workers in Mexico** — sources disagree by more than 3x (≈700,000 reform-affected vs. ≈2.5 million total platform workers in 2023); these likely measure different populations (workers meeting a minimum-wage threshold vs. anyone who ever worked a shift), but I could not reconcile the definitions from what I read.
- **Gig-worker earnings figures** — wildly inconsistent across sources (CIDE-cited ~4,000 MXN/month vs. trade press ~4,500–6,500 MXN/week vs. ~6,346 MXN/month net-of-expenses); this spread is itself informative (high measurement variance / high real volatility) but no single number here should be treated as "the" figure for a pitch deck.
- **"Workers with full social security access grew 55.5%, Jul–Dec 2025"** — could not trace to a primary IMSS bulletin; treat as a secondary-press claim.
- **PDF primary sources for ENOE and ENIF 2024** (INEGI boletín, CNBV/INEGI ENIF report) — I attempted to fetch these directly; the PDFs came back as non-extractable binary/compressed content in this session, so all ENOE/ENIF figures above are sourced from secondary press coverage of those releases, not from reading the primary tables myself. The URLs are the correct primary documents; a follow-up session with better PDF extraction should re-verify numbers directly against them.
- **Exact 2025 annual remittance total** — figures found ranged from a ~$64.8B trailing-12-month figure (Feb 2025) to a ~$61B full-year 2025 BBVA projection (implying a notable H2 2025 slowdown); I did not find a single authoritative "full-year 2025 actual" Banxico figure at the time of writing (Banxico's own December 2025 report exists as a source but was not fetched in full).

---

## Product opportunity hypotheses

1. **Merchant working-capital advance from blended card + cash-declared revenue, for terminal-owning micro-merchants.** Continuous transaction data (from a POS/mPOS terminal already in the merchant's hands, à la Clip/Mercado Pago) would enable short-term, revenue-based lending with automatic repayment as a % of daily card sales — this already exists (Clip Capital, Mercado Crédito) and is only available to merchants who already transact frequently through that specific terminal. A genuine improvement is a product that blends terminal data with a merchant's *self-declared* cash sales (accepting some fraud risk) to widen eligibility to more cash-heavy but still terminal-owning merchants — available for the ~2.88M+ aggregator-merchant population, NOT for pure-cash merchants with no terminal.

2. **Gig-income smoothing / advance product built on platform-earnings APIs (à la Palenca).** Continuous per-trip earnings data from Uber/DiDi/Rappi/InDrive would enable an earned-wage-access or income-smoothing product for the ~700,000 reform-covered platform workers (a population now also newly IMSS-registered, which itself creates a formal identity anchor to build on) — but this is available only for workers active on covered platforms who consent to data sharing, not for informal workers paid in cash by individuals or small unregistered businesses (the much larger 32.6M informal-employment population).

3. **Remittance-linked forced-savings or bill-smoothing product for remittance-receiving households.** Since remittances arrive as a fairly predictable (if variable) recurring inflow and already reach ~9.8 million adults (61.8% women) largely through formal/bank/fintech rails, continuous view of remittance *receipt timing* (not the recipient's other spending, which is likely cash) would enable auto-save or auto-bill-pay products timed to disbursement — available only for the receiving side of formal remittance channels (the ~99% of US-to-Mexico flows that are electronic, per remittance-tax reporting), and says nothing about the recipient's other income, which may still be cash/informal.

4. **NOT a viable transaction-stream product as scoped: a general "informal worker" or "cash economy" cash-flow product.** For the majority-of-workforce population (32.6M informal workers, 36.6% informal-only savers, 88% cash payers), no transaction stream exists to observe — any product for this segment has to be built on *non-transactional* signals (self-reported income, alternative data like utility/telecom payment history, group-based trust mechanisms like a digitized-but-fund-holding tanda) rather than continuous transaction ingestion. This is the honest constraint: the largest, most underserved population in this brief is also the one for which "read their transactions" is not a workable strategy.

---

*Sources are cited inline throughout; where a figure could not be traced to a primary document opened in this session, it is flagged explicitly under "What is UNVERIFIED" rather than presented as confirmed.*
