---
name: documentation-maintenance
description: Maintains and safely synchronizes accurate, non-duplicated workspace knowledge after repository, project, architecture, operational, agent, or policy changes.
---

1. Identify the source change and the documentation it makes stale.
2. Prefer updating an existing authoritative document over creating a duplicate.
3. Keep repository facts in `repos/<repo>.md`.
4. Keep cross-repository relationships in `projects/<project>/repos.md`.
5. Keep reusable guidance in `knowledge/`.
6. Keep decisions in ADR files.
7. Put uncertain or temporary information in `inbox/`.
8. Use relative links and mark missing evidence as `TODO: Verify`.
9. Report files created, moved, updated, and intentionally unchanged.

When work creates durable, verified knowledge, read
`docs/ai/knowledge/knowledge-sync.md`. Miku or an explicitly assigned
documentation agent may commit and normally push changes limited to the defined
KB surfaces after checking upstream state, validation, staged paths, and
secrets. Use only fast-forward-safe integration and never force-push. Stop on
divergence, conflicts, failed validation, missing authorization, or unrelated
staged changes.

Do not delete useful information during reorganization.
