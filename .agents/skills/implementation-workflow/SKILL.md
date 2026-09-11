---
name: implementation-workflow
description: Provides a disciplined workflow for implementing scoped software changes with evidence, focused diffs, and targeted validation.
---

1. Convert the request into acceptance criteria and explicit non-goals.
2. Read local instructions and inspect existing patterns.
3. Search for related implementations, helpers, types, and tests.
4. Identify the smallest complete change and its affected files.
5. Consider compatibility, error paths, security, performance, and rollback.
6. Implement in coherent edits without unrelated cleanup.
7. Update directly affected documentation.
8. Run the smallest existing validation that covers the change.
9. Review the diff for accidental changes and missing edge cases.
10. Report actual results and unresolved risks.

Do not add dependencies, abstractions, or tools unless repository evidence
shows they are needed.
