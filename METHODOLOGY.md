# Agent Testing Documentation — Universal Methodology + PheronAgent Case Study

**Version 7 · 2026-07-14**

---

## What This Is

This document is a **universal agent testing methodology and test battery**, independent of PheronAgent, that developers building agents on any architecture, language, or toolset can use directly. PheronAgent is a single **reference case study** showing how this methodology applies to a real agent — it is not the methodology itself.

The document has five layers: a map of the industry's agent-evaluation benchmarks (Part I), a directly applicable universal test protocol (Part II), concrete examples of how that protocol plays out on a real agent (Parts III, IV, VI), an aspirational verifiability vision not yet implemented (Part V), and a verification record showing that every external claim traces back to a checkable source (Parts VII–IX).

## How to Use It

| Your goal | Where to look |
|---|---|
| A ready-made test battery for your own agent | **Part II, Sections 4–10** — 58 core blocks. Each block is split into a "Universal Capability" (tool-agnostic definition) and a "PheronAgent Reference Implementation" (concrete example); adapt by replacing only the reference-implementation field with your own agent's tool names. |
| Blank, project-neutral template files | `templates/` (`golden_dataset.template.json`, `BLANK_TEST_BLOCK.template.md`) |
| Understanding industry benchmarks | **Part I** — summarizes what 61 academic/industry sources measure, including BFCL, GAIA, τ-bench, NESTFUL |
| Seeing the methodology applied to a real agent | **Parts III, IV, VI** — PheronAgent's tool catalog, internal reconciliation process, file inventory (case study; not a template to copy directly) |
| Advanced/aspirational verifiability ideas (cryptographic proofs, ZKP, a global transparency portal) | **Part V** — explicitly marked as not yet implemented, a vision document disproportionate in scale for a single-developer project |
| Auditing this document's own reliability | **Parts VII–IX** — detected inconsistencies, resolution records, verification status of every external citation |

For reuse terms, see `LICENSE` (CC BY 4.0 for the methodology, MIT for template files).

---

## Table of Contents

- **Part I — Industry Benchmark Map** (source: `agent_testing_procedures.md`)
  Function-calling, multi-step reasoning (including τ²-bench), web/browser, OS/GUI/terminal, software engineering, security (including OWASP Top 10 for Agentic Applications 2026 / ASI01–ASI10), and memory benchmarks; MCP security (OWASP MCP Top 10); OpenClaw/Hermes harness analysis; evaluation methodology (LLM-as-judge, pass^k, exact match vs. partial credit, cost/latency, production observability, automated red-teaming, benchmark reliability, multi-agent systems, regulatory alignment map).

- **Part II — Universal Agent Test Battery + PheronAgent Reference Implementation (Current, Canonical — Active)** (source: `PROTOCOL.md` v1.1 + Section 13 addendum)
  Environment setup, golden dataset, acceptance/rejection taxonomy, **77 test blocks** (58 universal core blocks L1–L4/HR/MT/GÜV — each split into Universal Capability + PheronAgent Reference Implementation — + 19 EK-TOOL case-study blocks), CI integration, result template.

- **Part III — Early Draft Format (Archive/Historical — Inactive)** (source: `agent_testing_protocol.md`)
  The predecessor/parallel version of PROTOCOL.md — ROUTE/UBID/CHAIN/MEM/SEC test blocks, Intent and UBID matrices. No longer in active use, reference only.

- **Part IV — Tool Catalog and Functional Test Procedures (PheronAgent Case Study)** (source: `tool_testing_protocol.md` + `tool_testing_procedures.md`)
  Categorical test methods and concrete L3-TOOL test scenarios for 50+ native/external MCP tools — not part of the universal battery, PheronAgent-specific. 19 were moved to Part II Section 13; 10 remain recorded as a genuine coverage gap.

- **Part V — Global Verifiability Vision (Advanced/Aspirational Roadmap)** (source: PDF report, Version 2.0)
  Cryptographic execution records (CER), SPIFFE identity, ZKP-based model verification, Docker/QEMU virtualization, anti-gaming protocol.

- **Part VI — File Inventory and Source Map** (source: `README.md` + actual file state)

- **Part VII — Open Issues, Inconsistencies, and Known Limitations (Consolidated Record — Detection Phase)**
  All "TODO/open question/gap" items from every source, collected in a single list.

- **Part VIII — Reconciliation Results and Verification Record**
  Resolution status of every item in Part VII: resolved / partially resolved / requires source-code access. No item was closed with fabricated data.

