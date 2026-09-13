# Sentinel Enterprise Pitch

## Positioning

Sentinel is a real-time payment protection layer for banks and fintechs operating instant payment rails. It detects social-engineering coercion and authorized push payment fraud before the transfer is submitted, then applies reversible friction: allow, challenge, or protected pause.

The business message is simple:

> Authentication proves who is holding the phone. Sentinel asks whether that authenticated customer is being manipulated right now.

## Executive Buyer Narrative

Instant payments created a customer experience advantage, but they also compressed the fraud response window from hours to seconds. Traditional fraud controls are strong at stolen credentials and unauthorized access. They are weaker when the legitimate customer is present, authenticated, and pressured by a scammer to move money voluntarily.

Sentinel closes that gap by combining three evidence groups:

- Account takeover and session risk: new device, high-risk IP or location, recent credential changes.
- Intent and coercion risk: active call, screen share, remote access, sudden amount deviation, regulatory-cap structuring.
- Recipient risk: first-time destination, recently added beneficiary, suspicious fan-in behavior.

The product does not block a customer because of one signal. It requires corroboration across independent dimensions, which is the core enterprise value: protection without turning legitimate payments into a support burden.

## Highest-Value Selling Points

### 1. Protects the moment current fraud systems miss

Most banking controls answer: "Is this the real user?" Sentinel answers: "Is the real user under pressure?" That reframes the product from another fraud score into a missing control for authorized payment scams.

### 2. Prevents loss before settlement

SPEI and other instant payment rails settle fast. Post-transaction investigation is expensive and often too late. Sentinel sits in the pre-submission path and returns a synchronous decision before money leaves the account.

### 3. Low-friction by design

The multi-factor corroboration rule is a strong buyer message. A new beneficiary alone is not enough. A high transfer alone is not enough. Sentinel intervenes when signals agree, reducing unnecessary customer friction.

### 4. Customer trust, not only fraud reduction

The product can be sold as customer protection and brand protection. It gives the bank a concrete way to tell customers: "We protect you even when scammers try to manipulate you into authorizing the transfer yourself."

### 5. Explainable decisions

Sentinel returns reason codes, signal breakdowns, and customer-facing Spanish guidance. This matters for risk teams, compliance teams, call-center operations, and product teams because interventions are auditable and explainable.

### 6. Enterprise-ready integration path

The MVP has a clear API contract:

- `POST /v1/events` for append-only ledger and security telemetry.
- `POST /v1/evaluate` for real-time transfer evaluation.
- `POST /v1/decisions/{id}/outcome` for feedback loops.
- `GET /v1/evaluations` and `GET /v1/evaluations/{id}` for dashboards and audits.

The architecture is stateless at the API layer, persists state in PostgreSQL, and is containerized for cloud portability.

### 7. Demonstrable proof, not slideware

The repository includes a simulator, dashboard, hidden labels, and benchmark harness. The demo can show the buyer the fraud story, the customer message, the bank dashboard, and the measured performance in one flow.

## Enterprise Buyer Map

| Stakeholder | What They Care About | Message |
|---|---|---|
| Chief Risk Officer | Loss prevention, model governance, false positives | Sentinel adds an explainable pre-submission control for authorized scams without relying on single-signal blocks. |
| Fraud Operations | Fewer manual reviews, clearer escalations | Decisions include reason codes and customer outcomes, giving analysts structured evidence. |
| Digital Banking/Product | Customer experience, conversion, trust | Sentinel applies reversible friction only when multiple risk dimensions corroborate. |
| CIO/CTO | Integration cost, latency, scalability | API-first, stateless, containerized, PostgreSQL-backed, synchronous low-latency evaluation. |
| Compliance/Legal | Auditability, fair treatment, controls | Every evaluation stores signals, reasons, decision, customer message, ruleset version, and outcome. |
| CFO/Business Sponsor | ROI, avoided losses, brand impact | Value can be modeled from prevented transfer losses, reduced reimbursements, fewer support escalations, and retention from trust. |

## Recommended Deck Structure

### Slide 1: Title

**Sentinel: Real-Time Protection Against Coerced Instant Payments**

Subtitle: Detecting social-engineering manipulation before money enters the rail.

### Slide 2: The Market Problem

Instant payments are fast, final, and customer-friendly. Scammers exploit that speed by manipulating authenticated customers into approving their own transfers.

Key point: existing authentication can be correct and still produce a fraudulent payment.

### Slide 3: The Control Gap

Traditional fraud question:

> Is this the authorized user?

Sentinel question:

> Is this authorized user acting under coercion?

Use a simple two-column comparison: authentication fraud vs. authorized scam/coercion fraud.

### Slide 4: Product Answer

Sentinel evaluates every proposed transfer across ATO, intent, and recipient dimensions. It returns allow, challenge, or pause with explainable reasons and customer-facing guidance.

### Slide 5: Why Buyers Should Believe It

Show the benchmark:

- 615 simulated transfers.
- 6 APP fraud attempts intercepted.
- 3 ATO attacks intercepted.
- 100% simulated APP and ATO recall.
- 0.0% simulated false positive rate for consumers and merchants.
- In-request latency measured in milliseconds.

Label this clearly as synthetic benchmark evidence, not production performance.

### Slide 6: Customer Experience

Show the protected pause. The message is not generic. It tells the customer why the bank is pausing and what scam pattern may be happening.

Business message: education at the exact moment of risk is more powerful than generic awareness campaigns.

