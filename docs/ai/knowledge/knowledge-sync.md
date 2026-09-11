# Shared Knowledge Synchronization

## Objective

Keep every developer and agent aligned through the repository's versioned
knowledge base. Knowledge synchronization is part of delivery when work
produces durable, verified information.

## Knowledge surfaces

The synchronized knowledge base consists of:

- `AGENTS.md` and `README.md`;
- `INSTALL-CODEX-GLOBAL.md`;
- `docs/ai/knowledge/`;
- `.codex/agents/`, `.codex/config.toml`, and `.codex/agent-tests/`;
- `.agents/skills/`;
- validation utilities that directly maintain these resources.

Application code, secrets, logs, caches, generated runtime data, and temporary
notes are not knowledge-base content.

## When to synchronize

Evaluate the KB at the end of a task and synchronize when the task establishes
or changes durable information, including:

- architecture, infrastructure, service ownership, or deployment boundaries;
- verified setup, build, test, release, recovery, or operational procedures;
- API, schema, security, privacy, accessibility, or compatibility decisions;
- agent roles, skills, delegation rules, validation cases, or tool policy;
- an incident lesson or repeated failure whose resolution changes future work.

Also check the KB before a deployment or release and after an approved durable
decision. Do not create a commit merely because time passed or wording can be
polished. Temporary observations, hypotheses, task status, and unverified facts
must remain out of the authoritative KB or be marked `TODO: Verify`.

## Ownership

Every specialist must include `Knowledge candidates` in its handoff when it
discovers information worth preserving. Read-only specialists do not edit or
push the KB.

The active main thread owns the synchronization decision and integration. It
may update the KB directly or assign one bounded, non-overlapping task to
`documentation`. Only the main thread or its assigned documentation agent may
create and push a KB sync commit. Other agents return evidence and proposed
destinations.

## Authorized Git workflow

The repository owner authorizes non-force KB synchronization pushes to the
configured `origin` branch when the change satisfies this policy. This standing
authorization applies only to the knowledge surfaces listed above.

Before pushing:

1. Confirm the repository, branch, remote, and working-tree state.
2. Fetch and integrate upstream only with a fast-forward-safe workflow. Use
   `git pull --ff-only` when the local branch is behind and clean enough to do
   so safely.
3. Stop on divergence, conflicts, detached HEAD, missing upstream, failed
   authentication, or unrelated staged changes.
4. Update the existing authoritative document instead of creating a duplicate.
5. Cite observed repository paths, commands, or owner decisions for material
   facts. Redact sensitive values.
6. Run `python3 scripts/validate-ai-config.py`,
   `python3 scripts/evaluate-agent-strategy.py`, `git diff --check`, and a secret
   pattern scan appropriate to the changed files.
7. Review the exact staged paths and ensure they are limited to KB surfaces.
8. Commit with a focused message such as `docs(kb): record deployment boundary`.
9. Push normally to the configured upstream. Never force-push, rewrite history,
   bypass branch protection, or silently switch branches.
10. Report the commit, pushed branch, validation, and any remaining uncertainty.

If upstream policy requires a pull request, push a dedicated branch and report
the branch for review instead of attempting to bypass the policy.

## Stop conditions

Do not commit or push when evidence is incomplete, a secret may be present,
unrelated work would be included, validation fails, the remote has diverged, or
the change requires an owner decision. Preserve the local evidence and return a
clear blocker.
