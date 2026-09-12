# hackmty-capital-one

This repository includes a shared Codex engineering environment. Anyone who
clones it with Codex can use the same project instructions, specialist agents,
skills, engineering strategies, and agent evaluation cases.

## Codex resources

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-wide engineering and delivery rules |
| `.codex/config.toml` | Registers the custom subagent roles |
| `.codex/agents/` | 25 specialist agents, coordinated by Miku |
| `.agents/skills/` | 11 reusable workflows discovered by Codex |
| `docs/ai/knowledge/` | Shared contracts, strategies, and templates |
| `docs/ai/knowledge/infrastructure.md` | Shared deployment host knowledge and safety boundaries |
| `docs/ai/knowledge/knowledge-sync.md` | Rules for verified, conflict-safe KB synchronization |
| `docs/ai/knowledge/agent-strategy-review.md` | Evidence-based review and roadmap for agent usage |
| `docs/ai/knowledge/agent-routing.md` | Activation, exclusion, effort, and coordination rules for all agents |
| `.codex/agent-tests/cases/` | Adversarial cases for agent evaluation |
| `scripts/validate-ai-config.py` | Static validation for the shared setup |
| `scripts/evaluate-agent-strategy.py` | Executable checks for routing, authority, concurrency, and tester boundaries |
| `INSTALL-CODEX-GLOBAL.md` | Agent-readable global installation procedure |

## Use

1. Clone the repository and open it as a trusted Codex project.
2. Start a new Codex session from the repository root so `AGENTS.md`, project
   configuration, agents, and skills are discovered.
3. Ask Codex to use a role when useful, for example:

   ```text
   Use the miku agent to coordinate this implementation.
   ```

4. In Codex CLI, use `/agent` to inspect or switch to an active subagent
   thread.
5. Validate the catalog after changing an agent or skill:

   ```bash
   python3 scripts/validate-ai-config.py
   python3 scripts/evaluate-agent-strategy.py
   ```

Miku is a technical orchestration role. This shared version intentionally has
no fictional-character or anime personality instructions.

To install the same resources globally for another Codex user, ask Codex to
review [`INSTALL-CODEX-GLOBAL.md`](INSTALL-CODEX-GLOBAL.md) and follow its
conflict-safe installation procedure.

## Portability

All internal references are repository-relative. Personal credentials,
authentication state, conversation history, logs, caches, and machine-specific
Codex settings are intentionally excluded.

## Hello-world demo

The repository includes a minimal static demo served by an unprivileged Nginx
container. Local development binds the service to `127.0.0.1:18080` by default:

```bash
docker compose up --build
curl --fail http://127.0.0.1:18080/healthz
```

`.github/workflows/deploy-demo.yml` targets the verified self-hosted runner
labels `self-hosted`, `linux`, `x64`, and `hackathon`. The workflow deploys only
under `/srv/hackathon/apps/hello-world`, verifies health, and rolls back to the
previous image tag when a deployment fails. The endpoint remains loopback-only
until an ingress design is separately approved. The infrastructure owner
approved only the Compose project `hackathon-hello-world`; the workflow does
not manage unrelated Docker resources.

## Signatures

- Claude Code (Claude Sonnet 5) — closed issue #1
