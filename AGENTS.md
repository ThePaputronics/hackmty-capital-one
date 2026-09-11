# Repository Codex Working Agreement

The shared agent catalog is registered in `.codex/config.toml`. Reusable skills
live in `.agents/skills`, and supporting engineering guidance lives in
`docs/ai/knowledge`. Load only the role, skill, and references relevant to the
current task.

Before planning deployment or remote-server work, read
`docs/ai/knowledge/infrastructure.md`. Treat the server as shared infrastructure
and require verified connection details, ownership, rollback, and approval
before changing remote state.

The only authorized remote filesystem scope is `/srv/hackathon`. Never create,
edit, move, delete, link, mount, or change permissions or ownership outside
that directory. Resolve target paths before every remote mutation and stop if
the resolved path is not `/srv/hackathon` or one of its descendants. System
packages, systemd units, global container-daemon state, firewall rules, SSH
configuration, global reverse-proxy configuration, and other host-level state
are outside the authorized scope.

All agent responses, documentation, plans, code comments, commit messages, and
user-facing text must be written in English unless the user explicitly asks
for another language.

## Engineering standards

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
