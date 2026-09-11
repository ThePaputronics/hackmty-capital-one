# Agent Routing Matrix

Use the narrowest role supported by repository evidence. A matching name alone
does not justify delegation. Small, localized tasks stay in the main thread;
specialists are useful when domain judgment, independent review, or parallel
read-heavy investigation offsets the handoff cost.

| Agent | Activate when | Do not activate when | Effort |
| --- | --- | --- | --- |
| `miku` | A complex request needs decomposition, sequencing, or a reusable orchestration package | A localized task has one clear implementation loop | high |
| `requirements-analyst` | Intent, scope, acceptance criteria, or business rules are ambiguous | The request and observable behavior are already precise | medium |
| `product-domain` | Product priority or domain meaning needs accountable clarification | The question is purely technical | medium |
| `repo-analysis` | The parent needs an evidence map across unfamiliar repository areas | The owning files and conventions are already known | medium |
| `architect` | Boundaries, migrations, cross-service trade-offs, or an ADR are required | A local change follows an established design | high |
| `api-contract` | API, event, schema, error, versioning, or compatibility behavior changes | Implementation preserves an already verified contract | high |
| `implementer` | A bounded change crosses layers or no narrower stack role fits | A stack specialist owns the same files | medium |
| `backend` | Backend work is stack-neutral or spans runtimes | One verified runtime owns the task | medium |
| `backend-dotnet` | Verified C# or .NET code owns the backend change | The affected backend uses another runtime | medium |
| `backend-go` | Verified Go code owns service, concurrency, or tooling behavior | The affected backend uses another runtime | high |
| `backend-node` | Verified Node.js or TypeScript code owns backend behavior | The affected code is browser React or another runtime | medium |
| `backend-python` | Verified Python code owns APIs, workers, data access, or packaging | The affected backend uses another runtime | medium |
| `frontend` | Client work is non-React or spans frontend frameworks | React and TypeScript exclusively own the surface | medium |
| `frontend-react` | Verified React and TypeScript code owns the user flow | The client uses another framework | medium |
| `database` | Data modeling, query plans, integrity, indexing, or migrations need independent analysis | No persistence behavior changes | high |
| `tester` | Existing checks must be selected, run, diagnosed, and mapped to acceptance criteria | The task only asks to write implementation or new tests | medium |
| `reviewer` | A finished diff needs independent correctness and regression review | Implementation is still changing | high |
| `security-review` | Trust boundaries, authentication, authorization, secrets, or exploitable data flows changed | No credible security-sensitive surface changed | high |
| `agent-security` | Agent prompts, tools, MCP, permissions, untrusted context, or delegation policies changed | The change contains no agent or tool boundary | high |
| `accessibility` | UI semantics, focus, keyboard, contrast, motion, or assistive use changed | No user interface behavior changed | high |
| `performance` | A measured regression or explicit performance target exists | There is no baseline or user-visible performance question | high |
| `privacy-compliance` | Personal or regulated data collection, use, sharing, retention, or deletion changed | No governed data lifecycle changed | high |
| `devops` | CI/CD, containers, infrastructure, deployment, or observability must be implemented | The work is only release assessment or application code | high |
| `release-incident` | Release readiness, rollback, SLOs, incident triage, or postmortem analysis is needed | Infrastructure implementation is the requested work | high |
| `documentation` | Durable facts, setup, operations, decisions, or KB entries changed | Documentation would only repeat an existing source | medium |

## Coordination rules

1. The main thread owns the user request, integration, final validation, and
   delivery. A spawned Miku is advisory within its handoff.
2. Use one implementation owner per file set. Never pair a generalist with its
   specialist on the same paths.
3. Run at most three active subagents. Parallelize independent, primarily
   read-only investigation; sequence design, writes, tests, and final review.
4. Review roles report findings and evidence. They do not repair the source
   they review.
5. The tester may create generated validation artifacts but may not edit source,
   configuration, tests, fixtures, snapshots, migrations, or lockfiles.
6. DevOps and release work on the shared server must resolve every remote
   mutation beneath `/srv/hackathon`; host-level changes remain prohibited.

## Handoff evidence

Every spawned agent returns status, observed evidence, changed paths, commands
and results, assumptions, risks, and the next dependency. The main thread checks
this evidence before using it or unblocking another wave.
