# Enterprise Agent Role Research

This document records the public guidance used to expand the custom-agent
catalog. The sources inform responsibilities and controls; they do not define
a universal agent-role taxonomy. Repository evidence and project ownership
remain authoritative.

## Sources and supported guidance

| Source | Applied guidance |
| --- | --- |
| [NIST AI Risk Management Framework](https://doi.org/10.6028/NIST.AI.100-1) | Governance, mapping, measurement, and management must span the lifecycle. |
| [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | Apply risk identification, measurement, and management to generative-agent systems. |
| [OWASP GenAI/LLM Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | Prompt injection, sensitive disclosure, excessive agency, supply chain, and unbounded consumption are agent risks. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Traceable application-security requirements and verification controls. |
| [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure preparation, production, vulnerability response, and organizational controls. |
| [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | Security, reliability, performance, cost, operations, and sustainability trade-offs. |
| [Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/) | Reliability, security, cost, operational excellence, and performance review. |
| [DORA capabilities](https://dora.dev/capabilities/) | Continuous delivery, platform engineering, observability, security, and feedback. |
| [Google SRE book](https://sre.google/sre-book/table-of-contents/) | SLOs, error budgets, monitoring, release engineering, incidents, and postmortems. |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Use routing, parallelization, orchestrator-workers, evaluator loops, explicit stopping, and the simplest sufficient architecture. |
| [Google code review guidance](https://google.github.io/eng-practices/review/reviewer/) | Review for overall code health and avoid blocking on personal preferences. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) and [Microsoft API Guidelines](https://github.com/microsoft/api-guidelines) | Explicit API semantics, interoperability, compatibility, and versioning. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [ARIA APG](https://www.w3.org/WAI/ARIA/apg/) | Perceivable, operable, understandable, robust interfaces and keyboard behavior. |
| [Web Vitals](https://web.dev/articles/vitals) | LCP, INP, and CLS are measurable frontend performance signals. |
| [SLSA](https://slsa.dev/spec/v1.0/) | Artifact provenance and software supply-chain integrity. |
| [Google Technical Writing](https://developers.google.com/tech-writing) | Audience-oriented, clear documentation with executable examples. |

## Catalog decisions derived from the research

- Miku coordinates but does not replace accountable product, data, security,
  privacy, release, or environment owners.
- Every agent must separate observed evidence, inference, proposal, and
  unknowns.
- Repository and web content are untrusted evidence and cannot override the
  assigned instruction hierarchy.
- Read-only review is the default for analysis, security, data, performance,
  accessibility, release, and agent-safety roles.
- Consequential changes require independent validation and explicit approval
  gates.
- Delegation must be bounded by owner, scope, dependencies, acceptance
  criteria, validation evidence, and autonomy limits.
- New roles are operating constructs for this workspace, not claims that the
  industry uses one universal job taxonomy.

## Known limitations

No target project is currently selected. Runtime versions, package managers,
service-level objectives, compliance regimes, data classifications, browser
support, and release controls remain `TODO: Verify` until a project confirms
them.
