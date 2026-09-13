# Sentinel Executive Speech

## 90-Second Version

Good afternoon. Sentinel is a real-time protection layer for instant payments.

The problem we are solving is not traditional account takeover alone. In many high-impact scams, the customer is real, the device is real, the password and biometrics are valid, and the bank's authentication system does exactly what it was designed to do. But the customer is being manipulated on a phone call, through screen sharing, or by a fake bank representative into authorizing a transfer themselves.

That creates a dangerous blind spot. The bank can confirm identity, but still miss intent.

Sentinel closes that gap. Before a SPEI transfer is submitted, the bank calls Sentinel with the proposed payment and recent customer context. Sentinel evaluates three dimensions at the same time: account takeover signals, coercion and intent signals, and recipient risk. It does not pause a payment because of one suspicious detail. It requires corroboration across independent signals, which is how we protect customers without creating unnecessary friction.

The output is simple: allow, challenge, or pause. But behind that decision, Sentinel returns explainable reason codes, signal evidence, and a customer-facing warning in Spanish. That matters because the intervention is not just a block. It is education at the exact moment the scammer is applying pressure.

In our benchmark, Sentinel evaluated 615 simulated transfers, intercepted all simulated APP fraud attempts and ATO attacks, and produced a zero percent simulated false positive rate for regular consumers and small merchants. Those are synthetic results, so the right next step is not a broad launch. The right next step is a controlled pilot: run Sentinel in shadow mode, measure fraud interception, false positives, latency, and customer outcomes, then activate protected pauses for the highest-confidence cases.

The business value is direct: reduce scam losses before settlement, reduce operational burden after fraud occurs, protect customer trust, and give the bank an auditable control for a fraud category that is growing around real-time payments.

Our thesis is simple: instant payments need instant intent protection. Sentinel provides it.

## 3-Minute Version

Good afternoon. We built Sentinel for a specific failure mode in modern banking: the moment when authentication is correct, but the customer's intent has been compromised.

Instant payment systems like SPEI are excellent for customers because they are fast and convenient. But that same speed creates a fraud window measured in seconds. Once the money moves, recovery is difficult, expensive, and often impossible.

Most fraud systems were designed around the question: "Is this the authorized user?" That is still important. But social-engineering scams exploit a different weakness. The customer may be fully authenticated, using their own device, and passing every normal login control. The issue is that someone is pressuring them in real time: a fake bank agent, a virtual kidnapping threat, a remote-access scam, or a screen-sharing manipulation.

That is why Sentinel asks a different question: "Is this authenticated customer being manipulated right now?"

Technically, Sentinel is a pre-submission risk API. The bank sends ledger events and session telemetry, then calls `/v1/evaluate` before executing the payment. Sentinel checks three independent evidence groups.

First, account takeover risk: new device, suspicious network, recent credential changes.

Second, intent and coercion risk: active phone call, screen sharing, remote access, sudden deviation from usual amounts, or transfers structured around regulatory limits.

Third, recipient risk: first-time destination, recently added beneficiary, or suspicious recipient patterns.

The product's key design choice is corroboration. We do not want to punish normal customer behavior. A new beneficiary alone is not enough. A higher amount alone is not enough. Sentinel intervenes when several independent signals tell the same story.

When that happens, the bank gets one of three decisions: allow, challenge, or pause. It also gets reason codes, explainable signals, and customer-facing Spanish copy. That lets the bank turn a fraud score into an actual protective experience: "Stop. This pattern matches a scam. Your bank will never ask you to move money to a safe account."

For executives, the value is not just technical. Sentinel supports four business outcomes.

First, avoided losses: stopping authorized scams before funds enter the rail.

Second, lower operational burden: fewer expensive post-transaction investigations and clearer evidence when fraud teams review cases.

Third, customer trust: the bank demonstrates protection at the customer's most vulnerable moment.

Fourth, governance: every evaluation is auditable with signals, reason codes, ruleset version, and outcome.

The MVP is also built to be shown, not just described. It includes a simulator, a bank-player service, a dashboard, hidden ground truth labels, and an evaluation harness. In the benchmark, Sentinel evaluated 615 transfers, intercepted all simulated APP fraud and ATO attempts, and kept simulated false positives at zero for both regular consumers and small merchants. We are careful with that claim: this is synthetic evidence, not production proof. But it proves the mechanism and gives us a disciplined path to a pilot.

The pilot plan is low risk. Start in shadow mode. Evaluate real transactions without affecting customers. Measure latency, false positives, fraud detection, and operational review quality. Then activate protected pauses only for high-confidence scenarios, with clear rollback and monitoring.

The market timing is strong. Fraud is moving toward impersonation, manipulation, and authorized transfers. Real-time payment rails need controls that are equally real time. Sentinel gives banks a practical way to protect customers without making every payment feel suspicious.

Our closing message is this: authentication confirms identity. Sentinel protects intent. For instant payments, banks need both.

## Demo Talk Track

1. "This customer is legitimate and authenticated. That is the point."
2. "The scammer's advantage is pressure and speed: call active, new beneficiary, unusual amount, immediate transfer."
3. "Sentinel evaluates the transfer before submission, not after settlement."
4. "Notice that no single signal is enough. The decision changes because the signals corroborate."
5. "The bank receives an explainable decision, and the customer receives a specific warning in Spanish."
6. "The dashboard separates what the bank sees from hidden simulation ground truth, so we can measure performance honestly."
7. "The pilot path starts with shadow mode, then controlled activation."

## Closing Line Options

- "Authentication protects access. Sentinel protects intent."
- "Real-time payments need real-time protection before the money moves."
- "Sentinel turns fraud prevention from a post-mortem into a pre-submission customer protection moment."
- "The safest payment is the fraudulent transfer that never enters the rail."

