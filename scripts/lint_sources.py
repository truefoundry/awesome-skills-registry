#!/usr/bin/env python3
"""Validate sources.yaml for duplicate / conflicting GitHub sources.

A "source" is a GitHub repo listed under `sources:` in sources.yaml. Each repo
should appear at most once — use `skills_paths` (plural) inside a single entry
when a repo exposes skills under multiple roots, rather than repeating the repo.

Checks (each is a hard failure unless noted):
  - malformed-url      : url is missing or not a parseable github.com/owner/repo
  - duplicate-source   : the same owner/repo is listed in more than one entry
  - duplicate-exact    : two entries are byte-for-byte identical scans
                         (same repo + same skills paths + same skill filename)

Usage:
    uv run python scripts/lint_sources.py              # validate sources.yaml (exit 1 on issues)
    uv run python scripts/lint_sources.py path/to.yaml # validate a specific file
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print(
        "Error: PyYAML is required. Run via `uv run python scripts/lint_sources.py`.",
        file=sys.stderr,
    )
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_PATH = REPO_ROOT / "sources.yaml"


class _LineLoader(yaml.SafeLoader):
    """SafeLoader that records the 1-based line each mapping starts on."""


def _construct_mapping(loader: _LineLoader, node: yaml.MappingNode):
    mapping = yaml.SafeLoader.construct_mapping(loader, node, deep=True)
    mapping["__line__"] = node.start_mark.line + 1
    return mapping


_LineLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


@dataclass
class SourceLint:
    rule: str
    message: str


@dataclass
class ParsedSource:
    line: int
    url: str
    owner: str = ""
    repo: str = ""
    skills_paths: tuple[str, ...] = field(default_factory=tuple)
    skill_filename: str = "SKILL.md"


def _normalize_paths(entry: dict) -> tuple[str, ...]:
    """Mirror load_sources(): collapse skills_path / skills_paths to a canonical tuple."""
    skills_paths_raw = entry.get("skills_paths") or []
    if not skills_paths_raw:
        skills_paths_raw = [entry.get("skills_path", "/")]

    normalized: list[str] = []
    for p in skills_paths_raw:
        p = str(p)
        if p != "/" and not p.endswith("/"):
            p += "/"
        normalized.append(p)
    return tuple(sorted(normalized))


def parse_sources(path: Path) -> tuple[list[ParsedSource], list[SourceLint]]:
    """Parse sources.yaml into ParsedSource records, collecting structural issues."""
    issues: list[SourceLint] = []
    raw = path.read_text(encoding="utf-8")

    try:
        data = yaml.load(raw, Loader=_LineLoader)
    except yaml.YAMLError as exc:
        return [], [SourceLint("yaml-parse-error", f"Invalid YAML: {exc}")]

    if not isinstance(data, dict) or "sources" not in data:
        return [], [SourceLint("missing-sources", "Top-level 'sources' key is missing")]

    parsed: list[ParsedSource] = []
    for entry in data.get("sources") or []:
        if not isinstance(entry, dict):
            issues.append(SourceLint("entry-not-mapping", f"Source entry is not a mapping: {entry!r}"))
            continue

        line = entry.get("__line__", 0)
        url = entry.get("url")
        if not url or not isinstance(url, str):
            issues.append(SourceLint("malformed-url", f"line {line}: entry is missing a 'url'"))
            continue

        parts = urlparse(url).path.strip("/").split("/")
        if len(parts) < 2 or not parts[0] or not parts[1]:
            issues.append(SourceLint("malformed-url", f"line {line}: not a github.com/owner/repo URL: {url}"))
            continue

        parsed.append(ParsedSource(
            line=line,
            url=url,
            owner=parts[0],
            repo=parts[1],
            skills_paths=_normalize_paths(entry),
            skill_filename=str(entry.get("skill_filename", "SKILL.md")),
        ))

    return parsed, issues


def find_duplicates(sources: list[ParsedSource]) -> list[SourceLint]:
    """Flag repos listed more than once (duplicate sources)."""
    issues: list[SourceLint] = []

    by_repo: dict[str, list[ParsedSource]] = defaultdict(list)
    for src in sources:
        by_repo[f"{src.owner}/{src.repo}"].append(src)

    for repo, group in sorted(by_repo.items()):
        if len(group) < 2:
            continue

        lines = ", ".join(str(s.line) for s in sorted(group, key=lambda s: s.line))
        configs = {(s.skills_paths, s.skill_filename) for s in group}

        if len(configs) == 1:
            issues.append(SourceLint(
                "duplicate-exact",
                f"'{repo}' is listed {len(group)} times with identical config (lines {lines}). "
                f"Remove the redundant entr{'y' if len(group) == 2 else 'ies'}.",
            ))
        else:
            issues.append(SourceLint(
                "duplicate-source",
                f"'{repo}' is listed {len(group)} times (lines {lines}). "
                f"A repo should appear once — use 'skills_paths' in a single entry for multiple roots.",
            ))

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate sources.yaml for duplicate GitHub sources")
    parser.add_argument(
        "file",
        nargs="?",
        default=str(SOURCES_PATH),
        help="Path to the sources file (default: sources.yaml)",
    )
    args = parser.parse_args()

    path = Path(args.file).resolve()
    if not path.exists():
        print(f"Error: {path} does not exist", file=sys.stderr)
        sys.exit(2)

    sources, issues = parse_sources(path)
    issues.extend(find_duplicates(sources))

    try:
        rel = path.relative_to(REPO_ROOT)
    except ValueError:
        rel = path

    if issues:
        for issue in issues:
            print(f"{rel}: {issue.rule}: {issue.message}")
        print()
        print(f"Checked {len(sources)} source(s) — found {len(issues)} issue(s).")
        sys.exit(1)

    print(f"Checked {len(sources)} source(s) — no duplicate sources found.")


if __name__ == "__main__":
    main()
