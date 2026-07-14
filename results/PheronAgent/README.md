# PheronAgent Results

This folder holds actual test-run artifacts from PheronAgent, the reference case study for the methodology in `METHODOLOGY_TR.md`. It exists to show what a real, non-hypothetical application of the methodology looks like — not as part of the universal methodology itself.

## Contents

- **32 result files** (`run_<model>_<YYYYMMDD>_k<n>[_<tag>].md` / `.jsonl`), following the naming and content conventions defined in Part II, Section 2.7 of the methodology document. Model attribution (`qwen3.5-9b`) and `k` values were verified from each file's own content, not assumed — see `CHANGELOG.md` (Version 7) for how.
- `datasets/` — `golden_dataset_seed.json` and `golden_dataset_smoke.json`: real, filled-in examples of the golden-dataset schema (Section 2.1), as opposed to the blank `templates/golden_dataset.template.json` at the repository root.

## Reading these files

- Files with `run_type` (inside the file content) marked `exploratory` — mostly the early `k1`/`k3` runs from 2026-06-29 through 2026-07-03 — are bug-hunting logs, not certified results. See Section 2.6 of the methodology (Minimum-k Rule) for why.
- `run_qwen3.5-9b_20260713_k5_scoringfinal.md` is the closest thing to a certified snapshot: the final, k=5, 86-test scored run referenced throughout the methodology document.
- These are PheronAgent-specific (test IDs, tool names, UBID numbers). If you're adapting the methodology to your own agent, don't copy these files — copy the *format* they follow, using the blank templates at the repository root instead.
