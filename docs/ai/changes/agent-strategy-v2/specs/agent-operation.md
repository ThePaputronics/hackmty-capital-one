# Agent Operation Scenarios

## Direct work

Given one localized and understood task, when the main thread selects an
execution strategy, then it performs the find-read-edit-verify loop itself.

## Specialist routing

Given a task with verified stack or domain evidence, when delegation adds
material value, then the main thread selects the narrowest matching specialist
and does not assign a generalist to the same paths.

## Parallel investigation

Given two or more independent read-heavy questions, when parallel execution
saves time, then no more than three active subagents receive non-overlapping
handoffs and the main thread integrates their evidence.

## Parent authority

Given Miku is spawned as a child agent, when it completes its handoff, then it
returns evidence or an orchestration package and does not claim final delivery.

## Tester artifacts

Given an existing build or test writes generated output, when the tester runs
it, then generated artifacts are allowed, source inputs remain unchanged, and
any remaining artifacts are reported.

## Shared server boundary

Given deployment work targets the shared server, when an agent plans a remote
mutation, then the resolved destination must remain beneath `/srv/hackathon`.
