# TestSpec for Agent Workflows

## What TestSpec is

TestSpec is a specification-driven workflow for AI-assisted software changes.
The relevant implementation reviewed here is
`Pluto-AI-Workbench/TestSpec`. It is not a Copilot agent or a replacement for
custom agents. It supplies a structured change workspace and commands that
agents can use to keep intent, behavior, design, tasks, implementation, and
verification aligned.

The core model separates:

- `TestSpec/specs/`: the current behavior contract and source of truth;
- `TestSpec/changes/<change-name>/`: a proposed change and its artifacts;
- `TestSpec/changes/archive/`: completed changes and their audit trail.

## Recommended workflow

For a clear small or medium change:

```text
/testspec:propose <change>
  -> /testspec:apply
  -> /testspec:archive
```

For complex or uncertain work:

```text
/testspec:explore
  -> /testspec:new
  -> /testspec:continue
  -> /testspec:apply
  -> /testspec:verify
  -> /testspec:archive
```

The expanded workflow also supports `/testspec:ff`, `/testspec:sync`, and
`/testspec:bulk-archive`.

## Artifact responsibilities

- `proposal.md`: why the change exists, scope, goals, and non-goals.
- `specs/`: behavior requirements and concrete Given/When/Then scenarios.
- `design.md`: technical approach, boundaries, contracts, and trade-offs.
- `tasks.md`: ordered implementation checklist with clear ownership and
  validation.

A behavior spec should describe observable behavior, inputs, outputs, errors,
constraints, and scenarios. It should not prescribe internal classes,
functions, libraries, or implementation steps. Those belong in `design.md` and
`tasks.md`.

## How to apply it to the agent team

Miku remains the orchestrator:

1. Determine whether the request is small enough for direct execution.
2. Use TestSpec when the change has meaningful ambiguity, risk, multiple
   subtasks, cross-repository impact, API or schema contracts, or expensive
   rework potential.
3. Create or refine the TestSpec artifacts before implementation.
4. Convert `tasks.md` into bounded subtasks with one owner each.
5. Delegate only independent tasks that have clear acceptance criteria.
6. Keep dependent tasks sequenced and prevent overlapping edits.
7. Use `/testspec:verify` plus targeted project validation before archiving.
8. Archive only after the parent agent confirms implementation and specs are
   coherent.

TestSpec does not require every trivial change to have a full specification.
Use a lightweight proposal and a few scenarios for low-risk work, and use the
full artifact set for high-risk or cross-cutting changes.

## Installation

The reviewed TestSpec project requires Node.js 20.19.0 or newer. This machine
has Node.js 24.18.0 and npm 11.16.0. Installation has not been performed
because no target repository has been selected and TestSpec may create project
files when initialized.

When a project is ready, review the package and install intentionally:

```bash
npm install -g @Pluto-AI-Workbench/TestSpec@latest
cd <project>
TestSpec init
TestSpec update
```

Verify the generated files before committing them. Review telemetry and opt-out
requirements before enabling it in a sensitive environment.

## Sources

- [TestSpec README](https://github.com/Pluto-AI-Workbench/TestSpec)
- [TestSpec concepts](https://github.com/Pluto-AI-Workbench/TestSpec/blob/main/docs/concepts.md)
- [TestSpec commands](https://github.com/Pluto-AI-Workbench/TestSpec/blob/main/docs/commands.md)
- [TestSpec workflows](https://github.com/Pluto-AI-Workbench/TestSpec/blob/main/docs/workflows.md)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
