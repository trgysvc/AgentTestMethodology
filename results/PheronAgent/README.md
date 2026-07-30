# PheronAgent Results

This folder holds actual test-run artifacts from PheronAgent, the reference case study for the methodology in `METHODOLOGY_TR.md`. It exists to show what a real, non-hypothetical application of the methodology looks like — not as part of the universal methodology itself.

## Contents

- **98 result files** (`run_<model>_<YYYYMMDD>_k<n>[_<tag>].md` / `.json` / `.jsonl` / `.log`), following the naming and content conventions defined in Part II, Section 2.7 of the methodology document:
  - **Historical Batch (2026-06-29 – 2026-07-13)**: 32 original result files documenting the evolution from early exploratory runs to certified snapshots (`run_qwen3.5-9b_20260713_k5_scoringfinal.md`).
  - **Automated Runner Batch (2026-07-15 – 2026-07-30)**: 66 automated test runs and execution log files (`run_qwen3.5-9b_*_autorun*.json/md/log`), covering 86-block and 94-block benchmark suites.
- `datasets/` — 9 filled-in golden dataset schema files (`golden_dataset_seed.json`, `golden_dataset_86.json`, `golden_dataset_regression_check.json`, etc.), representing real-world test prompt batteries used during evaluation.

## Privacy & Public Auditing

All paths, personal identifiers, and environment configurations in this directory have been sanitized:
- Machine paths are standardized (`<USER_HOME>` / relative paths).
- Personal email identifiers are anonymized (`user@example.com`).
- Every `.json` and `.md` file has been verified against schema validity and sensitive string leak checks.

> [!TIP]
> **Note on Placeholders in Log Traces:**
> Log traces and JSON dataset files contain `<USER_HOME>` and `user@example.com`. If you attempt to re-run these reference datasets on your system, replace `<USER_HOME>` with your actual home directory (e.g., `/Users/username` or `C:\Users\username`) and `user@example.com` with your test email account.

## Reading these files

- Files with `run_type` marked `exploratory` — including early `k1`/`k3` runs — are bug-hunting logs, not certified results. See Section 2.6 of the methodology (Minimum-k Rule) for why.
- Files with `run_type` marked `published` (k=5 runs) represent certified regression/benchmark runs.
- `run_qwen3.5-9b_20260730_k5_autorun0707.md` / `.json` represents the latest 94-block automated benchmark snapshot.
- These files are PheronAgent-specific (test IDs, tool names, UBID numbers). If you're adapting the methodology to your own agent, don't copy these files — copy the *format* they follow, using the blank templates at the repository root (`templates/`).
