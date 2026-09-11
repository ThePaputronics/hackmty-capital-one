# Subagent Delegation Strategy

## What a subagent is

A subagent is a temporary agent process spawned by the main Copilot CLI agent
to perform a focused part of a larger task. It has an isolated context window,
its own prompt and tool restrictions, and returns results to the parent session.
The parent remains responsible for scope, integration, final edits, validation,
and delivery.

Custom agents are profiles. A custom agent becomes a subagent when the runtime
delegates work to it.

The parent agent should be the orchestrator: it decomposes the initial request
into executable subtasks, assigns each subtask one owner, orders dependencies,
and integrates the results. A subagent is an executor for an assigned subtask,
not a replacement orchestrator.

## When delegation creates value

Delegate when at least one of these conditions is true:

- the task needs broad or unfamiliar repository exploration;
- the work has an independent context that would clutter the parent session;
- a long-running command can execute while other independent work continues;
- a specialist review is needed, such as security or code review;
- multiple repositories or disjoint areas can be analyzed independently;
- the work is naturally parallel and results can be merged without conflicting
  edits.

Keep work in the main agent when:

- the task is a narrow find-read-edit-verify sequence;
- the parent already has the required context;
- the subagent would repeat searches already completed;
- the task requires frequent interactive decisions;
- delegation would create overlapping edits or additional coordination.

Delegation introduces overhead: another handoff, context setup, tool calls,
result integration, and possible path or workspace mismatches.

## Handoff contract

Every delegated task should include:

1. **Objective**: the exact question or outcome.
2. **Known context**: relevant paths, findings, constraints, and user intent.
3. **Ownership**: the files, subsystem, or analysis surface owned by the
   subagent.
4. **Boundaries**: read-only or editable scope, excluded paths, and prohibited
   actions.
5. **Deliverable**: the exact result format expected by the parent.
6. **Validation**: commands or evidence the subagent must run or report.

Avoid sending a vague instruction such as "investigate everything". A narrow
handoff reduces repeated searching and makes the result easier to integrate.

## Initial task decomposition

Before dispatching any subagent, the parent creates a task map:

| Field | Requirement |
| --- | --- |
| Objective | Parent request and definition of done |
| Subtask | One concrete outcome |
| Owner | Exactly one parent or specialist agent |
| Scope | Files, repository, subsystem, or analysis surface |
| Dependencies | Results required before starting |
| Acceptance criteria | Observable completion conditions |
| Deliverable | Report, patch, test result, or decision |
| Wave | Parallel or sequential execution group |

The parent keeps a subtask local when it is small, obvious, interactive, or
already supported by gathered context. Delegation requires expected leverage;
the presence of a matching specialist is not enough.

## Parallel delegation

Parallelize only independent work:

- repository analysis and documentation inventory;
- frontend and backend analysis when their contracts are already known;
- implementation and read-only security review on disjoint scopes;
- test execution while documentation is being updated.

Do not parallelize tasks that:

- edit the same files;
- depend on an unresolved design decision;
- require one result to define the next task;
- can cause competing migrations, generated files, or lockfile changes.

Use waves for dependent work: discovery first, design second, implementation
third, validation and review last.

## Integration protocol

Miku must:

- compare subagent results against repository evidence;
- resolve contradictions before editing;
- avoid applying overlapping patches blindly;
- run validation after integrating changes;
- preserve useful findings even when the proposed implementation is rejected;
- report partial, failed, or stale subagent results explicitly.

Subagents must not claim a repository state they did not inspect. They must
return paths, commands, evidence, assumptions, and unresolved questions.

By default, subagents execute only their assigned subtask. They do not
recursively delegate, expand scope, or re-plan the complete parent request
without explicit authorization.

## Permissions and safety

Tool permissions are scoped per agent profile. Read-only agents should receive
only read and search tools. Editing agents should receive the smallest tool set
needed for their responsibility. Shell and external-service access should not
be pre-approved casually because it can enable arbitrary commands or expose
secrets.

Destructive operations, production changes, credential handling, and broad
dependency installation require explicit user confirmation.

## Practical workflow

```text
Miku: establish scope and read existing documentation
  -> repo-analysis: gather missing evidence
  -> requirements-analyst: define acceptance criteria (if unclear)
  -> architect: define design and contracts (if cross-cutting)
  -> frontend/backend/devops/implementer: edit disjoint owned surfaces
  -> tester: run focused validation
  -> security-review/reviewer: inspect the resulting diff
  -> documentation: update authoritative workspace knowledge
  -> Miku: integrate, validate, and deliver
```

## Sources

- GitHub Docs: [About custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents)
- GitHub Docs: [Invoking custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents)
- GitHub Docs: [Custom agents and sub-agent orchestration](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents)
- GitHub Blog: [How we made GitHub Copilot CLI more selective about delegation](https://github.blog/ai-and-ml/how-we-made-github-copilot-cli-more-selective-about-delegation/)
