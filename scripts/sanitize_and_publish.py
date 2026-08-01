#!/usr/bin/env python3
"""Sync a golden-dataset/run-result file from the private source repo into this
public repo, sanitizing machine-specific paths and the tester's real contact info.

Usage:
    AGENTTEST_REPO_ROOT=/path/to/private/repo \
    AGENTTEST_HOME_DIR=/Users/you \
    AGENTTEST_REAL_EMAIL=you@example.com \
    AGENTTEST_REAL_PHONE=+1XXXXXXXXXX \
    python3 scripts/sanitize_and_publish.py <source_file> <dest_file>

All four values are real, machine-specific secrets and must never be hardcoded
in this file (it lives in a public repo) — they are read from environment
variables at runtime instead, with no default fallback, so the script fails
loudly rather than silently sanitizing nothing if one is missing.

Replacement rules (order matters — repo-root prefix must be stripped before the
home-dir prefix, otherwise the home-dir rule fires first and leaves a dangling
"Developer/<repo-name>/..." segment):

  1. "<repo_root>/"   -> ""                  (repo-relative paths, no placeholder)
  2. "<home_dir>/"     -> "/Users/<user>/"    (paths outside the repo, e.g. ~/Desktop)
  3. real email        -> "user@example.com"
  4. real phone number  -> "+90XXXXXXXXXX"

Rule 1 previously used a literal "Tests/AgentTestSuite/" replacement instead of "",
which double-prefixed any path already containing that subdirectory as a suffix
(e.g. ".../<repo-name>/Tests/AgentTestSuite/fixtures/..." became
"Tests/AgentTestSuite/Tests/AgentTestSuite/fixtures/..."). That bug is why the
published golden_dataset_86.json and the autorun0707 run's own `dataset_path` field
both show the doubled path — see AgentTestMethodology repo audit, 2026-07-31.

A separate audit the same day found that the real email/phone/repo-root/home-dir
values had previously been hardcoded directly in this file's source, and that
sanitization had never actually been run against 22 already-published files
(METHODOLOGY.md/.TR + 20 result files under results/PheronAgent/), which still
contained the real values in plaintext. Both were fixed in that pass.
"""
import os
import sys

REPO_ROOT = os.environ.get("AGENTTEST_REPO_ROOT")
HOME_DIR = os.environ.get("AGENTTEST_HOME_DIR")
REAL_EMAIL = os.environ.get("AGENTTEST_REAL_EMAIL")
REAL_PHONE = os.environ.get("AGENTTEST_REAL_PHONE")

PLACEHOLDER_EMAIL = "user@example.com"
PLACEHOLDER_PHONE = "+90XXXXXXXXXX"
PLACEHOLDER_HOME = "/Users/<user>"


def sanitize(text: str) -> str:
    # 1. Repo-root-relative paths first (must run before the home-dir rule below).
    text = text.replace(REPO_ROOT + "/", "")
    text = text.replace(REPO_ROOT, ".")
    # 2. Remaining home-dir paths (outside the repo, e.g. ~/Desktop/...).
    text = text.replace(HOME_DIR, PLACEHOLDER_HOME)
    # 3. Contact info.
    text = text.replace(REAL_EMAIL, PLACEHOLDER_EMAIL)
    text = text.replace(REAL_PHONE, PLACEHOLDER_PHONE)
    return text


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    missing = [
        name
        for name, val in (
            ("AGENTTEST_REPO_ROOT", REPO_ROOT),
            ("AGENTTEST_HOME_DIR", HOME_DIR),
            ("AGENTTEST_REAL_EMAIL", REAL_EMAIL),
            ("AGENTTEST_REAL_PHONE", REAL_PHONE),
        )
        if not val
    ]
    if missing:
        print(f"ERROR: missing required env var(s): {', '.join(missing)}", file=sys.stderr)
        print(__doc__)
        return 1
    src, dest = sys.argv[1], sys.argv[2]
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    sanitized = sanitize(content)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(sanitized)
    leaked = []
    for needle in (REPO_ROOT, HOME_DIR, REAL_EMAIL, REAL_PHONE):
        if needle in sanitized:
            leaked.append(needle)
    if leaked:
        print(f"WARNING: possible leak still present in {dest}: {leaked}", file=sys.stderr)
        return 2
    print(f"Sanitized {src} -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
