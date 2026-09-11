"""Evaluate agent-routing and permission invariants without invoking a model."""

from pathlib import Path
import re
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".codex" / "config.toml"
AGENT_DIR = ROOT / ".codex" / "agents"
ROUTING = ROOT / "docs" / "ai" / "knowledge" / "agent-routing.md"
CONTRACT = ROOT / "docs" / "ai" / "knowledge" / "enterprise-agent-contract.md"


def main() -> int:
    errors: list[str] = []
    config = tomllib.loads(CONFIG.read_text())
    declarations = {
        name: value
        for name, value in config["agents"].items()
        if isinstance(value, dict)
    }
    routing = ROUTING.read_text()
    contract = CONTRACT.read_text()

    if config["agents"].get("max_concurrent_threads_per_session") != 3:
        errors.append("concurrency cap must be three")

    valid_efforts = {"medium", "high"}
    for name in sorted(declarations):
        profile = tomllib.loads((AGENT_DIR / f"{name}.toml").read_text())
        effort = profile.get("model_reasoning_effort")
        if effort not in valid_efforts:
            errors.append(f"{name}: expected medium or high reasoning effort")
        matches = re.findall(rf"^\| `{re.escape(name)}` \|", routing, re.MULTILINE)
        if len(matches) != 1:
            errors.append(f"{name}: expected exactly one routing row")

    tester = tomllib.loads((AGENT_DIR / "tester.toml").read_text())
    tester_rules = tester["developer_instructions"]
    if tester.get("sandbox_mode") != "workspace-write":
        errors.append("tester: sandbox must permit generated artifacts")
    for phrase in ("must not modify", "git status", "remaining path"):
        if phrase not in tester_rules:
            errors.append(f"tester: missing artifact boundary phrase {phrase!r}")

    miku = tomllib.loads((AGENT_DIR / "miku.toml").read_text())
    for phrase in ("main thread", "parent retains final integration"):
        if phrase not in miku["developer_instructions"]:
            errors.append(f"miku: missing parent-authority phrase {phrase!r}")

    if "active main thread owns orchestration and final" not in contract:
        errors.append("contract: final authority is not assigned to main thread")
    if "`/srv/hackathon`" not in routing:
        errors.append("routing: shared-server mutation boundary is missing")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Agent strategy is valid: {len(declarations)} routed profiles, "
          "concurrency 3, parent authority, and tester artifact boundaries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
