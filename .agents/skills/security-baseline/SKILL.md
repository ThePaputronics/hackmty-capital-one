---
name: security-baseline
description: Applies a focused security baseline to application code, dependencies, CI, infrastructure, and documentation.
---

Use this skill for security-sensitive changes or before release.

Check:

- authentication and authorization boundaries;
- input validation and injection resistance;
- secrets, tokens, personal data, logs, and error disclosure;
- dependency manifests and lockfiles;
- file, process, network, and command execution boundaries;
- webhooks, uploads, redirects, SSRF, and deserialization;
- CI permissions, artifact handling, and untrusted input;
- containers, infrastructure, and public exposure.

Report only evidence-backed, actionable findings. Never copy secret values into
reports. Distinguish vulnerabilities from general hardening suggestions.
