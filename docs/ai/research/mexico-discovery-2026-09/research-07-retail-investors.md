# Research: Retail Investors & Savers in Mexico — Market Participation, Savings Products, Investment Fraud

Scope: HackMTY / Capital One challenge discovery. Angle = retail investing, CETES/Cetesdirecto, neobank savings yields, AFORE/retirement, investment fraud, crypto, financial literacy — all Mexico-specific, 2022–2026.

---

## Top pain points (ranked)

### 1. Real (inflation-adjusted) yield confusion on neobank/SOFIPO savings products
- **Affected population:** Millions of Nu México, Klar, Stori, Hey Banco and similar SOFIPO/fintech-savings users. Nu alone reports well over 10M account holders in Mexico region-wide (LatAm scale; Mexico-specific account count for savings product NOT separately verified here — see UNVERIFIED).
- **Pain:** Products are marketed with a prominent **nominal** headline rate (e.g., Nu "Cajita" up to 14.25% in late 2024; Stori up to 15%/15.5%; Klar "Fondo de Rendimientos" up to 15%). The **GAT real** (inflation-adjusted) figure required by regulation is disclosed but far less prominent, and is roughly **less than half** the nominal number in the cases we could verify (e.g., Nu's 2026 published GAT real ranged 3.24%–3.49% against GAT nominal of 7.30%–7.57% for the same terms — note these are materially lower than the late-2024 rates, reflecting falling Banxico policy rates).
- **Severity/frequency evidence:** ENIF 2021 (CNBV/INEGI) shows only 45.0% of adults could correctly *calculate* simple interest even though 91.2% said they understood the concept — i.e., most people cannot translate an advertised rate into an actual peso outcome, let alone adjust for inflation. [ENIF 2021 report](https://www.cnbv.gob.mx/Inclusi%C3%B3n/Anexos%20Inclusin%20Financiera/Reporte_Resultados_ENIF_2021.pdf)
- **Why unsolved:** GAT real is a genuine, Banxico-mandated disclosure (calculator at [banxico.org.mx/waGAT](https://www.banxico.org.mx/waGAT/)), but it lives in fine print/footnotes and fluctuates with Banxico's own inflation forecast, not with what the app actually shows the user month-to-month. No product we found translates "GAT real" into a plain-language "you actually gained/lost N pesos of purchasing power this month" statement inside the app itself.

### 2. Retail investors and savers are exposed to unregistered "financieras"/Ponzi schemes, with a large low-friction (WhatsApp/social-media) sales channel
- **Affected population:** Not centrally quantified (no single Mexico-wide investment-fraud victim count found — see UNVERIFIED), but CONDUSEF's SIPRES impersonation reports are continuous and numerous (e.g., 174 financial institutions reported being impersonated cumulatively through Nov 2024, with new monthly batches of 8–16 institutions every month through 2025). [CONDUSEF SIPRES pages](https://www.condusef.gob.mx/?p=contenido&idc=2527&idcat=1)
- **Pain:** Documented 2023–2025 cases with concrete peso losses: TruCapitals (Tijuana, offered 8–12% "returns," stopped paying since June 2023), Aras Business Group (Chihuahua, MXN 74.046M + USD 332,441 in damages), VITAS Consulting SAPI de CV (real-estate investment scheme, MXN 3.13M + USD 4,400), "Ñoquis de la Abundancia" pyramid scheme (2024, promises up to 8x capital). CNBV explicitly warns that being incorporated as a SAPI ("Sociedad Anónima Promotora de Inversión") does **not** confer authorization to take deposits or offer investment products — a specific, exploitable gap in Mexican corporate law that scammers use. [CNBV — entidades no autorizadas](https://www.gob.mx/cnbv/acciones-y-programas/entidades-que-ilegalmente-ofrecen-servicios-de-inversion-fuera-de-mexico-y-otros-esquemas-de-fraude-financiero)
- **Severity/frequency evidence:** 113,824 total fraud cases were reported nationally in 2024 per the Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública — but this is **all fraud types**, not investment fraud specifically (UNVERIFIED how much is investment/Ponzi-related).
- **Why unsolved:** CNBV maintains no independent Mexico-specific blacklist of its own; it points the public to IOSCO's international investor-alerts portal and NASAA materials, both English-first and not designed for a Mexican retail audience. CONDUSEF's SIPRES tool exists but is a manual lookup a victim must proactively use *before* sending money — there is no automated check at the moment of transfer.

### 3. AFORE inertia: ~27% of retirement accounts are "assigned," not chosen, and fee/return awareness is low
- **Affected population:** Of roughly 67.7 million total AFORE accounts, about **27% are "cuentas asignadas"** (worker never actively chose an administrator) — a figure that varies hugely by AFORE (PensionISSSTE 49% assigned of 1.64M accounts; Sura 35% of 2.39M; vs. Coppel >90% actively chosen of 12.7M and XXI Banorte 95% signed of 8.38M). An older (2021, non-CONSAR-attributed, so treat as directional only) estimate put "workers who don't know they have an Afore" at 18.45 million — strikingly close to 27% of 67.7M (~18.3M), a plausible cross-check. [ElCEO — cuentas asignadas](https://elceo.com/negocios/afores-competiran-por-administrar-119000-mdp-de-cuentas-inactivas-del-sar/), [ElCEO 2021](https://elceo.com/economia/mas-de-18-millones-de-trabajadores-desconocen-que-tienen-afore/)
- **Pain:** Workers with assigned/unknown Afores face friction on procedures, beneficiary designation, and statement access; they also miss the chance to pick lower-fee, higher-return administrators (2025 system-average fee 0.547% of balance, ranging 0.52%–0.55% across Afores — a small-looking percentage that compounds over a multi-decade horizon). [Infobae — comisiones Afores 2025](https://www.infobae.com/mexico/2024/11/29/estas-seran-las-comisiones-que-cobraran-las-afores-en-2025-segun-la-consar/)
- **Severity/frequency evidence:** The 2020 pension reform is ramping mandatory employer contributions from 6.5% (2020) to 15% (2030) specifically because replacement rates were low; CONSAR reports the reform lifted replacement rates for workers earning up to 5 minimum wages from 31% to 54%, and reports an average ~71% replacement rate for those retiring already under the new rules — but this only helps workers who stay in the formal system long enough, and doesn't fix the "wrong/assigned Afore" problem. [El Contribuyente](https://www.elcontribuyente.mx/2020/07/presentan-reforma-a-pensiones-con-aumento-a-aportaciones-patronales-y-menos-semanas-de-cotizacion/), [FIAP](https://www.fiapinternacional.org/mexico-reforma-de-pensiones-del-2020-elevo-tasa-de-reemplazo-al-72/)
- **Why unsolved:** Afore choice is a low-salience, one-time decision made (or not made) at labor-market entry; CONSAR's own remedy is passive reassignment to better-performing Afores after non-response, not proactive worker engagement.

### 4. Retail brokerage/investment-fund participation is growing extremely fast off a low base, concentrated in one platform, and still tiny relative to US benchmarks
- **Affected population / growth:** AMIB reported brokerage accounts grew from ~7.8M (Dec 2020) to **15.77M (Dec 2024)**, +102% [search-aggregated AMIB figures via elceo.com/zya.mx]. Separately, at AMIB's Foro de Fondos (May 2025), total investors across the stock-market system reached **31 million** (1.5x IMSS contributors, >50% of the formal+informal labor force), with fund-investor count growing from <3M to 13.1M in five years (+400%) and AUM from 2.4 to 4.5 trillion pesos (~13% of GDP). [Yahoo/AMIB Foro de Fondos 2025](https://es-us.noticias.yahoo.com/foro-fondos-amib-2025-31-160000945.html) GBM alone held 4.94M of the ~4.94M-account total reported for Dec 2022 (91.8% of all brokerage accounts that year), per Milenio/CNBV data, with the number of accounts up 18x from 2018 to 2022. [Milenio](https://www.milenio.com/negocios/nueve-10-cuentas-inversion-encuentran-gbm-cnbv)
- **Pain:** Despite the fast growth, a GBM–EY Parthenon study cited in that same Milenio piece states only **2% of Mexico's adult population** holds an investment account, versus **58% in the US** — the "growth" is off a very small base and concentrated almost entirely in one app (GBM).
- **Why unsolved:** This is a market-development/product-design gap (access, minimums, trust, UX), not something a transaction stream by itself would reveal or fix.

### 5. Crypto adoption is real but small, and regulation actively blocks banks from offering it directly — pushing users to less-supervised channels
- **Affected population:** Bitso reports 4.4M users in Mexico at end of 2024 (+13% YoY; 9M across LatAm). [El Universal](https://www.eluniversal.com.mx/cartera/crecimiento-de-criptomonedas-en-mexico-alcanza-13-bitso-reporta-44-millones-de-usuarios-en-2024/) Broader crypto-holder estimates for Mexico put the number at 3.1M people (2.5% of population, +15% YoY, 2024), positioning Mexico as LatAm's #3 and world's #16 crypto market by adoption (source is a secondary aggregator article; treat the specific "3.1M/2.5%" figure as **lower-confidence** pending a primary Chainalysis-style source).
- **Pain:** Ley Fintech Art. 30 lets financial institutions use virtual assets only with prior Banxico authorization and only for **internal** operations — banks/fintechs are barred from directly offering clients exchange, custody, or transfer of virtual assets, and Banxico has never published an approved list of virtual assets, which several legal commentators (and one law firm publicly, calling Banxico's rules unconstitutional) say has frozen institutional crypto products in Mexico. [AbogadoBlockchain](https://abogadoblockchain.com/licencia-cripto-cnbv-mexico/), [Bitfinanzas — Banxico reaffirms bitcoin ban for banks](https://bitfinanzas.com/banco-de-mexico-reafirma-a-bancos-la-prohibicion-de-operar-con-bitcoin/) This pushes crypto activity to Bitso and similar non-bank exchanges plus informal/offshore platforms, which are harder to trace and to protect users on.
- **Why unsolved:** This is a standing regulatory posture (Banxico), not a product gap that a hackathon app can route around.

---

## Key statistics table

| Figure | Year | Source |
|---|---|---|
| 15.77M brokerage accounts in Mexico (+102% vs 7.8M in Dec 2020) | Dec 2024 | AMIB (via [elceo.com](https://elceo.com/mercados/cuentas-de-inversion-en-mexico-llegaran-a-20-millones-en-dos-anos-amib/)) |
| 31M total investors in stock-market system (1.5x IMSS contributors); fund investors 13.1M (+400% in 5 yrs); AUM 4.5 trillion pesos (~13% GDP) | May 2025 | [AMIB Foro de Fondos 2025 / Yahoo](https://es-us.noticias.yahoo.com/foro-fondos-amib-2025-31-160000945.html) |
| 4.94M brokerage accounts total; GBM = 4.536M (91.8% share); only 2% of adult population has an investment account vs 58% in US (GBM–EY Parthenon) | Dec 2022 | [Milenio/CNBV](https://www.milenio.com/negocios/nueve-10-cuentas-inversion-encuentran-gbm-cnbv) |
| Cetesdirecto: 1.95M users end of 2023 (+807,184 new users, +120% YoY) | 2023 | [Expansión](https://expansion.mx/economia/2024/01/08/cetesdirecto-llega-casi-2-millones-usuarios) |
| Cetesdirecto: 2.755M active accounts (>2.7M investors), ~600 new users/day; balance fell 53.7% (26,945M → 12,450M pesos) as rates dropped | 2024→2025 | [Diario de Morelos](https://www.diariodemorelos.com/noticias/cetes-directo-cumple-15-os-con-27-millones-de-usuarios-pero-inversiones-caen-53-en-2025), [Expansión](https://expansion.mx/economia/2025/12/14/cetes-directo-adios-horario-depositos-transferencias) |
| GAT real vs nominal (Nu México, term savings): 7.30–7.57% nominal vs 3.24–3.49% real | 2026 (published rates) | [Nu México ayuda](https://nu.com.mx/ayuda/cuenta-nu/cuanto-es-la-ganancia-anual-total-gat/) |
| Nu Cajita rates up to 14.25% nominal (90-day) | Nov 2024 | [El Imparcial](https://www.elimparcial.com/dinero/2025/01/14/que-rendimiento-ofrece-nu-al-cierre-del-2024-conoce-las-nuevas-tasas/) |
| Stori up to 15%/15.5% nominal; Klar Fondo de Rendimientos up to 15% nominal | 2025 | [Xataka](https://www.xataka.com.mx/empresas-y-economia/stori-tambien-cambia-sus-rendimientos-mexico-mantiene-15-5-estas-seran-nuevas-tasas), [Klar](https://www.klar.mx/post/fondo-de-rendimiento-klar-haz-crecer-tus-ahorros) |
| SAR total resources: 6.8 trillion pesos (20.3% of GDP); contribution rate at 8.5% of salary (ramping to 15% by 2030) | End 2024 | [CONSAR/gob.mx](https://www.gob.mx/consar/prensa/el-sistema-de-ahorro-para-el-retiro-al-cierre-de-2024-388102) |
| 2025 average Afore commission: 0.547% of balance (down from 0.566%); range 0.52–0.55% | 2025 | [Infobae](https://www.infobae.com/mexico/2024/11/29/estas-seran-las-comisiones-que-cobraran-las-afores-en-2025-segun-la-consar/) |
| Employer contribution ramp: 6.5% (2020) → 15% (2030); replacement rate for ≤5 minimum-wage earners: 31% → 54%; ~71% average for new retirees under reform | 2020 reform, ongoing | [El Contribuyente](https://www.elcontribuyente.mx/2020/07/presentan-reforma-a-pensiones-con-aumento-a-aportaciones-patronales-y-menos-semanas-de-cotizacion/), [FIAP](https://www.fiapinternacional.org/mexico-reforma-de-pensiones-del-2020-elevo-tasa-de-reemplazo-al-72/) |
| 27% of 67.7M Afore accounts are "assigned" (never chosen); varies 5%(XXI Banorte)–49%(PensionISSSTE) by administrator | Recent (exact date on source page not confirmed) | [ElCEO](https://elceo.com/negocios/afores-competiran-por-administrar-119000-mdp-de-cuentas-inactivas-del-sar/) |
| 18.45M workers reportedly unaware they have an Afore (expert estimate, not CONSAR-attributed) | 2021 article | [ElCEO](https://elceo.com/economia/mas-de-18-millones-de-trabajadores-desconocen-que-tienen-afore/) — **treat as dated/lower-confidence** |
| CONDUSEF SIPRES: 174 institutions cumulatively reported impersonated through Nov 2024; ongoing batches of 8–16/month through 2025 | 2024–2025 | [CONDUSEF](https://www.condusef.gob.mx/?p=contenido&idc=2527&idcat=1) |
| 113,824 total fraud cases reported nationally (all types, not investment-specific) | 2024 | Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública (cited via search aggregation — **primary link not directly fetched, verify**) |
| Bitso: 4.4M users in Mexico (+13% YoY); 9M across LatAm | End 2024 | [El Universal](https://www.eluniversal.com.mx/cartera/crecimiento-de-criptomonedas-en-mexico-alcanza-13-bitso-reporta-44-millones-de-usuarios-en-2024/) |
| ~3.1M people hold crypto in Mexico (2.5% of population, +15% YoY); Mexico = LatAm's #3, world's #16 by adoption | 2024 | Secondary aggregator (SDPnoticias) — **lower confidence, primary source (e.g. Chainalysis) not verified** |
| ENIF 2021: 56.7M people 18–70 (67.8%) hold a formal financial product; only 8% took a financial-education course; budgeting behavior fell 34.9%→22.5% (2018→2021); simple-interest concept understood by 91.2%, but only 45.0% could calculate it correctly | 2021 | [CNBV/INEGI ENIF 2021](https://www.cnbv.gob.mx/Inclusi%C3%B3n/Anexos%20Inclusin%20Financiera/Reporte_Resultados_ENIF_2021.pdf) |

---

## Mexico-specific mechanics

**GAT nominal vs. GAT real (Ganancia Anual Total)**
- GAT is the Banxico/CONDUSEF-standardized indicator for total return on savings/deposit products.
- **GAT nominal**: the annualized return after commissions/costs, *not* adjusted for inflation.
- **GAT real**: GAT nominal minus Banxico's median expected inflation for the next 12 months; can be **negative** if nominal return doesn't beat expected inflation.
- Official calculator: [Banxico waGAT](https://www.banxico.org.mx/waGAT/); official explanatory document: [Banxico GAT PDF](https://www.banxico.org.mx/sistema-financiero/d/%7BEFA9598F-0AE4-1C30-22B7-09773475697A%7D.pdf); consumer-facing explainer: [BBVA México](https://www.bbva.mx/educacion-financiera/banca-digital/portabilidad-de-nomina/portabilidad-que-es-gat-real.html).
- Every fintech/SOFIPO savings product checked (Nu, Klar, Stori) publishes GAT nominal prominently in marketing and GAT real in a secondary/legal-disclosure location — confirmed for Nu specifically (7.30–7.57% nominal vs. 3.24–3.49% real for 2026 published rates).

**CETES / Cetesdirecto**
- Government-run direct-retail-bond platform (via Banco del Bienestar), the "default" low-friction entry point to formal investing for retail Mexicans.
- Grew from ~1.1M users (implied, end of 2022) to 1.95M (end 2023, +120%) to 2.7–2.76M (2025), with an explicit roadmap to 3M users by 2026 and a planned move to 24/7 deposits/withdrawals to support that.
- Notably, user count keeps growing even as invested balances fell ~54% in 2025 — consistent with users chasing the previously very high CETES yields and pulling money out as Banxico's policy rate (and CETES yields) declined from their 2023–early 2024 peak.

**AFORE fees and the assignment mechanism**
- If a new formal-sector worker doesn't choose an Afore within roughly a year, CONSAR auto-assigns one (historically to better-performing/lower-fee administrators); if the account keeps receiving contributions without the worker ever choosing, CONSAR can reassign it again.
- Result: an estimated 27% of all Afore accounts (of ~67.7M total) are "assigned," with huge disparity by administrator (concentration of assigned accounts in PensionISSSTE and Sura vs. very low assignment rates at Coppel and XXI Banorte, likely reflecting differences in employer/onboarding channels).
- System-average management fee for 2025 is 0.547% of the administered balance — a figure that sounds small but compounds materially over a 30–40 year working life; CONSAR's own framing is that recent fee cuts alone represent 9 billion pesos of additional worker savings by 2030 (on top of 166 billion pesos from previous cuts).

---

## Existing players and their gaps

| Player | What it does | Gap observed |
|---|---|---|
| GBM+ | Dominant retail brokerage app (~92% of brokerage accounts in 2022 data) | Concentration risk / lack of competition; still only reaches ~2% of adults |
| Kuspit, Actinver/Bursanet, Finamex, Vector, Vifaru | Smaller brokerages, some fee/education-focused | Tiny share individually; fragmented data, hard to compare products |
| Cetesdirecto (gov't) | Free, simple, government-backed CETES access | Balances swing hard with rate cycles (users chase yield, don't stay invested); UX limitations (no 24/7 deposits until planned 2026 change) |
| Nu México, Klar, Stori, Hey Banco | High nominal-yield savings ("Cajitas"/"Apartados"/"Fondo de Rendimientos") | GAT real prominence gap (see pain point #1); rates change frequently and are hard to compare in real terms across apps |
| CONDUSEF (SIPRES) | Registry to check if an entity is legitimately registered | Manual, pre-transaction lookup only; not integrated into any transfer flow; consumer must know to check |
| CNBV | Warns about unauthorized entities; points to IOSCO/NASAA | No independent Mexico-specific, API-accessible blacklist found; reactive, not real-time |
| CONSAR | Regulates Afores, publishes fee caps, reassigns inactive accounts | Passive on engagement — doesn't proactively push workers to check/choose their Afore beyond reassignment after the fact |
| Bitso | Dominant Mexican crypto exchange | Banxico/Ley Fintech bars banks from offering crypto directly to clients, so activity stays concentrated off the banking rail, with fewer consumer protections than banked products |

---

## What is UNVERIFIED

- **"49.6 million accounts by Feb 2026"** figure surfaced in one aggregated search result (citing a non-primary source, itiger.com) claiming parity with the economically active population. This looks inconsistent with the more reliable AMIB 31M (May 2025)/15.77M (Dec 2024, brokerage-only) figures unless it conflates brokerage accounts + fund accounts + multiple accounts per person. **Do not use without locating the primary AMIB release.**
- **Exact date/primary source for the "27% of Afore accounts are assigned" statistic** — captured via search aggregation from an ElCEO article; the underlying CONSAR data table was not directly fetched/confirmed.
- **"18.45 million workers unaware they have an Afore"** — from a 2021 article attributing the figure to an academic expert, not explicitly to CONSAR; likely outdated and should not be quoted as a current official statistic.
- **113,824 fraud cases in 2024** — sourced via search aggregation to the Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública; primary dataset not directly verified, and the figure almost certainly includes non-investment fraud (card fraud, phishing, etc.), so it should **not** be used as an investment-fraud-specific victim count.
- **"3.1 million crypto holders in Mexico, 2.5% of population" (2024)** — from a secondary aggregator article; the primary source (likely a Chainalysis-style global adoption index) was not directly confirmed.
- **OECD/INFE 2023 Mexico-specific financial-literacy score** — could not retrieve the exact numeric score for Mexico (the OECD publication page returned an access error, and search results only confirmed Mexico participated with a caveat that its sample "may not be representative"). The specific 0–100 score is **UNVERIFIED** in this research pass.
- **Reddit anecdotal evidence (r/MexicoFinanciero, r/MexicoBursatil)** — targeted searches for real user complaints about fraud/investment experiences on these subreddits did not surface usable results through the search tool available in this session. This does not mean such complaints don't exist — it means they were **not independently verified here**; a direct Reddit browse (not available in this research pass) would be needed.
- **Banxico's Circular 4/2019 / Ley Fintech Art. 30 primary text** — the substance (banks barred from offering virtual-asset services directly to clients; no Banxico-approved asset list published) is corroborated by multiple legal-commentary sources and a law firm's public statement, but the primary regulatory text itself was not directly fetched and quoted in this pass.
- **Nu México's Mexico-specific account/user count for savings products specifically** (as opposed to LatAm-wide Nu figures) was not isolated with confidence.

---

## Fit-with-challenge-tracks verdict (honest)

**The challenge tracks are built around transaction streams — and most of the strongest retail-investor pain points here are NOT naturally observable in a transaction stream. This angle is a partial, not a strong, fit.**

Breaking it down honestly:

- **AFORE choice/inertia** is fundamentally a one-time, low-salience *enrollment* decision made at labor-market entry, and "has this person ever actively chosen an Afore" is a status flag sitting in CONSAR/Afore systems — it doesn't show up as a repeating, interpretable pattern in someone's bank transaction stream. A transaction-stream product could, at best, *notice* recurring/one-off SPEI transfers to an Afore-linked CLABE (voluntary contributions) and nudge on their absence — but that's a thin, indirect signal, and confirming "no Afore chosen" would still require external CONSAR/Afore data the challenge likely doesn't grant.
- **GAT nominal vs. real confusion** is a *point-of-sale/marketing disclosure* problem (what's shown when the product is sold), not something that unfolds across a transaction stream — though there is a real, narrow angle: a stream that captures actual interest-credit line items over time could recompute the *realized* yield and compare it to CPI, converting an abstract "GAT real: 3.4%" into "you gained 43 pesos of real purchasing power this month," which is a genuinely stream-native insight.
- **Ponzi/fraud victimization** is the pain point that fits best, but even here the *initial* exposure (a WhatsApp pitch, a social-media ad, a friend's referral) happens entirely outside any transaction stream. What a stream *can* plausibly see: an outbound-transfer pattern to a small, previously-unseen recipient that matches known Ponzi cadence (steady small "return" payouts credited in, escalating principal debited out, sudden stoppage of inbound credits), or transfers to a CLABE/name matching CONDUSEF's SIPRES fraud-impersonation list or CNBV's unauthorized-entity warnings. This is a legitimate, narrow, transaction-stream-native anomaly-detection use case.
- **Overall market-growth stats (31M investors, GBM dominance, Cetesdirecto growth)** are useful for sizing the opportunity but are not, themselves, pain points a transaction-stream product addresses — they describe adoption, not a solvable friction.
- **Crypto/Ley Fintech restrictions** are a regulatory-posture fact, not a product opportunity addressable via transaction data at all.

**Bottom line:** if the team wants to pursue this angle, it should be narrowed hard to (a) transaction-pattern-based fraud/Ponzi early-warning and (b) a "realized real yield" translator computed from actual interest-credit transactions — and should not lean on AFORE inertia or general market-growth stats as if they were stream-addressable, because they aren't.

---

## Product opportunity hypotheses

1. **Fraud/Ponzi Early-Warning from Transfer Patterns (best fit for a transaction-stream challenge).** Monitor a user's outbound-transfer stream for signatures consistent with unregistered "financiera"/Ponzi participation: transfers to a previously-unseen small non-bank recipient, a rhythm of modest "return" credits followed by escalating principal debits, sudden concentration of transfers to one new counterpart, and/or a recipient name/CLABE matching CONDUSEF SIPRES impersonation reports or CNBV's unauthorized-entity warnings. Surface a plain-language warning before/at the next transfer to that recipient. This is the one idea that is genuinely native to a transaction stream and addresses a real, evidenced harm (documented 2023–2025 cases with concrete peso losses).

2. **Realized Real-Yield Translator.** For savings products whose interest-credit transactions appear in the stream (Cajitas, Apartados, Fondos de Rendimiento, Cetesdirecto payouts), recompute the user's *actual realized* yield over a trailing period and translate it into an inflation-adjusted, plain-language "you kept/lost N pesos of real value this month" statement, replacing the abstract GAT-nominal-vs-real framing that ENIF 2021 data suggests most users can't calculate on their own. Moderate fit — it uses the stream, but the underlying pain (marketing emphasis on nominal over real rates) is really a disclosure/UX problem more than a behavioral one.

3. **(Weaker/stretch) Afore Engagement Nudge.** Detect payroll-deposit patterns in the stream and, where the product can also access CONSAR/Afore account status (external data, not the raw transaction stream itself), nudge workers who are on an "assigned" Afore or have never made a voluntary contribution. Flagged as the weakest fit of the three: the core problem (never having chosen an Afore) isn't visible in a transaction stream at all, and the feature only works if the challenge grants access to Afore/CONSAR data alongside transactions — confirm data-access scope before committing to this one.
