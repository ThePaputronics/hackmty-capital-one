# Direction of Record — SPEI Fraud Interception and the CLABE Flag Registry

**Status:** direction of record as of 2026-09-12, owner-directed.
Supersedes the coach-led hybrid recorded in `challenge-brief.md` on 2026-09-11.
The prior decision is preserved there as superseded, not deleted.

## 1. Sponsor scope clarification (new, 2026-09-12)

The owner relayed that Capital One clarified the submission **does not need to
solve a Capital One problem or target Capital One as the customer.** It should be
innovative and capable of changing the Mexican financial system.

This materially changes the target audience. The submission is now framed as a
**proposal to Banco de México**, with Capital One evaluating in the role of the
central bank / rail operator. Consequences:

- The "who would operate this?" objection dissolves — the audience is the
  operator. National infrastructure is a legitimate proposal, not overreach.
- The owner's ~100M-user scale target stops being aspirational and becomes the
  literal addressable population of the rail.
- Secreto bancario (Art. 142 LIC) stops being a blocker. It constrains third
  parties; it does not constrain the institution that operates SPEI.
- Evaluation weight shifts from product polish to systemic gap, legal basis,
  governance, rights, and adoption path.

## 2. The direction

A **two-layer system**:

**Layer 1 — Pre-submission intent guard (the product surface, and the demo).**
Scores a transfer in the seconds before submission and inserts reversible,
explained friction when evidence suggests the payer is being manipulated. All
inputs are the payer's own observed behavior.

**Layer 2 — A CLABE-scoped flag registry (the standard, and the network effect).**
Account-level fraud flags, no names, no addresses, no amounts. This is what lets
Layer 1 work beyond a single institution's book.

Layer 1 works standalone and has no abuse surface. Layer 2 is what makes the
pitch systemic. **If only one ships cleanly, ship Layer 1.**

## 3. Why the problem is structural, not neglect

- SPEI identifies a payment **only by CLABE**. The beneficiary name displayed
  verifies nothing.
- A settled transfer is firm, irrevocable, and enforceable against third parties.
- When the victim authenticated and authorized, neither bank is automatically
  liable, so the loss sits with the victim.
- CONDUSEF/BEF logged **1.515M fraud complaints in Q1 2026** (+31.5% YoY, ~75% of
  all complaints against financial institutions); **5.201bn pesos claimed,
  1.265bn returned (24.3%)**.

**No third party can fix the receiver side.** There is no public CLABE registry
of any kind, and secreto bancario blocks the private route. Only the operator of
the rail can. That is the argument for why this must be proposed to Banxico
rather than built as a fintech overlay.

## 4. The MTU evasion thesis (our original contribution)

Two published facts, not previously combined:

- **94.6%** of SPEI user transactions are at or below **1,500 UDIS**
  (Banco de México, 2025; 7,308.1M transfers processed that year).
- The **default MTU cap is 1,500 UDIs** (~$12,800 MXN), mandatory on banks since
  1 Oct 2025, with user configuration mandatory from 1 Jan 2026.

The regulator drew the cap at the top of normal behavior so it would not
inconvenience the other 95%. A scammer therefore has two options, both leaving
marks in the stream:

- **Stay under the line** → repeated sub-cap transfers to the same first-time
  beneficiary, compressed in time (structuring signature).
- **Move the line** → coach the victim into a self-service MTU increase,
  immediately followed by a transfer to a beneficiary registered minutes earlier.

**This inference is ours. Neither source states it.** Present it as reasoning,
never as a citation. Design consequence: the registry and the guard must both
capture **MTU configuration changes**, not only transfers.

To a bank this is a detection feature. To Banxico it is **feedback on their own
policy instrument**, which is a stronger pitch to that audience.

## 5. Precedent — Brazil's DICT fraud marking

Banco Central do Brasil already operates account-level fraud marking inside DICT,
the Pix key directory. This is the single strongest validation available.

**VERIFIED against BCB primary documentation (DICT API v2 FAQ):**
- An institution may create a fraud marking **only against its own customer**.
- A marking must be tied to **a specific Pix transaction**.
- Markings are created unilaterally and close immediately; refund-request
  infraction reports differ and require counterparty analysis within 7 days.
- Markings display on tiered windows of **90 days, 12 months, and 60 months**;
  beyond 60 months they become invisible to DICT users.

**VERIFIED as to instrument and date (Resolução BCB nº 506, 26 Sep 2025, in force
30 Sep 2025):** introduced transactional fraud marking and requires PSPs to hold
an internal policy defining criteria, triggers, and governance. Sourced from the
resolution record and convergent legal/industry analysis, not from the BCB text
itself — pull the primary before quoting specifics.

**SECONDARY SOURCES ONLY — do not present as verified:**
- That from Oct 2025 a marked key stops being disclosed to the system, in effect
  blocking its use in Pix.
- That the marking follows the key across institutions.
- A "contas laranja" (mule account) category. **Not found** in the BCB page
  checked; appeared only in vendor material.
- Reports of innocent receivers having balances blocked and accounts marked.

## 6. Why Mexico's version can be better than Brazil's

Brazilian legal commentary and press already describe people who unknowingly
received scam funds having balances blocked and accounts marked — the same
"abuelita account" harm identified in our own adversarial review. Two Brazilian
design choices drive it:

| Dimension | Brazil (DICT) | Proposed for Mexico |
| --- | --- | --- |
| What is marked | CPF/CNPJ — the **person's** tax ID | **CLABE only** — the account, no person data |
| Effect of a flag | Auto-block; key withheld from the system | **Informs the payer's own decision**; never blocks, never instructs a bank |
| Output shown | Effectively a verdict | **Evidence count** — "3 independent reports in 30 days" |
| Innocent receiver | Balance blocked, account marked | Pattern routes to **welfare outreach**, not restriction |

