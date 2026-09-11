---
name: mcp-governance
description: Reviews and governs MCP servers, external tools, permissions, authentication, sandboxing, consent, and rollback before integration.
---

Use this skill before adding, enabling, updating, or troubleshooting an MCP
server or external tool collection.

## Default posture

No MCP server is trusted by default. Do not add a server, endpoint, credential,
filesystem path, or network permission merely because a tool would be useful.
Prefer a narrowly scoped, read-only integration and use existing local tools
when they satisfy the task.

## Required review

1. State the business purpose and exact capabilities required.
2. Identify owner, maintainer, source repository, version or commit, license,
   data classification, and dependency chain.
3. List every tool, command, URL, filesystem path, network destination,
   credential, and side effect.
4. Confirm authentication, token handling, consent, session binding, OAuth
   redirect validation, SSRF controls, and logging behavior.
5. Define allowlist and denylist rules; deny rules take precedence.
6. Require sandboxing and least privilege for local processes and files.
7. Define tool-call audit, incident response, disable switch, rollback, and
   removal procedure.
8. Test malicious tool output, prompt injection, malformed arguments, access
   denial, timeout, retry, and partial failure.
9. Obtain the named workspace, security, data, and environment approvals.

## Prohibited shortcuts

- Do not pass through user tokens to an MCP server without an explicit
  security-approved design.
- Do not trust a server because it is popular, remote, local, or listed in
  documentation.
- Do not use broad filesystem or network access when an exact allowlist works.
- Do not enable production mutation tools for development convenience.
- Do not use `--yolo`, `--allow-all`, or equivalent as a permanent policy.
- Do not report an MCP server as safe without inspecting its tools and testing
  its failure behavior.

Return a governance review using the enterprise contract handoff format.
