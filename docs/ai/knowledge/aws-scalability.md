# AWS-Ready Scalability

## Purpose

Scalability on AWS is a top evaluation priority for this hackathon. Every
service, API, data store, and infrastructure decision must be designed so it
can be replicated onto AWS managed services without a redesign, even though
the current authorized deployment target is the shared VPS described in
`docs/ai/knowledge/infrastructure.md`. This document does not authorize
provisioning AWS resources or changing the deployment target; it defines the
design properties every specialist must apply from the start so a later lift
to AWS is a configuration change, not a rewrite.

## Principles

- **Stateless services.** No service may keep session, cache, or job state
  only in local process memory or on local disk if that state must survive a
  restart or a second replica. Put that state in a shared store (for example a
  Redis-compatible cache or the primary database) so it maps directly to
  ElastiCache without an application rewrite.
- **Externalized configuration.** Read hosts, ports, credentials, and feature
  flags from environment variables or a config layer, never hardcode them.
  This is what allows a direct move to AWS Systems Manager Parameter Store or
  Secrets Manager.
- **Horizontal over vertical scaling.** Design every service to scale by
  running more replicas behind a load balancer, not by depending on one
  instance's local state or an in-memory singleton that other replicas cannot
  see. This maps directly to an ALB/NLB with ECS, Fargate, or EKS target
  groups.
- **Containers as the deployment unit.** Package services as Docker images,
  matching the container tooling already used in this repository's
  infrastructure. A container image is the direct on-ramp to ECR plus
  ECS/Fargate/EKS with no rebuild required.
- **Portable persistence.** Use mainstream, standard SQL/engine features
  instead of exotic vendor-specific extensions when a mainstream engine
  achieves the same result, so schemas and migrations can move to RDS/Aurora
  (or a DynamoDB-style access pattern for key-value/document needs) with
  minimal change. Do not choose a database feature for convenience if a
  portable equivalent meets the same requirement.
- **Abstracted object storage.** Route file/blob writes through a storage
  interface with a local-disk adapter, rather than embedding local filesystem
  paths in business logic, so the adapter can be swapped for S3 without
  touching callers.
- **Queue-based async work.** Put background and async work behind a queue or
  worker abstraction rather than in-request background threads or host-only
  cron jobs, so it maps to SQS/SNS/EventBridge and can run correctly with
  multiple replicas.
- **Health checks and graceful shutdown.** Expose a health/readiness endpoint
  and handle termination signals for a graceful drain. This is required by
  ECS/ALB health checks and by Kubernetes-style orchestration.
- **Observability via stdout/stderr.** Write structured logs to stdout/stderr
  as the source of truth, not only to local log files, so they map directly to
  the CloudWatch Logs / Fargate log driver.
- **Infrastructure as versioned config.** Describe infrastructure (container
  definitions, environment variables, networking assumptions) in versioned
  files (Dockerfiles, compose files, IaC) instead of undocumented manual server
  steps, so it can be translated into Terraform/CDK/CloudFormation later.

## What this does not require right now

- It does not require deploying to AWS during the hackathon. The authorized
  deployment target remains the VPS in `docs/ai/knowledge/infrastructure.md`
  until an explicit new infrastructure decision changes that.
- It does not require adding AWS SDKs or provisioning cloud resources
  prematurely — only that the current design does not block a later
  lift-and-shift.
- It does not justify unnecessary distributed complexity (premature
  microservices, speculative queues, speculative multi-region design). Apply
  the simplest architecture that satisfies current requirements, per
  `docs/ai/knowledge/engineering-principles.md`, while still keeping the
  properties above.

## Design checklist

When designing or reviewing a service, endpoint, or infrastructure change,
verify:

1. Can this run as two or more replicas at the same time without shared local
   state breaking correctness?
2. Is all configuration external (environment variables), with no
   host-specific hardcoded paths outside `/srv/hackathon` per
   `docs/ai/knowledge/infrastructure.md`?
3. Is persistent state only in the database/cache/object-store layer, never
   only on local disk or only in in-process memory?
4. Does the service expose a health check and shut down gracefully on a
   termination signal?
5. Are logs written to stdout/stderr in a structured, parseable format?
6. If asynchronous work exists, is it behind a queue/worker boundary rather
   than an unpersisted in-request background task?

## Recording trade-offs

When a decision trades AWS-readiness against hackathon velocity, the
`architect` agent should record it as an ADR noting the trade-off and what
would need to change to move that piece to AWS later. Do not block hackathon
delivery on premature cloud provisioning — record the gap instead.

## Sources

- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [The Twelve-Factor App](https://12factor.net/)
