# Design: Agent Strategy v2

The existing catalog remains stable. A central routing matrix provides the
selection contract so profile prompts do not duplicate a large policy block.
Every profile inherits that matrix through the enterprise contract and adds its
own domain procedure.

Reasoning effort follows risk and ambiguity. Architecture, contracts, audits,
operations, performance, concurrency-sensitive Go work, and final review use
`high`; bounded implementation, requirements, discovery, documentation, and
ordinary validation use `medium`. Models remain unpinned so the workspace can
use the parent session's available model.

The tester uses `workspace-write` because compilers and test runners commonly
create caches and reports. Its prompt limits writes to generated validation
artifacts, requires a final working-tree inspection, and prohibits edits to
source and project inputs. Runtime permissions are broader than this semantic
boundary, so adversarial evaluation must still inspect actual tool calls and
changed paths before claiming behavioral enforcement.

Static evaluation checks configuration invariants quickly. Markdown adversarial
cases remain the source for future runtime response evaluations; the static
runner deliberately does not claim to execute a model.
