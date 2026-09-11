"""Validate the repository's shared Codex agents, skills, and references."""

from pathlib import Path
import re
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / ".codex" / "agents"
SKILLS = ROOT / ".agents" / "skills"
CONFIG = ROOT / ".codex" / "config.toml"
CONTRACT = ROOT / "docs" / "ai" / "knowledge" / "enterprise-agent-contract.md"
CASES = ROOT / ".codex" / "agent-tests" / "cases"


def yaml_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    return text[4:end]


def main() -> int:
    errors: list[str] = []

    try:
        config = tomllib.loads(CONFIG.read_text())
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"{CONFIG}: {exc}")
        config = {}

    registered = {
        name: value
        for name, value in config.get("agents", {}).items()
        if isinstance(value, dict)
    }

    agent_files = sorted(AGENTS.glob("*.toml"))
    for path in agent_files:
        try:
            profile = tomllib.loads(path.read_text())
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        for key in ("name", "description", "developer_instructions"):
            if not profile.get(key):
                errors.append(f"{path}: missing {key}")
        if path.stem not in registered:
            errors.append(f"{path}: agent is not registered in config.toml")
        if "docs/ai/knowledge/enterprise-agent-contract.md" not in profile.get(
            "developer_instructions", ""
        ):
            errors.append(f"{path}: missing shared contract reference")

    for name, declaration in registered.items():
        expected = f"./agents/{name}.toml"
        if declaration.get("config_file") != expected:
            errors.append(f"agent {name}: config_file must be {expected}")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    for path in skill_files:
        try:
            header = yaml_frontmatter(path.read_text())
        except (OSError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        if not re.search(r"^name: [a-z0-9]+(?:-[a-z0-9]+)*$", header, re.MULTILINE):
            errors.append(f"{path}: invalid skill name")
        if not re.search(r"^description: .+$", header, re.MULTILINE):
            errors.append(f"{path}: missing description")

    if not CONTRACT.is_file():
        errors.append(f"{CONTRACT}: missing")
    if len(list(CASES.glob("*.md"))) != 3:
        errors.append(f"{CASES}: expected three evaluation case files")
    if len(agent_files) != 25:
        errors.append(f"expected 25 agents, found {len(agent_files)}")
    if len(skill_files) != 11:
        errors.append(f"expected 11 skills, found {len(skill_files)}")

    if errors:
        print("\n".join(errors))
        return 1

    print(
        f"Codex configuration is valid: {len(agent_files)} agents, "
        f"{len(skill_files)} skills, and 3 evaluation suites."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
