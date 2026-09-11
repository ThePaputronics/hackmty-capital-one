---
name: testspec-workflow
description: Applies TestSpec-style specification-driven development to ambiguous, risky, cross-cutting, or multi-subtask software changes without adding ceremony to trivial work.
---

Use this skill when a change needs a behavior contract before implementation.

## Decide whether TestSpec is warranted

Use it for:

- ambiguous requirements or expensive rework;
- cross-cutting or cross-repository changes;
- API, schema, migration, security, privacy, or compatibility changes;
- work requiring several coordinated subtasks;
- behavior that needs explicit edge-case scenarios.

Do not require it for a trivial, localized, already-understood change where a
focused implementation and existing tests are sufficient.

## Artifacts

Keep the following concerns separate:

- `proposal.md`: intent, scope, goals, and non-goals;
- `specs/`: observable behavior and scenarios;
- `design.md`: technical approach and trade-offs;
- `tasks.md`: bounded implementation tasks and validation;
- `archive/`: completed change history.

Requirements should use clear normative language such as MUST, SHALL, SHOULD,
or MAY. Scenarios should cover the happy path, invalid input, errors, empty
states, authorization, and important boundary conditions where relevant.

Do not put class names, framework choices, or step-by-step implementation in a
behavior spec. Put those details in design and tasks.

## Agent coordination

The parent orchestrator creates or approves the artifacts, then converts
`tasks.md` into subtasks. Each subtask has one owner, a bounded scope,
dependencies, acceptance criteria, and a deliverable. Delegate only subtasks
with clear independent leverage. Never assign overlapping edits.

Subagents execute the task they receive. They must not expand scope, re-plan
the complete change, or recursively delegate by default.

## Completion

Before archive:

1. Confirm all intended tasks are complete.
2. Run `/testspec:verify` when available.
3. Run the project's focused tests, lint, type-check, or build.
4. Resolve spec/design/implementation drift.
5. Sync specs if required and archive only with the parent's confirmation.
