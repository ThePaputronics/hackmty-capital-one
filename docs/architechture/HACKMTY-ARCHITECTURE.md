# HackMTY Architecture

This diagram shows the current high-level architecture. The core MVP is an
API as a product for transfer-intent anomaly analysis. Bank interfaces and the
public CLABE lookup are optional extensions, shown to give the product
visibility and to indicate where it can evolve.

The canonical flow is defined in
[`ADR-0001`](ADR-0001-canonical-mvp-architecture.md). The API is the entry
point; risk scoring is called inside the request, not run ahead of it.

```mermaid
flowchart TB
    client["Bank app / client<br/>(proposes a transfer)"]

    subgraph mvp["MVP - API as a product"]
        direction TB
        api["API service<br/>POST / GET"]
        rules["Rule analysis service<br/>(payer baseline signals)"]
        ml["ML<br/>(anomaly score, later phase)"]
        db[("DB<br/>payer context,<br/>evaluations, audit")]
    end

    subgraph optional["Desirable features"]
        direction TB
        lookup["CLABE lookup<br/>Transparency Portal<br/><i>(public query)</i>"]
        banco1["Bank 1 application"]
        banco2["Bank 2 application"]
    end

    client -->|"proposed transfer"| api
    api -->|"load payer context and baseline"| db
    api -->|"evaluate this transfer"| rules
    rules -->|"signals and risk points"| ml
    ml -->|"anomaly score"| api
    api -->|"persist evaluation, signals, decision audit"| db
    api -->|"allow / warn / pause + reason codes"| client

    api -.-> lookup
    banco1 <-.->|"end-to-end flow"| api
    banco2 <-.->|"end-to-end flow"| api

    classDef core fill:#e8f0fe,stroke:#1a73e8,stroke-width:2px
    classDef extra fill:#fff4e5,stroke:#e8912d,stroke-width:1px,stroke-dasharray:4 3
    class ml,db,rules,api core
    class lookup,banco1,banco2 extra
```

## Flow

- A bank application or client proposes a transfer to the API. The API is the
  entry point for every request.
- The API loads the payer's context and behavioral baseline from the database.
- The rule analysis service evaluates **this transfer** against **this payer's**
  baseline and emits explainable signals with risk points.
- The ML component contributes an anomaly score. It is a later phase; the
  rule-based path works without it.
- The API persists the risk evaluation, its signals, and the decision audit,
  then returns `allow`, `warn`, or `pause` with reason codes before the
  customer confirms.
- The two bank applications are optional end-to-end interfaces that show how
  the guard can prevent a fraudulent operation.
- The public CLABE lookup is an optional public product connected to the API.

## Scope constraint

The system scores a **transfer**, not a person. It does not compute
person-level risk, receiver reputation, or "anomalous person" records. See
`docs/ai/knowledge/spei-intent-guard-data-model.md` for the entity model and
`docs/ai/engineers-discussion/HACKMTY-CONTEXT.md` section 6 for why reputation
and complaint signals were deliberately excluded.
