# Changelog

All notable changes to the methodology document are recorded here. Version numbers refer to the "Sürüm Geçmişi" table inside `METHODOLOGY_TR.md` itself — this file mirrors that table in English for readers who don't read the primary document end to end.

## Translation note — 2026-07-14

`METHODOLOGY.md`, a full English translation of `METHODOLOGY_TR.md` (Version 7, all 9 Parts), was added. This is a translation only — no content, test criteria, or citations were changed in the process. Two sections (`VisualWebArena`, `AssistantBench`) were caught missing from an initial machine-translated draft during verification (a heading-count and table-count diff against the Turkish source) and restored before publishing.

## Pre-history — 2026-05-02 to 2026-05-29 (before Version 1)

No methodology document existed yet. The true first artifact, per `git log`, was a forgotten 6-scenario `Tests/scenarios.json` committed 2026-05-02 as a side-effect of an unrelated daemon refactor — never run, never referenced again. A completely independent, unconnected effort started fresh 22 days later (2026-05-24): a Python harness (`Tests/RouterHealth/harness.py`) running a new hand-written scenario set that grew from 16 to 31 scenarios over the following days, establishing conventions (Turkish category codes like `HESAP`/`SISTEM`/`DOSYA`/`ZINCIR`, an `expected_tool` validation field, a "run everything first, fix in bulk afterward" discipline) that persisted through every later version. On 2026-05-29, a single project-wide cleanup commit deleted both the long-forgotten May 2nd file and the actively-used harness script and its result history — but not the 31-scenario data itself, which survived and resurfaced a month later as the seed of Version 1. See `STORY.md`, Chapter 0, for the full account.

## Version 7 — 2026-07-14

**Result file naming and content schema added (Part II, Section 2.7).**

- Extended the file-naming rule that previously covered only calibration runs (`calibration_<model>_<YYYYMMDD>.md`) to all test runs: `run_<model>_<YYYYMMDD>_k<n>[_<tag>].md` / `.jsonl`.
- Reviewed five industry eval harnesses/tools already cited in the bibliography (Inspect AI, OpenAI Evals, promptfoo, HAL leaderboard, DeepEval) and extracted the common pattern they all share: a run-level metadata header separate from per-sample records, and (in HAL's case) an explicit raw/summary file split.
- Defined a new `.jsonl` result-record schema (`record_type`, `model`, `verdict`, `latency_ms`, `cost_tokens` fields) going forward — historical files were not rewritten.
- Renamed 32 real result files in the working `results/` directory to the new convention (21 via `git mv`, 11 via plain `mv` for files not yet tracked). Model attribution (`qwen3.5-9b`) was verified from the `Model:` field present in every `.md` report from that period, not assumed.

## Version 6 — 2026-07-14

**2025–2026 gap-closing pass — 27 new external citations, all independently web-verified.**

- Added 5 new function-calling benchmarks (ToolSandbox, ComplexFuncBench, ACEBench, StableToolBench, MetaTool), a full τ²-bench section (dual-control, user simulator), TheAgentCompany, Terminal-Bench, SWE-Lancer, MLE-bench, and 6 new security benchmarks (ToolEmu, R-Judge, SafeAgentBench, PrivacyLens, ST-WebAgentBench, Cybench) plus BEAM (long-term memory).
- New Section 6.11: full **OWASP Top 10 for Agentic Applications 2026** (ASI01–ASI10) taxonomy table, cross-mapped to the 6 universal security test blocks. Section 6.12: a coverage-control cross-check against a 40-benchmark safety taxonomy survey (arXiv:2605.16282).
- Section 8.5 expanded with **OWASP MCP Top 10** and MCP supply-chain security methodology.
- 7 new methodology subsections in Section 9: cost/latency (9.5, CLEAR + HAL), production observability (9.6, OTel GenAI semconv + LangSmith/Arize/Langfuse/Weave), eval harness selection guide (9.7), automated red-teaming (9.8, garak/PyRIT/DeepTeam), benchmark reliability & anti-gaming (9.9), multi-agent system testing (9.10), regulatory alignment map (9.11, NIST AI RMF/MITRE ATLAS/EU AI Act/ISO 42001).
- New Section 11.4: coverage cross-check against the IBM ACL 2026 five-perspective agent-evaluation survey (arXiv:2503.16416).
- Bibliography citation count: 34 → 61. One agent-proposed source ("MCP-Atlas benchmark") could not be independently verified and was replaced with the real OWASP MCP Top 10; "CyBench" was corrected to its actual name, "Cybench" (arXiv:2408.08926).

## Version 5 — 2026-07-14

**Scope reframing.** The document's primary identity was redefined from "PheronAgent's own test document" to "a universal agent test methodology, with PheronAgent as one case study." Each of the 58 core blocks in Part II was split into a tool-agnostic **Universal Capability** definition and a concrete **PheronAgent Reference Implementation**. Part 13 and Part IV were explicitly labeled as PheronAgent-specific case study material. The whole document was re-read end to end for internal consistency: table-of-contents/heading mismatches, verification that `RouterHealthTests` genuinely exists in code, reflection of the k=5 run (436 records / 86 tests) in `results/`, and resolution of an internal contradiction in the Hermes citation's verification count. The front matter was restructured into a professional format (what it is → how to use it → table of contents), and the version history table was moved here.

## Version 4 — 2026-07-08

**Five methodological gaps closed** in the document's claim to be usable as a third-party reference: calibration/control-group procedure (Section 2.4 — procedure defined, run itself still pending), inter-rater reliability (2.5), minimum-k rule (2.6), reusable blank templates (`templates/`), and a license (`LICENSE`, CC BY 4.0 for docs + MIT for code).

## Version 3 — 2026-07-01

**Part IX (Bibliography and Verification Method) added.** 26 academic citations consolidated into a single list; 3 (NESTFUL, GAIA, WildClawBench) independently web-verified in this pass. A UBID:22 counting error was corrected.

## Version 2 — 2026-06-30

File-name mismatches and the overlap between Part II and Part III were resolved. 19 of 29 UBID coverage gaps were closed (Section 13 addendum added, total block count 58 → 77). Memory UBID collisions and other issues requiring source-code access were explicitly marked "unresolved" rather than guessed at.

## Version 1 — 2026-06-29

**Origin.** Seven source files (`agent_testing_procedures.md`, `PROTOCOL.md`, `agent_testing_protocol.md`, `tool_testing_protocol.md`, `tool_testing_procedures.md`, `README.md`, and a PDF report) were merged without loss — verified line by line via diff. This same day also saw the first live end-to-end test run: 31 scenarios from `Tests/RouterHealth/scenarios_v2.json` executed against a running instance of the agent, producing the first `run_YYYYMMDD_HHmm.md` result report and surfacing the first real infrastructure gaps (a referenced `RouterHealthTests` class that didn't exist; a deleted `harness.py` runner; a 30s test-runner timeout too short for a 9B local model's ~70–120s planning turns).
