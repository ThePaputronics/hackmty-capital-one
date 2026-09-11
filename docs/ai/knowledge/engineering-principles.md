# Engineering Principles for Specialized Agents

These principles are defaults, not substitutes for repository conventions,
framework documentation, or explicit project requirements. Agents must verify
the actual stack before applying technology-specific advice.

## Universal principles

- Prefer clear, boring, maintainable code over clever abstractions.
- Keep responsibilities cohesive and dependencies directed inward where
  practical.
- Make invalid states difficult to represent and validate external input at
  system boundaries.
- Make errors explicit, contextual, observable, and actionable.
- Preserve compatibility unless a breaking change is intentional, documented,
  and migrated.
- Keep side effects at boundaries and make retries safe through idempotency.
- Treat security, accessibility, performance, and operability as behavior.
- Test observable behavior and failure paths, not implementation trivia.
- Make small reversible changes and remove dead code only when in scope.
- Prefer existing project patterns over introducing new libraries or layers.

## Design heuristics

- Start with the simplest architecture that satisfies current requirements.
- Use interfaces at ownership boundaries, not everywhere by default.
- Separate domain rules from transport, persistence, and framework code.
- Prefer composition over inheritance when it reduces coupling.
- Make time, randomness, network, filesystem, and database dependencies
  injectable or controllable in tests.
- Use structured logs and stable error codes at service boundaries.
- Document decisions when they affect multiple teams, repositories, or future
  migrations.

## Quality gates

Every implementation should consider:

1. behavior and acceptance criteria;
2. type and input validation;
3. authorization and data exposure;
4. error, timeout, retry, and cancellation behavior;
5. test coverage for normal and negative paths;
6. performance and resource use;
7. observability and rollback;
8. documentation and compatibility.

## Technology routing

Technology-specific agents are adapters, not replacements for the domain
agents. Miku should route to one technology specialist only after identifying
the repository's language and framework from manifests, configuration, and
source. If evidence is incomplete, use the domain agent or `repo-analysis`
first and mark uncertainty as `TODO: Verify`.

## Sources

- [Effective Go](https://go.dev/doc/effective_go)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [Node.js Learn](https://nodejs.org/en/learn)
- [ASP.NET Core best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices)
- [React documentation](https://react.dev/learn)
