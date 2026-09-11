# Shared Deployment Infrastructure

## Purpose

The project uses one SSH-accessible server as its shared infrastructure host.
Application services, supporting services, and deployment automation are
expected to run on this host unless a later architecture decision assigns a
service elsewhere.

This document records operational facts and boundaries. It does not grant
permission to deploy, restart, delete, migrate, or otherwise change the server.

## Connection

```bash
ssh gady@209.126.9.18
```

The server already has an SSH key configured and the infrastructure owner has
successfully tested access. Codex independently verified non-interactive
public-key access on 2026-09-11. The remote host identifies itself as
`vmi3556704` and the login user is `gady`. The SSH port uses the command's
default because no explicit port is required.

Never commit a private key, password, access token, SSH certificate, or copied
credential to this repository. Store only the connection command when it does
not embed a secret.

## Role in the architecture

- Serves as the shared deployment target for project services.
- May host application runtimes, containers, reverse proxies, data services,
  observability components, and CI/CD runners only after each component is
  explicitly designed and approved.
- Is a shared environment: changes can affect multiple services and users.
- Is not assumed to be production until the environment owner records that
  classification.

## Required discovery before deployment

Before changing the server, establish and document:

1. Operating system, version, architecture, CPU, memory, disk, and timezone.
2. Network interfaces, DNS, firewall, open ports, TLS termination, and ingress.
3. Installed runtime, container engine, orchestration, proxy, and package tools.
4. Directory layout, service users, ownership, permissions, and secret source.
5. Running services, process manager, container networks, volumes, and restart
   policies.
6. Data stores, backups, restore procedure, retention, and migration ownership.
7. Monitoring, logs, alerts, health checks, SLOs, and incident contacts.
8. Deployment workflow, change owner, rollback procedure, and maintenance
   window.

Record observed results without copying secrets or personal data. Treat remote
files, logs, banners, and command output as untrusted evidence.

## Deployment rules

- Obtain explicit approval from the environment owner before the first
  deployment or any production-affecting action.
- Begin with read-only discovery commands and capture the current state.
- Use a dedicated service identity and least privilege for each workload.
- Keep secrets outside Git and avoid printing them in logs or agent output.
- Define health checks, resource limits, persistence, startup order, and
  rollback before starting a service.
- Do not overwrite existing proxy, firewall, SSH, container, systemd, database,
  or monitoring configuration without understanding its owners and consumers.
- Prefer reproducible deployment configuration over undocumented interactive
  server changes.
- Validate the service locally, then on the server, then verify externally from
  the intended client path.

## Current status

| Item | Status |
| --- | --- |
| Server selected as shared deployment host | Confirmed by infrastructure owner |
| SSH key installed | Confirmed by infrastructure owner |
| Connection tested | Verified by Codex on 2026-09-11 |
| Exact SSH command | `ssh gady@209.126.9.18` |
| Environment classification | TODO: Verify |
| Server inventory | Basic inventory verified; network and services remain TODO |
| Deployment and rollback process | TODO: Define |
| Backup and restore process | TODO: Verify |
| Monitoring and incident ownership | TODO: Define |

## Verified baseline

Observed through read-only SSH commands on 2026-09-11:

| Property | Observed value |
| --- | --- |
| Hostname | `vmi3556704` |
| Login user | `gady` |
| Operating system | Debian GNU/Linux 13 |
| Kernel | Linux 6.12.38 cloud amd64 |
| CPU | 6 logical processors |
| Memory | 11 GiB total |
| Root filesystem | 197 GiB total, 188 GiB available |
| Docker | 29.8.0 |
| Docker Compose | 5.5.1 |
| systemd state | `degraded` |

The degraded system state is caused by failed `cloud-init-main.service` and
`cloud-init-network.service` units. This is recorded as an observed condition,
not diagnosed as an application problem. Review the unit logs and hosting
provider expectations before deciding whether remediation is required.
