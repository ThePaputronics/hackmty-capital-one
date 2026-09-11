---
name: workspace-context
description: Establishes the correct workspace, project, repository, and documentation scope before analysis or implementation.
---

Use this skill at the beginning of substantial work.

1. Identify the current workspace and active repository.
2. Look for global and repository instructions.
3. Identify the active project under `projects/`.
4. Read the project's `README.md`, `repos.md`, `architecture.md`, and relevant
   decisions before scanning source repositories.
5. Read `repos/<repo>.md` before analyzing a repository when it exists.
6. Determine which repositories are actually involved from `repos.md`.
7. Inspect current changes and preserve unrelated user work.
8. State the scope and excluded repositories before proceeding.

Never scan every repository by default. Use `TODO: Verify` for missing context.
