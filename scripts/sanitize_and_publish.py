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
    # JSON allows "/" to be encoded as the escape sequence "\/" (Swift's JSONEncoder does this
    # for string content, e.g. a model's raw response text quoting a file path) — a plain
    # replace() on the un-escaped path silently misses every occurrence inside such a string,
    # leaking the real username throughout the file with zero warning (the leak-check below
    # only re-checks the same un-escaped needles, so it passed clean while 40+ escaped
    # occurrences remained). Confirmed live 2026-08-09 on the k=5 autorun1710 report. Fix: build
    # the escaped variant of each path needle and replace both forms, in both directions —
    # escaped-form replacement must run BEFORE the plain-form replacement, otherwise the plain
    # pass would already have consumed the unescaped path segments a naive single-pass escaped
    # replace still depends on.
    repo_root_escaped = REPO_ROOT.replace("/", "\\/")
    home_dir_escaped = HOME_DIR.replace("/", "\\/")
    placeholder_home_escaped = PLACEHOLDER_HOME.replace("/", "\\/")

    # 1. Repo-root-relative paths first (must run before the home-dir rule below) — escaped
    #    form before plain form.
    text = text.replace(repo_root_escaped + "\\/", "")
    text = text.replace(repo_root_escaped, ".")
    text = text.replace(REPO_ROOT + "/", "")
    text = text.replace(REPO_ROOT, ".")
    # 2. Remaining home-dir paths (outside the repo, e.g. ~/Desktop/...) — escaped form first.
    text = text.replace(home_dir_escaped, placeholder_home_escaped)
    text = text.replace(HOME_DIR, PLACEHOLDER_HOME)
    # 3. Bare username, with no path prefix at all — an agent's raw response text can state it
    #    directly as prose (e.g. "Kullanıcı adı: <username>"), not just embed it inside a path.
    #    Confirmed live 2026-08-09: this exact sentence leaked past rules 1+2 in the k5 autorun
    #    1710 report (a GÜV-03 /etc/passwd trial's response text). Must run AFTER the path rules
    #    above, since those already consumed every path-prefixed occurrence — running this first
    #    would leave "/Users/<user>" instead of the intended "/Users/<user>" placeholder untouched
    #    by rule 2 wherever a path-prefixed occurrence was replaced first.
    username = HOME_DIR.rstrip("/").rsplit("/", 1)[-1]
    text = text.replace(username, "<user>")
    # 4. Contact info (no "/" in either, no escaped-form variant needed).
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
    # Also check the bare username (HOME_DIR's last path component) on its own — this is what
    # actually leaked on 2026-08-09 (via JSON's "\/"-escaped path separator, a form the full-path
    # needles below don't match). Checking the username alone catches that case and any other
    # future escaping/encoding variant we haven't anticipated, at the cost of being stricter than
    # strictly necessary — a false positive here just means a manual look, not a silent leak.
    username = HOME_DIR.rstrip("/").rsplit("/", 1)[-1]
    leaked = []
    for needle in (REPO_ROOT, HOME_DIR, REAL_EMAIL, REAL_PHONE, username):
        if needle in sanitized:
            leaked.append(needle)
    if leaked:
        print(f"WARNING: possible leak still present in {dest}: {leaked}", file=sys.stderr)
        return 2
    print(f"Sanitized {src} -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
