#!/usr/bin/env python3
"""Block x run stability matrix (METHODOLOGY Section 14.8).

    python3 scripts/stability_matrix.py <run1.json> <run2.json> ... > matrix.md

One column per run (in the order given), one row per block, a letter per cell
(P pass, F fail, R needs_review, E infra_error, - block absent from that run) and the number of
*flips* (changes of verdict between consecutive runs where the block was present). Blocks with
flips are listed first. Run-to-run variance during a fix cycle is information, not noise to hide.
"""
import json
import sys

LETTER = {"pass": "P", "fail": "F", "needs_review": "R", "infra_error": "E"}


def verdict(block: dict) -> str:
    trials = block.get("trials") or []
    if not trials:
        return "-"
    statuses = [t.get("status") for t in trials]
    if all(s == "pass" for s in statuses):
        return "P"
    if any(s == "infra_error" for s in statuses):
        return "E"
    if any(s == "needs_review" for s in statuses):
        return "R"
    return "F"


def main() -> int:
    paths = sys.argv[1:]
    if len(paths) < 2:
        print(__doc__)
        return 1
    runs = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            runs.append({b["test_id"]: verdict(b) for b in json.load(f).get("blocks", [])})
    ids = sorted({i for r in runs for i in r})
    rows = []
    for i in ids:
        cells = [r.get(i, "-") for r in runs]
        seen = [c for c in cells if c != "-"]
        flips = sum(1 for a, b in zip(seen, seen[1:]) if a != b)
        rows.append((flips, i, cells))
    rows.sort(key=lambda x: (-x[0], x[1]))
    names = [p.rsplit("/", 1)[-1].replace(".json", "")[-18:] for p in paths]
    print("| Block | " + " | ".join(names) + " | flips |")
    print("|---|" + "---|" * len(paths) + "---|")
    for flips, i, cells in rows:
        print(f"| {i} | " + " | ".join(cells) + f" | {flips} |")
    unstable = sum(1 for r in rows if r[0] > 0)
    print(f"\n{unstable} of {len(rows)} blocks changed verdict between consecutive runs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
