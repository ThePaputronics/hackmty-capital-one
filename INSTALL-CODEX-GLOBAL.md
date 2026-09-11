# Install This Repository's Codex Environment Globally

This repository is both a project workspace and a portable Codex knowledge
base. A developer can ask Codex to inspect this file and install the shared
agents, skills, strategies, and tests into their personal Codex environment.

## Prompt for Codex

From the repository root, start a new Codex session and send:

```text
Review AGENTS.md and INSTALL-CODEX-GLOBAL.md in this repository. Install the
shared Codex agents, skills, knowledge, and agent evaluation cases into my
personal Codex environment. Preserve my existing configuration, show me any
conflicts, do not copy credentials or machine-specific state, validate the
result, and tell me whether I need to restart Codex.
```

Codex should treat that prompt as authorization to prepare and perform the
local installation. Normal filesystem permission controls still apply.

## Required installation behavior

Codex must:

1. Read `AGENTS.md`, this file, `.codex/config.toml`, and the resource map in
   `README.md`.
2. Inspect the target user's existing `~/.codex/config.toml`,
   `~/.codex/AGENTS.md`, `~/.codex/agents/`, `~/.agents/skills/`, and relevant
   knowledge directories before writing.
3. Create a timestamped backup of every existing file that will be changed.
4. Copy the 25 files from `.codex/agents/` to `~/.codex/agents/`.
5. Register the agent declarations from `.codex/config.toml` in the user's
   `~/.codex/config.toml` without replacing unrelated model, MCP, plugin,
   permissions, project, telemetry, or UI settings.
6. Copy the 11 skill directories from `.agents/skills/` to
   `~/.agents/skills/` while preserving unrelated personal skills.
7. Copy `docs/ai/knowledge/` to a stable personal location and rewrite copied
   agent and skill references to that location when necessary.
8. Copy `.codex/agent-tests/` to a stable personal location used by the
   `agent-evaluation` skill.
9. Merge the reusable working agreements from `AGENTS.md` into
   `~/.codex/AGENTS.md`. Preserve stricter existing instructions and report
   conflicts instead of silently choosing one.
10. Never copy `.git`, credentials, SSH keys, environment files, logs, session
    databases, caches, or machine-specific authentication state.
11. Run `python3 scripts/validate-ai-config.py` and
    `python3 scripts/evaluate-agent-strategy.py` in the repository and validate
    every installed skill with Codex's available skill validator.
12. Report installed paths, backups, conflicts, validation results, and restart
    requirements.

## Use without global installation

Global installation is optional. When the repository is trusted and Codex is
started from its root:

- `AGENTS.md` supplies project instructions;
- `.codex/config.toml` registers project agents;
- `.agents/skills/` exposes repository skills;
- agent and skill instructions route Codex to `docs/ai/knowledge/`.

Start a new Codex session after cloning or after changing configuration. Ask
Codex to use Miku when a task benefits from coordinated specialist work:

```text
Use the miku agent to coordinate this task. Read the repository knowledge base
and load only the specialists and skills relevant to the work.
```

## Verification

Run:

```bash
python3 scripts/validate-ai-config.py
python3 scripts/evaluate-agent-strategy.py
```

Expected result:

```text
Codex configuration is valid: 25 agents, 11 skills, and 3 evaluation suites.
Agent strategy is valid: 25 routed profiles, concurrency 3, parent authority, and tester artifact boundaries.
```
