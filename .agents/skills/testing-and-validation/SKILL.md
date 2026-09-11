---
name: testing-and-validation
description: Selects and diagnoses existing tests, linters, type-checks, builds, and smoke checks for a software change.
---

1. Read the repository manifest and CI configuration.
2. Identify the package manager and documented commands.
3. Prefer focused validation for changed packages or files.
4. Run related checks together when they use the same runner.
5. Escalate to broader validation only when focused checks are insufficient.
6. Capture the first meaningful failure and enough context to diagnose it.
7. Separate code failures, test failures, dependency failures, and environment
   failures.
8. Never report a command as passing unless it exited successfully.

Do not install a new test framework or alter test configuration as a shortcut.
Ask before broad dependency installation.
