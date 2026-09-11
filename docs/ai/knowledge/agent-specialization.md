# Agent Specialization and Value Model

## Purpose

The agent team is organized around explicit engineering responsibilities. Each
agent should create value through a narrow capability, not by repeating the
parent agent's planning or by expanding its scope.

The detailed mandatory lifecycle for every agent is defined in
`enterprise-agent-contract.md`. This document explains role specialization and
handoff semantics; it does not replace the enterprise contract.

## Shared agent contract

Every specialist agent receives:

- one bounded subtask;
- relevant paths and known evidence;
- explicit dependencies;
- acceptance criteria;
- a required deliverable;
- read-only or editable boundaries.

Every specialist agent must:

1. Read applicable instructions and existing documentation.
2. Confirm the assigned scope before acting.
3. Reuse repository patterns and avoid speculative changes.
4. Surface blockers, uncertainty, and failed commands.
5. Return evidence, affected paths, validation, and remaining risks.

Every specialist agent must not:

- re-plan the complete parent request;
- scan unrelated repositories;
- silently broaden its ownership;
- delegate recursively by default;
- overwrite another agent's work;
- invent missing requirements or successful validation.

## Value model

An agent is useful when its specialist perspective reduces risk, context
switching, or execution time. The parent should not delegate work when the
handoff and integration cost exceeds that benefit.

| Role | Creates value by | Not responsible for |
| --- | --- | --- |
| `requirements-analyst` | Making behavior and acceptance criteria testable | Choosing implementation details |
| `repo-analysis` | Producing evidence about unfamiliar code | Editing or redesigning code |
| `architect` | Making boundaries and trade-offs explicit | Implementing the feature |
| `frontend` | Delivering usable, accessible browser behavior | Inventing API contracts |
| `backend` | Delivering reliable services and data behavior | Designing unrelated UI |
| `implementer` | Coordinating focused cross-cutting code edits | Owning product decisions |
| `tester` | Proving behavior and diagnosing failures | Fixing source code |
| `security-review` | Finding exploitable vulnerabilities | General style review |
| `reviewer` | Finding high-confidence defects and drift | Applying fixes |
| `devops` | Making delivery reproducible and operable | Changing production without approval |
| `documentation` | Keeping knowledge authoritative and current | Inventing facts |

## Handoff quality

The parent should prefer handoffs that answer:

- What exact outcome is needed?
- What is already known?
- Which files, repository, or subsystem does the agent own?
- Which files and actions are explicitly out of scope?
- What evidence must be returned?
- What makes the subtask complete?

## Completion states

Agents should report one of these states:

- **complete**: acceptance criteria met and validation reported;
- **partial**: useful progress made but criteria remain;
- **blocked**: cannot proceed without a decision, dependency, or access;
- **not applicable**: assigned scope does not exist or is not affected;
- **failed**: execution attempted and failed with evidence.

## Coordination rule

Miku owns decomposition, sequencing, integration, conflict resolution, and
final delivery. Specialists own execution within their subtask. This division
keeps the system productive without making every agent a second orchestrator.
