# Mexico financial-agent opportunity map

## Decision summary

**First choice: the selected wellness-plus-anomaly hybrid, narrowed to
payday resilience with Transfer Guardian.** The product surface remains a
consumer financial-wellness coach; its highest-risk real-time agent is an
explainable, pre-send SPEI check for salaried workers and households. This
implements the owner-selected hybrid in
[the canonical challenge brief](challenge-brief.md), rather than re-scoping the
project to a pure fraud product. It should be framed as user-side decision
support, never as a fraud verdict, bank control, or automated freeze.

**Backups:** (1) a commitment-aware 30-day liquidity copilot for formal small
businesses; (2) a payday resilience guardrail for low-buffer payroll users.

## Evidence boundary

All statistics below are verified facts from the linked source. Product gaps,
user willingness, and proposed features are hypotheses unless explicitly marked
otherwise. This report does not claim any problem is unique to Mexico.

## Ranked opportunity map

| Rank | Opportunity | User / track | Evidence and pain point | Direction and streaming demo | Key constraints |
| --- | --- | --- | --- | --- | --- |
| 1 | Transfer Guardian | Households and salaried mobile-banking users / Risk & Security | CONDUSEF reported 13,631 unrecognized electronic transfers among 72,873 possible-fraud cases in 2025; phishing/vishing and urgency tactics are documented. [CONDUSEF 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-DIC-2025.pdf), [fraud guidance](https://www.condusef.gob.mx/index.php/i?p=tipos-de-fraude) | Stream transfers; flag new beneficiary + unusual amount/velocity/hour + balance depletion; explain and require reversible user confirmation. | Explicit consent; minimize financial data; no freeze, reversal, report, or fraud determination. |
| 2 | Liquidity-before-deadline copilot | Formal micro/small commerce and services / B2B | In ENAFIN's covered firms, 25.8% cited financing cost and 20.7% lack of financing as growth constraints; 53.1% had a debt-management financial plan. [INEGI ENAFIN 2024](https://www.inegi.org.mx/contenidos/programas/enafin/2024/doc/Presentacion_ENAFIN.pdf) | Stream transfers plus manual cash, forecast 7/14/30 days, reserve user-confirmed commitments and show buffer breach. | ENAFIN excludes much of informality; no tax filing, payment initiation, or lending. |
| 3 | Payday resilience guardrail | Low-buffer payroll households / B2C | 45.9% of adults almost never/never have money left at month-end; 47% had savings of at most one fortnight's income. [INEGI ENSAFI 2023](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/ENSAFI/ENSAFI.pdf), [technical report](https://ensafi.condusef.gob.mx/pdf/IR-ENSAFI2023-CONDUSEF.pdf) | Stream payroll and commitments; project low-balance date and safe-to-spend amount; propose a virtual reserve, subject to approval. | Not underwriting, a credit score, or automatic savings. |
| 4 | Payment-confirmation fulfillment queue | PYMES that release goods/services after SPEI / Risk & Security + B2B | Banco de México's CEP records recipient-bank crediting and offers validation; screenshot-only payment proof is not equivalent to confirmation. [Banco de México CEP](https://www.banxico.org.mx/servicios/mi-spei_-transferencias-ban.html) | Match a claimed payment/order to an incoming transaction or CEP; label fulfill / pending / mismatch. | Mexico-wide fake-proof loss frequency was not established: **TODO: Verify**. |
| 5 | Cash-to-credit readiness dossier | Formal PYMES seeking capital / B2B | Rejection reasons include guarantees (21.9%), inability to prove income/meet requirements (21.6%), no history (18.4%), and repayment capacity (16.5%). [ENAFIN](https://www.inegi.org.mx/contenidos/programas/enafin/2024/doc/Presentacion_ENAFIN.pdf) | Turn consented ledger trends and user explanations into an editable 90-day cash-flow dossier and debt-service scenarios. | Not a score, approval prediction, lender referral, or data sharing without separate consent. |
| 6 | Hybrid cash/digital daily ledger | Informal and transitioning microbusinesses / B2B | 64.3% of census-counted units were informal in 2023; informal economy was 25.4% of 2024 GDP (preliminary). Cash was a customer payment method for 79.8% of ENAFIN-covered firms. [Economic Censuses](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/ce2024_mn00.pdf), [MEI](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/pibmed/MEI2024_CP.pdf), [ENAFIN](https://www.inegi.org.mx/contenidos/programas/enafin/2024/doc/Presentacion_ENAFIN.pdf) | Merge user-entered cash with transaction events into a 7-day buffer forecast. | Scale does not prove demand for software: validate with interviews; do not infer tax status. |

## Why the top three win

### 1. Transfer Guardian — recommended safety agent in the selected hybrid

**Problem.** A household is about to send an atypical SPEI transfer after a
scam or credential compromise. The immediate harm is observable and time
sensitive. Banco de México describes SPEI as the main rail for electronic
transfers and applies a 24-hour delay to certain virtual-asset-provider
transfers to allow legitimacy checks, supporting the value of a pause at a
high-risk moment. [Banco de México](https://www.banxico.org.mx/sistemas-de-pago/6--acciones-regulatorias-po.html)

**Why alternatives are insufficient.** Notifications exist, but a post-event
notification is not a pre-send decision aid; this is a product hypothesis, not
a national capability comparison. The defensible differentiation is a plain
language explanation tied to this transfer's behavior rather than a generic
security dashboard.

**MVP.** Synthetic normal transfers establish a baseline; a new-beneficiary,
late-night, high-amount burst produces: risk reasons, a confidence-aware
second-look screen, and a user choice to continue or use a short cooling
period. The success metric is the percentage of scripted high-risk transfers
interrupted with understandable reason codes while legitimate unusual transfers
can proceed after review.

### 2. Liquidity-before-deadline copilot

**Problem.** A formal small firm has cash in the account but cannot see whether
it is already committed to payroll, suppliers, debt, or a monthly tax payment.
Legal entities generally face monthly provisional/final tax-payment deadlines
by the 17th of the following month. [SAT](https://wwwmatnp.sat.gob.mx/declaracion/95291/declaracion-mensual-para-tu-empresa-en-el-servicio-de-declaraciones-y-pagos)

**MVP.** A synthetic mixed cash/transfer ledger updates a 30-day projection on
every event; an unexpected supplier debit causes a projected buffer breach;
the agent names the commitments driving it and proposes a reversible reserve or
reminder. The measure is forecasted commitment coverage before the due date.

### 3. Payday resilience guardrail

**Problem.** Formal account access does not imply an emergency buffer: ENIF
shows 33.6% reported no savings and 36.6% only informal savings in the prior
year. [INEGI ENIF 2024](https://www.inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)

**MVP.** On each transaction, forecast the next paycheck, recurring essentials,
and low-balance date. Present a conservative safe-to-spend value and a
user-confirmed virtual envelope. The measure is avoided predicted essential-
payment shortfalls across scripted scenarios.

## Responsible product boundary

- Financial/patrimonial data needs a privacy notice, purpose limitation,
  minimization, access/deletion controls, and (where applicable) express
  consent under the current Mexican private-sector data law. [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)
- Use synthetic or explicitly consented data in the prototype. Keep raw
  counterparties and account numbers out of alerts and logs.
- Agent actions must be reversible: explain, notify, ask for confirmation,
  schedule a reminder, or create a virtual plan. Do not autonomously move
  money, file a report, apply for credit, submit a tax return, freeze an
  account, or label a person fraudulent.
- Show data freshness, uncertainty, and user corrections. Evaluate false
  positives, especially for risk alerts and cash-flow classifications.

## Decisions before implementation

1. Confirm Transfer Guardian as the track and target segment, or select one
   backup.
2. Choose the intervention: warning only, or user-selectable cooling period.
3. Define synthetic data scenarios, including normal, suspicious, and
   legitimate-but-unusual transfers.
4. Approve a prototype data boundary, retention period, and consent language.
5. Define one demo metric and the threshold for a successful run.

## Sources

Primary sources are linked inline above. The most decision-critical are INEGI's
[ENIF 2024](https://www.inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf),
[ENSAFI 2023](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/ENSAFI/ENSAFI.pdf),
[ENAFIN 2024](https://www.inegi.org.mx/contenidos/programas/enafin/2024/doc/Presentacion_ENAFIN.pdf),
CONDUSEF's [2025 possible-fraud report](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-DIC-2025.pdf),
Banco de México's [SPEI/CEP material](https://www.banxico.org.mx/servicios/mi-spei_-transferencias-ban.html),
and the [LFPDPPP](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf).