### Slide 7: Bank Operating Model

Show the API flow:

1. Bank streams ledger and security events.
2. Bank calls `/v1/evaluate` before SPEI submission.
3. Sentinel returns a decision and explanation.
4. Bank reports outcome for feedback and governance.

### Slide 8: ROI Logic

Use a conservative model:

```text
Annual value = prevented scam value
             + reduced reimbursement exposure
             + reduced fraud operations cost
             + reduced reputational/customer trust loss
             - integration and operating cost
```

For the hackathon demo, use the benchmark value at risk as proof of mechanism, not as a market-size claim.

### Slide 9: Why Now

Fraud is shifting toward manipulation, impersonation, and authorized transfers. Real-time rails make delayed detection less useful. Banks need real-time, explainable, customer-sensitive intervention.

### Slide 10: Ask

Pilot Sentinel on a narrow payment flow:

- one product line,
- selected customer segment,
- shadow-mode evaluation first,
- then controlled challenge/pause interventions,
- success measured by fraud interception, false positive rate, latency, and customer completion.

## Competitive Differentiation

| Alternative | Limitation | Sentinel Advantage |
|---|---|---|
| Authentication-only controls | User may be legitimate but manipulated | Detects coercion context after authentication. |
| Rules-only fraud engines | Often brittle and noisy | Corroborates independent dimensions and stores explanations. |
| Post-transaction monitoring | Too late for instant rails | Evaluates before submission. |
| Generic customer education | Delivered outside the moment of pressure | Delivers specific warning during the risky action. |
| Black-box scores | Harder for enterprise governance | Returns reasons, signals, and ruleset version. |

## Business Development Strategy

Enterprise B2B buying is non-linear and involves multiple stakeholders. The pitch should support buyer confidence, not only feature awareness.

Recommended sales motion:

1. Lead with business pain: authorized fraud, irreversible instant payments, customer trust.
2. Prove the gap: authentication succeeds while the customer is being manipulated.
3. Show live demo: scam setup, evaluation, protected pause, dashboard, outcome.
4. Quantify pilot value: value at risk, false positives, latency, support impact.
5. De-risk adoption: shadow mode, narrow segment, audit logs, clear rollback.
6. Expand: more payment types, more telemetry, stronger recipient-network intelligence.

## Objection Handling

### "We already have fraud detection."

Sentinel is not a replacement for existing fraud stacks. It is a missing pre-submission control for authorized manipulation, where normal authentication can be correct.

### "We cannot add friction to payments."

Sentinel is designed around corroboration. It avoids blocking on single signals and supports graded outcomes: allow, challenge, or pause.

### "Synthetic results are not enough."

Correct. The MVP proves mechanism and integration shape. The next step is a shadow-mode pilot with bank historical data and agreed success thresholds.

### "This may create compliance risk."

The system stores the decision, reason codes, signal evidence, ruleset version, customer message, and outcome. That creates an auditable intervention trail.

### "Integration sounds expensive."

The API surface is intentionally small: ingest events, evaluate proposed transfer, report outcome, stream evaluations. A pilot can start with existing ledger events plus mobile session telemetry.

## Source-Informed Sales Principles Applied

- Gartner describes B2B buying as a non-linear set of buying jobs: problem identification, solution exploration, requirements building, supplier selection, validation, and consensus creation. The pitch therefore includes proof, stakeholder-specific messages, and pilot de-risking.
- Gartner also emphasizes helping buyers quantify value and build confidence with digital tools and human guidance. Sentinel's demo, dashboard, benchmark, and ROI model serve that buyer-enablement role.
- McKinsey emphasizes superior value propositions and business impact, not feature lists. Sentinel's pitch should stay anchored in avoided loss, customer trust, operational efficiency, and explainable governance.
- FTC, FDIC, FBI, UK Finance, and the UK Payment Systems Regulator all show that impersonation, social engineering, APP fraud, and bank-transfer scams are material and current risks. Use these as external context, while marking Mexico-specific market sizing as `TODO: Verify` unless sourced directly.

## External References

- Gartner, "The B2B Buying Journey": https://www.gartner.com/en/sales/insights/b2b-buying-journey
- Gartner, "Improve Digital Engagement to Support B2B Buying Journeys": https://www.gartner.com/en/documents/5083031
- Gartner, "Gartner Survey Finds 69% of B2B Buyers Turn to Sales Reps to Validate AI-Generated Insights": https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights
- McKinsey, "Delivering value to customers": https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/delivering-value-to-customers
- McKinsey, "The basics of business-to-business sales success": https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-basics-of-business-to-business-sales-success
- FTC, "New FTC Data Show a Big Jump in Reported Losses to Fraud to $12.5 Billion in 2024": https://www.ftc.gov/news-events/news/press-releases/2025/03/new-ftc-data-show-big-jump-reported-losses-fraud-125-billion-2024
- FDIC, "Bank Impersonation Scams and Fake Banks": https://www.fdic.gov/consumer-resource-center/2025-06/bank-impersonation-scams-and-fake-banks
- FBI IC3, "Business Email Compromise: The $55 Billion Scam": https://www.ic3.gov/PSA/2024/PSA240911
- UK Finance, "Fraud continues to pose a major threat with over £1 billion stolen in 2024": https://www.ukfinance.org.uk/news-and-insight/press-release/fraud-report-2025-press-release
- Payment Systems Regulator, "APP fraud performance data": https://www.psr.org.uk/app-fraud-data/

