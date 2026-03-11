#!/usr/bin/env python3
"""Validate that the curated skill repo stays internally consistent."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


README_COUNT_PATTERNS = {
    "badge": r"Skills-(\d+)-brightgreen\.svg",
    "intro": r"focused set of \*\*(\d+) skills\*\*",
    "available_skills": r"This curated fork currently ships \*\*(\d+) skills\*\*",
}


def sorted_skill_dirs(skills_root: Path) -> list[str]:
    return sorted(
        entry.name
        for entry in skills_root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def manifest_skills(manifest_path: Path) -> list[str]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    skills = data["plugins"][0]["skills"]
    return [Path(skill).name for skill in skills]


def readme_counts(readme_path: Path) -> dict[str, int]:
    content = readme_path.read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    for name, pattern in README_COUNT_PATTERNS.items():
        match = re.search(pattern, content)
        if not match:
            raise ValueError(f"README pattern not found for {name!r}: {pattern}")
        counts[name] = int(match.group(1))
    return counts


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skills_root = repo_root / "scientific-skills"
    manifest_path = repo_root / ".claude-plugin" / "marketplace.json"
    readme_path = repo_root / "README.md"

    dirs = sorted_skill_dirs(skills_root)
    manifest = manifest_skills(manifest_path)
    manifest_sorted = sorted(manifest)

    missing_from_manifest = sorted(set(dirs) - set(manifest))
    missing_from_dirs = sorted(set(manifest) - set(dirs))
    duplicate_manifest = sorted(
        skill for skill in set(manifest) if manifest.count(skill) > 1
    )

    errors: list[str] = []
    if missing_from_manifest:
        errors.append(
            "Skills present on disk but missing from marketplace.json: "
            + ", ".join(missing_from_manifest)
        )
    if missing_from_dirs:
        errors.append(
            "Skills present in marketplace.json but missing on disk: "
            + ", ".join(missing_from_dirs)
        )
    if duplicate_manifest:
        errors.append(
            "Duplicate skills listed in marketplace.json: "
            + ", ".join(duplicate_manifest)
        )

    try:
        counts = readme_counts(readme_path)
    except ValueError as exc:
        errors.append(str(exc))
        counts = {}

    expected_count = len(dirs)
    for label, value in counts.items():
        if value != expected_count:
            errors.append(
                f"README {label} count is {value}, expected {expected_count}"
            )

    if errors:
        print("Curated skill sync validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {expected_count} curated skills.")
    print("Skill directories and marketplace.json are in sync.")
    print("README counts are in sync.")
    if manifest != manifest_sorted:
        print(
            "Note: marketplace.json skill order is not alphabetical. "
            "This is allowed."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
