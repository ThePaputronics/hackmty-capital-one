# Proposal: Agent Strategy v2

## Problem

The catalog has capable specialists but allows six concurrent threads, leaves
reasoning effort implicit, prevents the tester from producing normal build
artifacts, and lacks an enforceable routing distinction for overlapping roles.
Miku also claims final authority even when Codex invokes it as a child agent.

## Outcome

Keep all 25 roles for compatibility while giving each an explicit activation,
exclusion, and reasoning level. Limit concurrency to three, keep final authority
in the main thread, permit only generated validation artifacts for the tester,
and add executable policy checks for these guarantees.

## Scope

- `.codex/config.toml` and all registered agent profiles;
- the shared operating and delegation contracts;
- routing and adversarial evaluation documentation;
- local validation scripts.

Remote infrastructure and application services are outside this change.

## Success criteria

- all 25 profiles have a valid `model_reasoning_effort`;
- routing covers every registered role exactly once;
- the maximum configured concurrency is three;
- the parent owns final integration;
- tester validation can write artifacts but never source;
- static strategy evaluation and existing configuration validation pass.
