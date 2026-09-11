# Agent Strategy Review

Status: proposed  
Review date: 2026-09-11  
Scope: repository Codex agents, skills, delegation, validation, permissions,
knowledge synchronization, and shared-server operations.

## Executive assessment

The current operating model has strong safety and handoff foundations. It
already follows the most useful Codex pattern: bounded specialist tasks,
parallel read-heavy work, sequenced writes, parent-owned integration, explicit
validation, and concise evidence returned to the coordinator.

The next improvement should reduce orchestration overhead and make key controls
enforceable. The catalog currently contains 25 custom agents and 144,524 bytes
of agent, skill, instruction, and knowledge text. Most text is loaded
progressively, so total size is not an immediate context failure; however,
role overlap, a large Miku profile, inherited model settings, and prompt-only
remote restrictions create avoidable ambiguity and risk.

## Observed current state

- `.codex/config.toml` registers 25 project agents and permits six concurrent
  subagent threads.
- Codex already provides built-in `worker` and `explorer` agents. The custom
  `implementer` and `repo-analysis` roles overlap those built-ins.
- `backend` overlaps four language-specific backend roles; `frontend` overlaps
  `frontend-react`; `reviewer` overlaps parts of `security-review`,
  `api-contract`, `database`, `accessibility`, and `performance`.
- Miku contains 11,069 characters of instructions and declares itself the only
  orchestration authority, while Codex assigns orchestration and final result
  ownership to the main thread.
- All custom agents inherit the parent model and reasoning effort. No role has
  an explicit workload-appropriate reasoning setting.
- Thirteen analytical profiles use `sandbox_mode = "read-only"`, including
  `tester`. Test, build, browser, and benchmark tools commonly need to create
  caches or artifacts even when they do not edit source.
- The agent evaluation suite contains useful adversarial cases, but the current
  validator checks catalog structure rather than running behavioral evals.
- The `/srv/hackathon` remote boundary is documented in instructions and tests,
  but no command wrapper, hook, or remote account policy enforces it.
- Knowledge synchronization now has one owner, fast-forward-only behavior,
  scoped staging, validation, and no force-push.

## Recommended operating model

### 1. Keep orchestration in the main thread

Treat the active Codex main thread as the final coordinator. Keep Miku as an
optional orchestration profile for complex decomposition or as the shared name
for the repository workflow, but remove language claiming that a spawned Miku
thread is the sole final authority. A spawned subagent must return evidence to
its parent; the parent integrates and delivers the result.

Move stable coordination rules that must always apply into concise sections of
`AGENTS.md` and keep detailed procedures in skills or references. Reduce Miku
to the decisions that differ from Codex defaults.

### 2. Use three delegation levels

| Level | Trigger | Strategy |
| --- | --- | --- |
| Direct | Small, localized, understood task | Main thread performs find-read-edit-verify |
| Specialist | One bounded domain with material expertise | Spawn one agent and verify its handoff |
| Parallel | Two or more independent read-heavy questions | Spawn two or three agents, wait, compare, then integrate |

Use sequential waves for architecture, implementation, testing, and review.
Do not run parallel writes on the same checkout. When independent parallel
writes provide real value, use separate Git worktrees and integrate through the
main thread.

Start with a practical concurrency cap of three active subagents. Raise it only
when measured elapsed-time savings outweigh token use and integration cost.

### 3. Reduce the default role catalog

Prefer a smaller core catalog and load specialized behavior through skills.
A practical core is:

- `requirements-analyst`;
- `architect`;
- `worker` or one project implementer;
- `tester`;
- `reviewer`;
- `security-review`;
- `devops`;
- `documentation`.

Keep technology specialists only after the repository contains that stack and
their instructions add verified project conventions. Prefer either the general
domain role or the technology specialist for one subtask, not both.

Specialized audit roles remain valuable for relevant high-risk changes but do
not need to participate in routine work.

### 4. Match reasoning effort to the work

