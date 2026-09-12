# Repository Codex Working Agreement

The shared agent catalog is registered in `.codex/config.toml`. Reusable skills
live in `.agents/skills`, and supporting engineering guidance lives in
`docs/ai/knowledge`. Load only the role, skill, and references relevant to the
current task.

Before planning deployment or remote-server work, read
`docs/ai/knowledge/infrastructure.md`. Treat the server as shared infrastructure
and require verified connection details, ownership, rollback, and approval
before changing remote state.

Before planning product scope, features, or architecture, read
`docs/ai/knowledge/challenge-brief.md`. It records the sponsor's challenge
tracks, the track this repository targets, and the owner-stated scale and
stack constraints. Do not change the targeted track on your own initiative;
raise a blocker instead.

AWS scalability is a top evaluation priority for this hackathon. Before
proposing or implementing any service, API, data store, or infrastructure
design, read `docs/ai/knowledge/aws-scalability.md` and apply its
cloud-readiness checklist so the architecture can be replicated onto AWS
without a redesign, even while the project runs on the shared VPS described in
`docs/ai/knowledge/infrastructure.md`.

At the end of work that creates durable knowledge, read and follow
`docs/ai/knowledge/knowledge-sync.md`. Every specialist reports knowledge
candidates; Miku or an explicitly assigned documentation agent verifies,
integrates, validates, commits, and normally pushes KB-only changes. Never
force-push or include unrelated files.

The only authorized remote filesystem scope is `/srv/hackathon`. Never create,
edit, move, delete, link, mount, or change permissions or ownership outside
that directory. Resolve target paths before every remote mutation and stop if
the resolved path is not `/srv/hackathon` or one of its descendants. System
packages, systemd units, global container-daemon state, firewall rules, SSH
configuration, global reverse-proxy configuration, and other host-level state
are outside the authorized scope.

The infrastructure owner approved one narrow Docker exception on 2026-09-11:
the hello-world demo may create and replace resources owned by the Compose
project `hackathon-hello-world`. Its bind-mounted files and deployment state
must remain below `/srv/hackathon/apps/hello-world`, and its published port must
bind only to `127.0.0.1:18080`. This exception does not authorize Docker daemon
configuration, unrelated images, containers, networks, volumes, privileged
containers, host networking, public ingress, or host-level changes.

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
