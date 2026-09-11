---
name: github-actions-debugging
description: Provides a repeatable workflow for diagnosing failed GitHub Actions workflows and applying verified fixes.
---

1. Identify the workflow, run, job, commit, and changed paths.
2. Inspect workflow definitions and repository instructions.
3. Read the failing step and surrounding logs before changing files.
4. Classify the failure as code, dependency, configuration, permissions,
   runner, flaky test, or external-service failure.
5. Reproduce locally when practical using the repository's documented commands.
6. Make the smallest fix that addresses the root cause.
7. Re-run the focused validation and inspect the resulting diff.
8. Document required secrets, permissions, environment assumptions, or rollout
   steps without exposing secret values.

Do not rerun workflows indefinitely or weaken a quality/security gate merely to
make a check green.