The pitch is therefore: *Brazil proved the mechanism works; here is what it is
costing innocent receivers; here is the Mexican version that fixes it using
instruments Banxico already operates.*

## 7. Governance non-negotiables

A missing one turns the registry into a weapon:

- **Evidence counts, never verdicts.** Never render a `SCAMMER` label.
- **Independent reporters, not report volume.** N distinct reporters, not N reports.
- **Standing must be earned by a transaction, not asserted.** Require a
  Banxico-sealed **CEP** as proof the reporter actually transferred to that
  CLABE. This raises attack cost from zero to real, traceable pesos, and lets the
  centre verify standing without seeing any private data. (Brazil's equivalent —
  only-your-own-customer — is arguably cleaner because the reporter is a
  supervised entity; both mechanisms are worth presenting.)
- **Decay.** Tiered visibility windows, as Brazil uses.
- **Right to know and contest**, designed in from the start. LFPDPPP grants ARCO
  rights including rectification and opposition.
- **Asymmetric consequence.** A flag informs a payer. It never blocks an account
  or propagates as an instruction to a bank.
- **No free burn-check.** If anyone can query any CLABE, criminals will test
  whether mule accounts are still clean. Rate-limit, answer only in the context
  of a pending transfer, never expose the underlying count.

## 8. Privacy position — state it correctly

**"CLABE only, no names" is pseudonymization, not anonymization.** Under LFPDPPP
personal data is data relating to an identified **or identifiable** person, and a
CLABE is trivially linkable to its holder by the issuing institution. The
registry therefore holds regulated personal data.

Do not claim an exemption that does not exist. The correct framing is:
pseudonymous, minimized, no names/addresses/amounts, with a stated consent basis,
retention limit, and contest process.

## 9. What is public about a CLABE (verified)

- **Public:** the 18-digit structure (3 institution + 3 plaza + 11 account +
  1 check digit), the weighted mod-10 check-digit algorithm, and the ABM-assigned
  institution code catalog. A CLABE can be validated and attributed to an
  institution **entirely offline**.
- **Public but not a lookup:** Banxico's **CEP** verifies a specific transfer,
  and requires the operation date, clave de rastreo, and both institutions. It
  cannot be queried by CLABE.
- **Not public:** CLABE → identity (secreto bancario), CLABE → history, any
  registry or enumerable directory.

Design consequence: the "unfamiliar destination" signal — *this CLABE is new to
you; you have never sent to this institution* — is computed **entirely locally**,
with no external data, no privacy exposure, and no attack surface.

`TODO: Verify` — whether digits 4–6 (plaza) still carry real geographic meaning.
Believed largely vestigial, with many institutions using a fixed value. Do not
build geographic inference on it without checking a real CLABE sample.

## 10. Scope boundaries settled in adversarial review

Four-question test for admitting any signal:

1. Can we legally and practically obtain this data?
2. Does it create a durable judgment about a third party who is not our user?
3. Can an adversary manufacture the input cheaply?
4. Does cutting it break the core thesis?

**Governing principle:** the moment a signal depends on someone *asserting*
something rather than *doing* something, it is an attack surface. Prefer observed
behavior over reported allegation.

**Ruled out for the prototype:**
- Scraping CONDUSEF. Complaints are filed **against institutions, not accounts**,
  so they contain no usable CLABE-level data; REDECO requires institutional
  onboarding; repurposing regulatory complaint data into a private score is a
  purpose-limitation problem under LFPDPPP.
- A prior spec item, "cross-reference destination CLABE against CONDUSEF's
  Monitor de Reportes," is **withdrawn** — existence of such a per-account
  database is unconfirmed. `TODO: Verify` before any reliance.
- Reporter-reputation / "griefer" scoring as a defense. Defeated by collusion
  (N friends each filing once). Transaction-anchoring replaces it.
- Any IFPE-licensed activity — holding or moving client funds.

## 11. Cold start

The registry cannot bootstrap from CONDUSEF. Seed it from **behavioral detections
contributed by participating institutions**, not user reports. This also keeps
the transaction stream central to the submission rather than letting it become a
database project.

## 12. Named failure modes — lead with these

1. **No public ground truth for APP fraud in Mexico.** CONDUSEF's categories
   capture transactions the customer says they did *not* authorize — the opposite
   of this fraud. We train on synthetic labels and say so first.
2. **False positives delay legitimate money.** Report the challenge rate as
   prominently as the detection rate.
3. **The innocent receiver.** The mule-account holder is usually a victim, often
   elderly. Vulnerability must raise the "being exploited" hypothesis above
   "criminal," and route to outreach rather than restriction.
4. **A legitimate merchant looks like a mule on fan-in alone.** Must be solved or
   the design flags most small businesses in Mexico.

## 13. Open questions

- `TODO: Verify` Brazil specifics against BCB primary text before any slide.
- `TODO: Verify` Banxico's legal authority to use SPEI traffic for this purpose.
  Note the CEP-anchored design deliberately avoids requiring it — a central bank
  is likelier to accept a protocol that does not oblige it to mine the rail.
- `TODO: Verify` the precise Banxico circular article establishing irrevocability
  and CLABE-only identification. Currently sourced from a CONDUSEF explainer via
  news coverage, not primary text.
- Adoption path: who joins first, and what is their incentive absent a mandate.
- Cost to small participating institutions.

## Sources

Owner relay of the sponsor scope clarification, 2026-09-12. Research corpus in
`docs/ai/research/mexico-discovery-2026-09/` (7 reports, each with citation
tables and unverified lists). Ranked map in `mexico-opportunity-map.md`.
Brazil precedent: BCB DICT API v2 FAQ (primary); Resolução BCB nº 506/2025
(record and convergent secondary analysis).
