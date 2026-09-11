# Original Environment Setup Snapshot

This file records the source machine at migration time. It is not a portable
requirement. Verify every tool, version, account, service, and command in the
current environment before relying on it.

## Current environment

Detected tools:

- `copilot`: available at `/usr/local/bin/copilot`
- `git`: available at `/usr/bin/git`
- `python3`: available at `/usr/bin/python3`
- `node`: v24.18.0
- `npm`: v11.16.0
- `docker`: v29.7.2
- `docker compose`: v5.5.0
- `gh`: not installed
- `pnpm`, `yarn`: not installed
- `kubectl`, `terraform`: not installed

Docker is enabled and running as a system service. The user `gady` belongs to
the `docker` group. A new login session may be required before Docker works
without `sg docker` or `sudo`.

## Recommended installation policy

Install additional tools only after a target repository establishes that they
are needed:

1. Read the repository manifest and setup documentation.
2. Prefer the repository's declared runtime and package manager.
3. Prefer a version manager or project-local environment.
4. Install the smallest missing tool required for the current validation.
5. Record the decision in the project or repository documentation.

Likely tools, depending on the project:

- JavaScript/TypeScript: Node.js and the repository-selected package manager.
- Python: Python, a virtual environment, and the repository-selected manager.
- Containers: Docker or the project's compatible container runtime.
- Kubernetes: `kubectl` plus the configured cluster or package tool.
- Infrastructure: the repository-selected Terraform, OpenTofu, or cloud CLI.
- GitHub automation: GitHub CLI (`gh`) only when repository or workflow
  operations require it.

Do not install or configure production credentials from an agent task.

## Copilot commands

After adding or changing skills, reload them in the CLI:

```text
/skills reload
/skills list
/skills info <skill-name>
```

After adding or changing user custom agents, restart the CLI if they are not
visible in `/agent`.
