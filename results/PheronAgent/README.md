# PheronAgent Results

This folder holds actual test-run artifacts from PheronAgent, the reference case study for the methodology in `METHODOLOGY_TR.md`. It exists to show what a real, non-hypothetical application of the methodology looks like — not as part of the universal methodology itself.

## Contents

- **123 result files** (`run_<model>_<YYYYMMDD>_k<n>[_<tag>].md` / `.json` / `.jsonl` / `.log`), following the naming and content conventions defined in Part II, Section 2.7 of the methodology document:
  - **Historical Batch (2026-06-29 – 2026-07-13)**: 32 original result files documenting the evolution from early exploratory runs to certified snapshots (`run_qwen3.5-9b_20260713_k5_scoringfinal.md`).
  - **Automated Runner Batch (2026-07-15 – 2026-08-09)**: automated test runs and execution log files (`run_qwen3.5-9b*_autorun*.json/md/log`), covering 86-block and 94-block benchmark suites.
  - **126-Block Batch (2026-09-09)**: `run_qwen3.5-9b-4bit_20260908_k5_autorun1732.md` / `.json` — first certified k=5 run of the 126-block dataset (Version 10, see `CHANGELOG.md`).
  - **September Bug-Hunt Batch (2026-09-16 – 2026-09-24)**: 16 exploratory `k1`/`k3` runs (32 files) spanning a single, active refactor cycle on the 148/149/150-block dataset — see Version 11 in `CHANGELOG.md` for the full, honest breakdown of why the pass rate swings from 54.7% down to 3.1% and back up across this batch (it tracks a real regression being found and fixed mid-cycle, not measurement noise). Includes 4 single-block isolated debug probes (`xcodedebug*`) and 5 small targeted-verification runs (`officeverify*`, `continuityverify1914`, `socialisolated1152`).
- `datasets/` — 15 filled-in golden dataset schema files (`golden_dataset_seed.json`, `golden_dataset_94.json`, `golden_dataset_126.json`, `golden_dataset_148.json`, `golden_dataset_149.json`, `golden_dataset_regression_check.json`, `golden_dataset_social_isolated.json`, `golden_dataset_office_verify.json`, `golden_dataset_continuity_verify.json`, etc.), representing real-world test prompt batteries used during evaluation. `golden_dataset_149.json` (150 blocks as of 2026-09-24 — see the Version 11 note on the name/count mismatch) is the current main dataset going forward.
  - **Known gap, disclosed rather than hidden:** two datasets referenced by this batch's run files — `golden_subset_A1.json` (used by `subsetA11203`) and `xcode_mcp_tool_isolated.json` (used by the 4 `xcodedebug*` runs) — no longer exist in the source repo (they were temporary, scratch debug datasets, deleted after use) and could not be published here. The run result files themselves are still complete and published (they embed the actual prompts/responses inline), but the reusable dataset files for those two specific runs are unavailable.

## Privacy & Public Auditing

All paths, personal identifiers, and environment configurations in this directory are sanitized with `scripts/sanitize_and_publish.py` before publishing:
- Paths inside the source repo are made repo-relative (the repo-root prefix is stripped, not replaced with a placeholder).
- Paths outside the source repo (e.g. Desktop files referenced in a prompt) keep their structure but replace the real username with `<user>` (`/Users/<user>/...`).
- The real tester email is replaced with `user@example.com`, and the real phone number with `+90XXXXXXXXXX`.

> [!TIP]
> **Note on Placeholders in Log Traces:**
> Log traces and JSON dataset files may contain `/Users/<user>/...` and `user@example.com`. If you attempt to re-run these reference datasets on your system, replace `/Users/<user>` with your actual home directory and `user@example.com` with your test email account.

## Reading these files

- Files with `run_type` marked `exploratory` — including early `k1`/`k3` runs — are bug-hunting logs, not certified results. See Section 2.6 of the methodology (Minimum-k Rule) for why.
- Files with `run_type` marked `published` (k=5 runs) represent certified regression/benchmark runs.
- `run_qwen3.5-9b-4bit_20260908_k5_autorun1732.md` / `.json` remains the latest **certified** (k=5) benchmark snapshot — nothing in the September batch replaces it, since every one of those 16 runs is k=1/k=3 `exploratory` by the Minimum-k Rule. The September batch's highest result (`run_qwen3.5-9b-4bit_20260924_k1_autorun1632`, 82/150 = 54.7% pass@1) is the most current *exploratory* snapshot of active development, not a new certified number.
- **Metadata gap, disclosed:** several run files in the September batch show `"model_id": "unknown"` and `"git_commit": "fatal: not a git repository"` in their JSON header — a bug in the test harness's own metadata capture for those specific invocations, not a genuine ambiguity about what was tested. Every run in this batch used the same standing model (`qwen3.5-9b-4bit`, confirmed via the app's own persisted model preference and via the runs in the same window where capture worked correctly) — recorded here rather than silently filled in, so the gap itself stays visible.
- These files are PheronAgent-specific (test IDs, tool names, UBID numbers). If you're adapting the methodology to your own agent, don't copy these files — copy the *format* they follow, using the blank templates at the repository root (`templates/`).
