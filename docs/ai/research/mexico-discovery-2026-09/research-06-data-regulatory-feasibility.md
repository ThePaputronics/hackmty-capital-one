# Data & Regulatory Feasibility — Capital One Challenge (HackMTY)

Research date: 2026-09-11. This is a reality check, not a design document. Angle: what data can actually be pulled in a weekend, what Mexican law actually requires, and what has already been done to death at fintech hackathons.

---

## 1. Usable data sources

| Source | Mexican? | Free sandbox? | Data shape | Signup effort | URL |
|---|---|---|---|---|---|
| **Capital One Nessie API** | No — US-shaped mock data | Yes, free hackathon key | Mock banking data: customers, accounts, purchases, transfers, deposits/withdrawals, bills, merchants, ATMs/branches (with real ATM/branch geodata). Enterprise key = read-only across all mock data; Customer key = full CRUD on your own seeded data. JS/Android/Golang community SDKs exist. | Minutes — self-serve key at api.nessieisreal.com | http://api.nessieisreal.com/, https://developer.capitalone.com/nessie-api-guide |
| **Belvo (sandbox)** | Yes | Yes, free, "~5-10 minutes to first call" per their own docs | Bank account aggregation (balances, movements/transactions, owners) for connected Mexican institutions; separate **Fiscal API** product that connects to the **SAT** (via RFC + e.firma/CIEC) returning tax status, invoices (CFDI), tax returns — this is a real, documented, existing SAT integration, not a rumor | Fast — email confirm, dashboard, generate keys, sandbox has canned dummy data (no real bank/SAT creds needed in sandbox) | https://developers.belvo.com/, https://developers.belvo.com/products/fiscal_mexico/fiscal-mexico-introduction |
| **Finerio Connect** | Yes (LatAm, Mexico-first) | Sandbox exists (per vendor docs/marketing) | Open banking aggregation + PFM categorization for Mexican accounts; OAuth playground, Postman/Insomnia collections advertised | Not independently timed; vendor claims "under a day" | https://apiv2.finerioconnect.com/, https://finerioconnect.com/en |
| **Prometeo** | Yes, part of a wider LatAm footprint (11 countries incl. Mexico) | Yes — public sandbox at banking.sandbox.prometeoapi.com | Bank account access/movements/transfers, account validation, cross-border payments, identity (CURP for Mexico), fiscal (SAT/DIAN/CEP) | Low-moderate — API key + header auth, sample sandbox app on GitHub (thomasviana/sandbox_prometeo_api) | https://prometeoapi.com/en, https://docs.prometeoapi.com/ |
| **Palenca** | Yes (HQ Mexico City, LatAm coverage) | Yes — free Console signup, sandbox + production keys | Gig/payroll income & employment verification (Uber, Rappi, DiDi, formal payroll) — income streams, not transaction ledgers | Fast — vendor claims "integrate in under 10 minutes"; separate sandbox vs prod keys in Console | https://console.palenca.com/, https://developers.palenca.com/ |
| **Banxico SIE API** | Yes | Yes, free | Macro time series only: interest rates (CETES/TIIE), FX, SPEI/remittance volumes, inflation, etc. — aggregate economic indicators, **not** transaction-level or per-user data | Fast — request a 64-char token via web form, then REST/JSON queries by series ID | https://www.banxico.org.mx/SieAPIRest/service/v1/ |
| **INEGI DENUE API** | Yes | Yes, free | Business directory: 6M+ establishments with name, address, geocoordinates, economic-activity class (good for realistic merchant/MCC data), searchable by radius/name/activity | Fast, but docs assume JS + OOP familiarity | https://www.inegi.org.mx/servicios/api_denue.html |
| **CNBV Portafolio de Información** | Yes | Public but not really an "API" for hackathon use | BI dashboards / bulk statistical financial data on regulated institutions (balance sheets, indicators) — not transaction-level, not per-consumer | Browsing a web portal, not a signup | https://portafolioinfo.cnbv.gob.mx/ |
| **CONDUSEF (SIPRES/REDECO)** | Yes | Only for registered institutions, not general hackathon use | SIPRES = public registry of regulated institutions (identity/status, not transactions); REDECO API is for collection agencies to register complaint data, requires institutional onboarding | Not hackathon-friendly — REDECO API needs an institutional account | https://webapps.condusef.gob.mx/SIPRES/, https://api-redeco-docs.condusef.gob.mx/ |
| **datos.gob.mx** | Yes | Yes, free, no signup | General open-data catalogs (government financial/budget data, not consumer banking) — useful at most for narrative/context, not transaction simulation | Instant download | https://www.datos.gob.mx/ |
| **IEEE-CIS Fraud Detection (Kaggle)** | No — Vesta/US e-commerce card-not-present data | Yes, free Kaggle download | 590k transactions, 394 features across transaction+identity tables, 3.5% fraud rate. Real fraud labels, but US e-commerce card-present-not shape (device/browser fingerprints), not MX bank-transfer shape | Instant | Kaggle competition page |
| **PaySim (Kaggle)** | No — modeled on an African mobile-money operator, scaled synthetic | Yes, free | 6.3M synthetic mobile-money transactions, 30-day sim, types (cash_in/out, transfer, payment, debit), 0.13% fraud rate. Good for volume/velocity simulation, wrong currency/geography/merchant context for Mexico | Instant | Kaggle |
| **Sparkov / Kaggle credit card fraud (ULB)** | No — European/US card data | Yes, free | Classic anonymized PCA-transformed card transactions (ULB) or Sparkov-generated synthetic card transactions with merchant/category fields | Instant | Kaggle |

