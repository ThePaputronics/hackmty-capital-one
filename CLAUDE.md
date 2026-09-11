# Repository Working Agreement (Claude Code)

This repository's engineering and delivery rules are defined in `AGENTS.md`.
That file is the source of truth — read it first, in full, before making any
change. This file exists only to map the repository's shared Codex resources
onto Claude Code so the same working agreement applies here.

All agent responses, documentation, plans, code comments, commit messages, and
user-facing text must be written in English unless the user explicitly asks
for another language.

## Shared resources (Codex-authored, still apply here)

- `.codex/config.toml` and `.codex/agents/*.toml` — 25 specialist role
  definitions (backend, frontend, security-review, tester, etc.), written for
  the Codex CLI's `/agent` command.
- `.agents/skills/*` — 11 reusable workflow write-ups.
- `docs/ai/knowledge/*` — shared contracts, engineering principles, and
  templates referenced by the roles above.
- `.codex/agent-tests/cases/*` — adversarial evaluation cases for the agents.
- `scripts/validate-ai-config.py` — static validator for the catalog; run it
  after editing any agent or skill file.

## How this maps to Claude Code

Claude Code's built-in `Agent` tool has its own fixed subagent roster
(`general-purpose`, `Explore`, `Plan`, etc.) and does not read
`.codex/*.toml` files directly — there is no automatic `miku` or
`backend-node` subagent here. When a task matches one of the `.codex/agents/`
roles:

- Read the matching `.codex/agents/<role>.toml` for its
  `developer_instructions` and apply that role's scope, constraints, and
  delivery format directly.
- If delegating to a Claude Code subagent, brief it with the relevant role's
  instructions inline (a fresh subagent has no access to `.codex/` context on
  its own).
- Follow the orchestration discipline described in `.codex/agents/miku.toml`
  (scope the task, decompose before delegating, verify returned work against
  the repo, avoid overlapping edits) even when acting as a single Claude Code
  session rather than a multi-agent Codex run.

## Engineering standards (from AGENTS.md)

- Inspect existing documentation and repository instructions before making
  changes.
- Preserve user changes and avoid unrelated edits.
- Prefer small, reversible, well-tested changes.
- Reuse existing patterns, helpers, types, and dependencies.
- Do not invent APIs, technologies, integrations, requirements, or test
  results.
- Mark unverifiable information as `TODO: Verify`.
- Surface errors instead of swallowing them.
- Ask for confirmation before destructive or production-affecting actions.

## Workspace knowledge

- Read project documentation before scanning repositories.
- Read `repos/<repo>.md` before analyzing a repository when it exists.
- Keep repository facts, project decisions, reusable knowledge, and temporary
  information in their designated locations.
- Update documentation when a change makes it inaccurate.

## Delivery standard

Every completed task should state:

- what changed;
- which files or systems were affected;
- what validation was run;
- what remains uncertain or blocked.