- **Part IX — Bibliography and Verification Method**
  Internal sources (7 documents), external academic/industry citations (61 benchmarks/standards/tools, by category — including OWASP ASI 2026 and MCP security, τ²-bench, cost/observability/red-team methodology), technical standards (RFC 8785, SPIFFE, NIST RMF, MITRE ATLAS, EU AI Act, ISO 42001, etc.), verification method, and this document's own scope/limits statement.

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1 | 2026-06-29 | 7 source files (`agent_testing_procedures.md`, `PROTOCOL.md`, `agent_testing_protocol.md`, `tool_testing_protocol.md`, `tool_testing_procedures.md`, `README.md`, PDF report) merged without loss — verified line by line via diff. |
| 2 | 2026-06-30 | File-name mismatches and the Part II/III overlap resolved. 19 of 29 UBID coverage gaps closed (Section 13 addendum added, total block count 58→77). Memory UBID collisions and other issues requiring source-code access were explicitly marked "unresolved." |
| 3 | 2026-07-01 | Part IX (Bibliography and Verification Method) added. 26 academic citations consolidated into a single list; 3 (NESTFUL, GAIA, WildClawBench) independently web-verified. A UBID:22 counting error was corrected. |
| 4 | 2026-07-08 | 5 methodological gaps closed in the document's claim to serve as a third-party reference: calibration/control-group procedure (Section 2.4, run itself still pending — "EXECUTION PENDING"), inter-rater reliability (2.5), minimum-k rule (2.6), reusable blank templates (`templates/`), license (`LICENSE`, CC BY 4.0 + MIT). |
| 5 | 2026-07-14 | **Scope clarification:** The document's primary identity was reframed from "PheronAgent's own test document" to "a universal agent test methodology, with PheronAgent as one case study." Each of Part II's 58 core blocks was split into "Universal Capability" (tool-agnostic) + "PheronAgent Reference Implementation" (concrete example); Section 13 and Part IV were explicitly labeled "PheronAgent-specific case study." The whole document was also re-read end to end and internal inconsistencies fixed: TOC/heading mismatches, verification via code that `RouterHealthTests` now genuinely exists, reflection of the k=5 run (436 records/86 tests) in `results/`, resolution of an internal contradiction in the bibliography's verification counts (Hermes). The front matter (purpose/usage) was brought into a professional document format (what it does → how to use it → table of contents), and the version history was moved here. |
| 6 | 2026-07-14 | **2025–2026 gap-closing pass (27 new external citations, all independently web-verified):** Added to Part I: 5 new function-calling benchmarks (ToolSandbox, ComplexFuncBench, ACEBench, StableToolBench, MetaTool), τ²-bench (full section, dual-control), TheAgentCompany, Terminal-Bench, SWE-Lancer, MLE-bench, 6 new security benchmarks (ToolEmu, R-Judge, SafeAgentBench, PrivacyLens, ST-WebAgentBench, Cybench), and BEAM. New Section 6.11: full **OWASP Top 10 for Agentic Applications 2026** (ASI01–ASI10) taxonomy table + cross-mapping to the existing GÜV-01..06 tests; Section 6.12: a coverage-control survey of 40 benchmarks (arXiv:2605.16282). Section 8.5 expanded with **OWASP MCP Top 10** and MCP supply-chain security methodology. 7 new methodology subsections added to Section 9: 9.5 cost/latency (CLEAR, HAL), 9.6 production observability (OTel GenAI semconv, LangSmith/Arize/Langfuse/Weave), 9.7 eval harness selection guide, 9.8 automated red-teaming (garak/PyRIT/DeepTeam), 9.9 benchmark reliability/anti-gaming, 9.10 multi-agent system testing, 9.11 regulatory alignment map (NIST RMF/MITRE ATLAS/EU AI Act/ISO 42001). Section 11.4 added: coverage cross-check against the IBM ACL 2026 five-perspective survey (arXiv:2503.16416). Part IX citation count: 34→61; the unverifiable "MCP-Atlas" name proposed by an external research pass was dropped in favor of the real OWASP MCP Top 10; "CyBench" was corrected to its actual name, "Cybench" (arXiv:2408.08926). |
| 7 | 2026-07-14 | **Result-file naming and content schema added (Section 2.7):** The file-naming rule, previously defined only for calibration runs (`calibration_<model>_<YYYYMMDD>.md`), was extended to cover ordinary runs as well: `run_<model>_<YYYYMMDD>_k<n>[_<tag>].md/.jsonl`. The result-record formats of five industry tools (Inspect AI, OpenAI Evals, promptfoo, HAL harness, DeepEval — all independently web-verified) were reviewed and a common pattern extracted (run-level metadata record + sample-level attempt record, raw/summary separation); a new `.jsonl` schema based on this (`record_type`, `model`, `verdict`, `latency_ms`, `cost_tokens` fields) was defined — historical file content was not changed. The 32 real result files in `results/` were migrated to this new naming format (21 via `git mv`, 11 via `mv`); model attribution (`qwen3.5-9b`) was verified from the `Model:` field present consistently in every `.md` report, not assumed. |

---