Avoid pinning a model until team entitlement and cost constraints are known.
Use workload-specific effort or explicit spawn requests:

- low or medium for repository exploration, documentation inventory, and
  narrow mechanical checks;
- medium for ordinary implementation and tests;
- high for architecture, final review, security, concurrency, migrations, and
  incident analysis.

Measure quality and cost before making these defaults permanent. Each subagent
performs its own model and tool work and therefore consumes additional tokens.

### 5. Separate source immutability from filesystem immutability

Keep reviewers and policy analysts in a read-only sandbox. Rework `tester` so
it may create known build, cache, coverage, screenshot, and temporary artifacts
without editing source. A dedicated worktree or bounded writable roots are
safer than broad full access.

Remember that live permission choices on the parent turn propagate to spawned
agents and can override profile defaults. Validate effective permissions during
agent evaluation rather than assuming TOML alone enforces them.

### 6. Turn agent cases into executable evaluations

Add a small evaluation runner that records:

- profile and commit under test;
- test case and expected decision;
- observed response and tool calls;
- changed paths and delegation graph;
- pass, fail, blocked, or not-applicable result;
- prompt-level controls versus runtime-enforced controls.

Run it whenever agents, skills, permissions, MCP, orchestration, or deployment
policy changes. Static TOML and frontmatter validation should remain as the
fast first check, not the final proof.

### 7. Enforce the remote path boundary technically

The `/srv/hackathon` rule is currently prompt-level. Add an enforcement layer
before agents perform deployments. Viable options include:

- a narrowly scoped deployment script that rejects canonical paths outside
  `/srv/hackathon`;
- a restricted SSH command or dedicated deployment account;
- filesystem permissions that prevent the account from writing elsewhere;
- command policy or hooks that reject remote mutation commands without an
  approved wrapper.

The enforcement must account for symlinks, mounts, shell redirection, archive
extraction, temporary files, Docker daemon state, and commands that change host
configuration indirectly. Do not claim the boundary is enforced until an
adversarial test proves the runtime blocks it.

### 8. Measure whether agents help

For complex tasks, record a lightweight delegation summary:

- agents spawned and why;
- elapsed time versus expected serial work;
- correction loops and failed handoffs;
- duplicated exploration or edit conflicts;
- validation defects found by independent review;
- approximate usage impact when available.

Review the data after several real tasks. Remove or merge roles that are rarely
selected, repeatedly misrouted, or do not improve outcomes.

## Prioritized roadmap

### Immediate

1. Correct Miku's authority model so the main thread owns final integration.
2. Lower concurrency from six to three until parallel value is measured.
3. Change tester permissions to permit bounded artifacts without source edits.
4. Add technical enforcement for `/srv/hackathon` before the first deployment.

### Next

5. Consolidate overlapping general and technology roles.
6. Assign reasoning effort by risk and measure usage.
7. Add executable behavioral evaluation and store results by agent version.

### After real project code exists

8. Add verified build, test, deploy, rollback, and ownership commands to the
   relevant agents and skills.
9. Evaluate role selection and handoff quality using real repository tasks.
10. Retire generic instructions that Codex already handles reliably.

## Sources

- OpenAI, [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  main-thread focus, bounded summaries, read-heavy parallelism, write conflict
  risk, token usage, model/effort selection, permission inheritance, built-in
  agents, and custom-agent configuration.
- OpenAI, [Codex best practices](https://learn.chatgpt.com/guides/best-practices):
  concise practical `AGENTS.md`, one coherent outcome per chat, planning for
  complex work, worktrees for parallel live changes, and test/review loops.
- OpenAI, [Build skills](https://learn.chatgpt.com/docs/build-skills): concise,
  discriminating skill descriptions, progressive loading, and repository
  skill discovery from `.agents/skills`.

## Decision status

These recommendations are research findings, not adopted policy. Apply them in
small reviewable changes and run agent evaluation before declaring the new
behavior effective.