**Bottom line on data:** there is no free, hackathon-speed source of *real* Mexican transaction-level consumer data. The realistic play is: Nessie (or a self-rolled generator) for the transaction stream shape, optionally overlaid with Banxico/INEGI data for realistic macro context and merchant geography, and one of the fraud Kaggle sets purely for a well-labeled anomaly-detection signal to train/validate against — clearly disclosed as US/EU-shaped synthetic-or-anonymized data, not Mexican production data. Belvo/Prometeo sandboxes are real and worth wiring up for demo credibility (they return dummy data that *looks* like a real MX bank/SAT connection), but their sandbox data is still canned demo data, not live Mexican consumer transactions — don't claim otherwise on stage.

---

## 2. Regulatory constraints

### 2.1 Ley Fintech (2018), Art. 76 — Open Finance data-sharing mandate
**What it requires:** ITFs and other financial entities must expose standardized APIs for three data tiers: (1) open data (products, services, branch/ATM locations), (2) aggregated data (anonymized statistics), (3) transactional data (with customer consent).

**What a prototype must do:** Cannot rely on a legally-mandated, bank-operated transactional-data API existing in Mexico today (see §3 — it doesn't). Any "connect your real Mexican bank account" flow must go through a private aggregator (Belvo/Finerio/Prometeo) that has negotiated its own bank connections, not a regulator-mandated pipe. Frame any real-bank-connection feature in the pitch as "via an open-finance aggregator," not "via Mexico's Open Finance API," since the latter doesn't exist yet for transactions.

### 2.2 LFPDPPP (new law, in force since 21 March 2025) — data protection
**What changed:** A new Ley Federal de Protección de Datos Personales en Posesión de los Particulares took effect 21 March 2025, following the constitutional reform that eliminated INAI; INAI's data-protection oversight functions moved to the new Secretaría Anticorrupción y Buen Gobierno (SABG). The new law broadens who counts as a "responsable" (data controller) — now anyone who processes personal data, even without deciding on the processing — and formally defines ARCO rights (Acceso, Rectificación, Cancelación, Oposición); tacit consent is valid as a general rule, but financial data is typically treated as sensitive, which normally raises the consent bar (explicit, not tacit) — verify this nuance against the final regulations before building a consent flow.

**What a prototype must do:** Even a demo touching real user financial data needs: an aviso de privacidad (privacy notice) covering purpose/scope, an explicit-consent flow for financial data specifically (don't rely on tacit consent for anything framed as "sensitive"), and a plan for ARCO requests. For a hackathon demo using synthetic/mock data (Nessie, sandbox data), this is largely moot — say so explicitly in the pitch to preempt the question, and don't collect real personal data from judges/testers without a notice.

### 2.3 Secreto bancario — Art. 142, Ley de Instituciones de Crédito
**What it restricts:** Banks cannot disclose client account information/documentation to third parties except through narrow statutory exceptions (judicial order, SHCP for tax enforcement, Public Prosecutor for criminal investigation, and — separately, under the Fintech Law framework — data-sharing APIs built for that purpose with consent). It is a real constitutional-privacy-linked restriction, not a formality.

**What a prototype must do:** A product that "reads a user's real bank transactions" cannot do so by scraping or asking users for bank credentials directly against a bank — it must go through a licensed/contracted aggregator (Belvo etc.) that has its own legal basis, or use the user's own exported statements/mock data. Don't design a flow that implies the product itself has bank-side access.

### 2.4 Automated decision-making / credit scoring
**Status:** No dedicated Mexican statute for algorithmic credit scoring or a general AI law (see 2.6). Practitioner commentary converges on: scoring models must avoid proxies for discrimination (e.g., can't reject purely on postal code or name), and consequential automated credit decisions should retain a human-review component. This is industry best-practice / emerging legal-commentary consensus, not a codified requirement with an enforcement mechanism as of today — **treat as `TODO: Verify`** if the team wants to cite a specific binding rule; nothing found ties this to a specific CNBV circular or article number.

**What a prototype must do:** If the product does cash-flow-based credit scoring for thin-file consumers (track 1), build in an explainability layer (feature-level reasons, not a black-box score) and never use protected-class proxies (postal code, gender, indigenous-community indicators) as model features — both for ethics and to preempt an obvious judge question.

### 2.5 Licensing — moving money or giving "asesoría"
- **IFPE (Institución de Fondos de Pago Electrónico):** required to legally hold/move client funds electronically. CNBV authorization, with SHCP/Banxico input; commentary cites a 12–18 month authorization timeline. **Not attainable for a hackathon prototype.**
- **Asesor en Inversiones / robo-advisor licensing:** searches did not surface a clear, hackathon-relevant answer on thresholds — flagged as **UNVERIFIED**; the safe assumption is that any feature framed as personalized investment advice (not just budgeting/cash-flow nudges) risks needing this and should be avoided or clearly labeled "educational, not investment advice."

**What a prototype must do:** Stay in the "financial wellness / analytics / nudges" lane — categorizing spend, forecasting cash flow, flagging anomalies, suggesting a savings amount — and avoid: actually moving money between real accounts, holding float, or presenting output as licensed investment advice. This is squarely compatible with the repo's selected hybrid direction (coach + anomaly agent), which does not require IFPE/advisor licensing as designed.

### 2.6 AI regulation in Mexico
**Status:** No general AI law in force. As of the most recent evidence found (mid-2026), ~85 AI-related legislative initiatives have been introduced since 2023, 67 still pending; a separate senate bill for a "Ley Nacional para Regular el Uso de la Inteligencia Artificial" was introduced 11 Feb 2026; regulation is proceeding sector-by-sector (labor, telecom, data protection, IP) rather than as one omnibus law. **No binding AI-specific obligation applies to a hackathon prototype today**, beyond the existing data-protection and automated-decision norms above.

---

## 3. Open Finance status — VERDICT: **VERIFIED, and it is NOT in force for transactional data**

- **VERIFIED:** CNBV published the first Open Finance secondary rules in the DOF on **4 June 2020**, covering **only the "open data" tier** — product/service catalogs, branch/office locations, and ATM location/service data. This is operational.
- **VERIFIED (convergent across two independent sources — a LatAm fintech-law article and a 2026 regulatory-map site):** the secondary rules for the **aggregated data** and **transactional data** tiers mandated by Article 76 of the 2018 Ley Fintech have **never been published**, years past the law's own deadline. One source states explicitly that as of **February 2026** this secondary regulation "had still not been published," and that CNBV signaled at Fintech Festival 2026 an *intent* to keep working on it — no committed date.
- **Practical meaning:** there is no regulator-mandated, standardized API today through which a third-party app can pull a Mexican consumer's real transaction history "the way Open Banking works in the UK/EU." What exists in the market (Belvo, Finerio, Prometeo) are **private aggregators** operating via their own bilateral bank integrations/credential-based aggregation (and, for Belvo, a dedicated SAT fiscal-data integration) — not the Article 76 transactional-data API.
- Do not let the team pitch "we use Mexico's Open Finance API" — that phrase overclaims a regulatory pipe that does not exist. Correct framing: "we integrate with a Belvo/Prometeo-style aggregator sandbox, consistent with where Mexican open finance is headed, while the transactional-data secondary rules are still pending at CNBV."

---

## 4. Crowdedness map — what's already been done

Evidence from HackMTY 2023–2025 Devpost galleries, BBVA Hackathon (2018–2024), and general fintech-hackathon-idea aggregators:

**Cliché ideas to avoid (high confidence, direct evidence):**
1. **Generic budgeting/expense-tracking dashboard** ("track income, savings, monthly spend, get alerts") — explicitly called out as *the* common fintech-hackathon concept by an idea-aggregator site, and matches multiple HackMTY entries (CapitalTrack, Capital One All In One).
2. **Debt payoff / payment-strategy optimizer** — HackMTY 2025 had at least two near-identical entries (debt-planner; OMEGA, which "analyzes balances, interest rates, and due dates to suggest optimal payment strategies").
3. **Generic AI financial-literacy chatbot/co-pilot** — HackMTY 2025 (Liora, "Your Financial Co-Pilot"; BanxAI, "smart financial decisions instantly") and BBVA's 2024 winners (financial-education trivia bot, sign-language financial-education chatbot) both landed here — this is the single most repeated pattern across both events.
4. **Transaction categorization via ML for cash-flow view** — BBVA Hackathon Mexico's own **2019 winning project** was exactly this (auto-categorize business transactions + cash-flow analysis) — a judge on this exact challenge track has already rewarded this idea once; doing only this again is a regression, not a differentiator.
5. **Subscription tracker** — explicitly documented as a past Citibanamex hackathon project built directly from account-holder research; a bare "find your subscriptions" feature is not novel by itself (it can still be one *component* of a larger system, per the repo's own selected direction, but shouldn't be the headline).
6. **"Merge all your accounts + AI assistant" super-app** — HackMTY 2025 "Capital One All In One" already did this framing.

**What is comparatively less crowded (opportunity space):** real-time anomaly/fraud-and-velocity detection **as a first-class, explainable agent surfacing through a consumer-facing coach** (rather than either a back-office fraud-ops tool or a bolted-on "we also flag odd charges" footnote) was not found as a repeated HackMTY/BBVA winner pattern — this supports the repo's already-selected hybrid direction (`docs/ai/knowledge/challenge-brief.md`) as more differentiated than a standalone budgeting or chatbot entry, provided the anomaly agent is genuinely load-bearing in the demo rather than decorative.

---

## 5. What is UNVERIFIED (flagged loudly, not guessed)

- Exact **rate limits** for the Nessie API — the interactive docs page returned HTTP 403 to automated fetch; only general capability/shape claims are confirmed via secondary sources, not the primary doc.
- Whether **explicit vs. tacit consent** is legally required for "sensitive" financial personal data under the new 2025 LFPDPPP specifically (general ARCO/consent framework is confirmed; the sensitive-data carve-out interaction with the new tacit-consent default rule was not confirmed against the statute text itself).
- Whether **automated credit-scoring explainability/human-review** is an actual binding legal requirement in Mexico or only strong practitioner commentary/best practice — no specific CNBV circular or statute article was found backing this as enforceable law.
- **Asesor en Inversiones / robo-advisor licensing thresholds** and whether any safe-harbor exists for a clearly-labeled "educational, not advice" prototype — not found.
- Exact **signup latency** for Finerio Connect's sandbox (only vendor marketing claims found, not an independent account of "we signed up and it took X minutes").
- Whether CNBV's February–2026-and-later public statements (Fintech Festival 2026) contain any **firm committed date** for publishing the transactional-data secondary rules — evidence found says intent was signaled, not a date.

---

## 6. Feasibility verdicts per challenge track

**Track 1 — Consumer Financial Autonomy & Credit Building:**
Feasible for a weekend using Nessie (or a custom generator) for the transaction stream, with cash-flow-based scoring built as an explainable model (not a black box) and clearly labeled as a prototype/non-binding score, not a regulated credit decision. Real "connect your bank" via Belvo/Prometeo sandbox is a believable demo add-on but must be pitched as aggregator-based, not as "Mexico's Open Finance." Avoid landing on a bare budgeting dashboard or generic chatbot — both are the most repeated HackMTY/BBVA pattern.

**Track 2 — SMB Cash-Flow & Working Capital Intelligence:**
Feasible for the forecasting/analytics core using synthetic or Nessie-shaped transaction data plus INEGI DENUE for realistic MX merchant/business context. **Not feasible** in a weekend: any feature that implies actually extending or brokering working-capital financing to a business — that would cross into IFC/IFPE licensed-activity territory. Keep the "recommend a working capital buffer" feature as a recommendation engine, not a financing product.

**Track 3 — Real-Time Anomaly & Security Sentinel:**
Feasible and comparatively fresh territory (see §4) — Kaggle fraud datasets (IEEE-CIS, PaySim) give real, well-labeled anomaly signal to train/validate a velocity/MCC-hopping detector, even though they're US/EU-shaped; the mismatch should be disclosed as a limitation ("model trained on public fraud-labeled data, applied to Mexican-shaped synthetic transactions for the demo") rather than glossed over. Legally, flagging/scoring anomalies for a user's own review is low-risk; do not build in an auto-block/auto-freeze-account action against real funds without treating it as a production-security feature requiring far more diligence than a hackathon allows.

**Overall:** the repo's already-selected hybrid direction (wellness coach + anomaly agent as one pipeline) is defensible on both the data-availability and crowdedness axes — it avoids the single most repeated failure mode (a bare budgeting app or generic chatbot) while staying inside what a non-licensed prototype can legally claim to do.
