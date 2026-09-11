# Custom Agent Design Tips

This guidance summarizes patterns found in official GitHub documentation,
GitHub's public analysis of more than 2,500 `agents.md` files, the
`github/awesome-copilot` collection, and Microsoft guidance on orchestrator and
subagent architectures.

## Practices that consistently help

### 1. Define a specific job

Avoid catch-all profiles such as "general coding helper." State the role,
expertise, trigger conditions, owned surfaces, and output. A narrower role
improves routing and reduces unrelated edits.

### 2. Put executable commands and project knowledge near the top

When the target repository exists, add verified commands early in the relevant
agent profile:

- build;
- focused tests;
- lint and formatting;
- type-check;
- local development;
- safe diagnostic or dry-run commands.

Do not invent commands. Use `TODO: Verify` until a repository confirms them.

### 3. Use concrete examples

One verified example of a good API response, test, component, error report, or
documentation section is more useful than broad prose. Examples must come from
the project or be clearly labeled as illustrative.

### 4. Define three levels of boundaries

For each agent, document:

- **Always do**: required behavior and validation;
- **Ask first**: risky decisions, migrations, dependencies, production changes;
- **Never do**: secrets, unrelated paths, destructive commands, or ownership
  outside the handoff.

### 5. Scope tools to the role

Read-only analysis, testing, security review, and code review should not have
edit access. Editing agents should receive only the tools they need. External
services, shell commands, and production operations require careful approval.

### 6. Require structured outputs

Structured reports make handoffs composable. Require paths, evidence,
commands, results, severity or status, assumptions, blockers, and next action.
Avoid outputs that only say "looks good" or "implemented."

### 7. Treat the repository as the source of truth

Agent profiles can describe stable workflow rules, but stack versions,
commands, architecture, and file paths belong to repository or project
documentation. Update those facts as the project evolves.

### 8. Start small and iterate

Create a focused agent, observe failures, and refine its boundaries and output.
Do not add every possible role or install third-party plugins before the target
project demonstrates a need.

## Orchestrator design

An orchestrator should own the user conversation, initial decomposition,
subtask routing, dependency ordering, integration, and final validation.
Subagents should own bounded execution. This is useful when work naturally
breaks into domains, but it is a poor fit for simple sequential tasks,
time-sensitive tasks with expensive retries, or workflows requiring a highly
consistent fixed process.

Prefer:

```text
intake -> task map -> independent discovery
       -> design/requirements
       -> bounded implementation
       -> validation and review
       -> integration and delivery
```

Do not create a fan-out tree merely because multiple agents are available.

## Useful specialist roles

The current team covers the core software lifecycle. Add narrower agents only
when the project shows repeated need, for example:

- accessibility reviewer;
- performance analyst;
- API contract reviewer;
- database migration reviewer;
- release documentation;
- incident response;
- dependency or supply-chain reviewer.

Each additional role should have a distinct owner, output, and restriction.

## Plugin and community guidance

`github/awesome-copilot` provides agents, skills, hooks, workflows, and plugins,
but its contents are community contributed. Inspect source, permissions,
scripts, network access, telemetry, and maintenance status before installing
anything. Prefer copying a small reviewed pattern into the local workspace
when a full plugin would add unnecessary capabilities.

## Sources

- [GitHub: How to write a great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [GitHub: Custom agents in Copilot CLI](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/)
- [GitHub: Awesome Copilot](https://github.com/github/awesome-copilot)
- [GitHub Docs: Custom agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Microsoft Learn: Orchestrator and subagent patterns](https://learn.microsoft.com/en-us/agents/architecture/multi-agent-orchestrator-sub-agent)
