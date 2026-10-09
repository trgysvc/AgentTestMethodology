#!/usr/bin/env python3
"""Check a run-result JSON against the reporting rules of METHODOLOGY Section 14.

    python3 scripts/validate_run_report.py <run.json> [<run2.json> ...]

Exit code 0: no problem found.  1: a file could not be read.  2: at least one problem or warning.

Problems (a number built on this file could mislead):
  * model_id missing/"unknown"; git_commit not a 40-character hex hash;
  * run_type does not match k (k < 5 must be "exploratory");
  * trials that ended by a limit or by the environment (not scoreable, Section 14.3).
Warnings: results-1.0 files (no telemetry), no dataset hash, passes carrying quality flags.
Also prints pass@1 and the *clean pass@1* of Section 14.2 for results-1.1 files.
"""
import json
import re
import sys

NOT_SCOREABLE = {"request_budget_cut", "infra_error"}
LIMIT_ENDED = {"turn_limit_loop", "critic_escalation", "empty_response_fallback"}
UNCLEAN_FLAGS = {"answer_is_question", "guard_assisted", "loop_signals", "mock_output_in_response"}


def is_clean(trial: dict) -> bool:
    flags = set(trial.get("quality_flags") or [])
    if flags & UNCLEAN_FLAGS or any(f.startswith("ended_by_") for f in flags):
        return False
    return trial.get("termination_reason", "completed") == "completed"


def check(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    problems, warnings = [], []
    model = d.get("model_id")
    if not model or model == "unknown":
        problems.append(f"model_id is {model!r}")
    commit = d.get("git_commit", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit or ""):
        problems.append(f"git_commit is not a 40-character hash: {str(commit)[:40]!r}")
    k, run_type = d.get("k", 1), d.get("run_type")
    if k < 5 and run_type == "published":
        problems.append(f"run_type 'published' with k={k} (Section 2.6 requires k >= 5)")
    schema = d.get("report_schema_version", "results-1.0")
    meta = d.get("run_meta") or {}
    if schema == "results-1.0":
        warnings.append("results-1.0 file: no per-trial telemetry, termination_reason or quality_flags")
    elif not meta.get("dataset_sha256"):
        warnings.append("results-1.1 file without run_meta.dataset_sha256")

    trials = [(b["test_id"], t) for b in d.get("blocks", []) for t in b.get("trials", [])]
    cut = [(i, t.get("termination_reason")) for i, t in trials if t.get("termination_reason") in NOT_SCOREABLE]
    if cut:
        problems.append("not scoreable (re-run before counting): " + ", ".join(f"{i}[{r}]" for i, r in cut))
    limited = [(i, t.get("termination_reason")) for i, t in trials if t.get("termination_reason") in LIMIT_ENDED]
    if limited:
        warnings.append("ended by a limit: " + ", ".join(f"{i}[{r}]" for i, r in limited))

    passes = [(i, t) for i, t in trials if t.get("status") == "pass"]
    flagged = [i for i, t in passes if not is_clean(t)]
    if schema != "results-1.0" and flagged:
        warnings.append(f"{len(flagged)} pass(es) carry quality flags: {', '.join(flagged)}")

    n = len(trials)
    print(f"== {path}")
    print(f"   schema {schema} | model {model} | commit {commit[:12]} | k={k} | {n} trials")
    if n and schema != "results-1.0":
        clean = sum(1 for _, t in passes if is_clean(t))
        print(f"   pass@1 (grader): {len(passes)}/{n} = {len(passes) / n:.1%}   clean pass@1: {clean}/{n} = {clean / n:.1%}")
    for p in problems:
        print(f"   PROBLEM: {p}")
    for w in warnings:
        print(f"   warning: {w}")
    return 2 if problems or warnings else 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    code = 0
    for path in sys.argv[1:]:
        try:
            code = max(code, check(path))
        except (OSError, ValueError, KeyError) as e:
            print(f"== {path}\n   cannot read: {e}", file=sys.stderr)
            code = max(code, 1)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
