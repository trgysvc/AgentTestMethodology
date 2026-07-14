# AgentTestMethodology

**Universal AI Agent Testing Methodology — with PheronAgent as Reference Case Study**

Version 7 · 2026-07-14

---

## What This Is

A framework-agnostic, architecture-independent test methodology and battery that any agent developer can apply directly to their own project — regardless of language, runtime, or toolset.

The primary document exists in two languages: `METHODOLOGY.md` (English) and `METHODOLOGY_TR.md` (Turkish, the original — this is where the methodology was actually developed; see `STORY.md`). Both are structured in five layers:

| Layer | Content |
|---|---|
| **Part I** | Industry benchmark map — what 61 academic and industry sources measure, and how to use them |
| **Part II** | Universal test battery — 58 core blocks (L1–L4 / Error Recovery / Multi-Turn / Security), each split into a tool-agnostic *Universal Capability* definition and a concrete *Reference Implementation* |
| **Parts III–IV, VI** | PheronAgent case study — how the methodology applies to a real agent with 50+ native/MCP tools (read for examples; do not copy verbatim) |
| **Part V** | Advanced verifiability roadmap — cryptographic execution proofs, ZKP-based model verification, anti-gaming protocol (explicitly marked as aspirational/not yet implemented) |
| **Parts VII–IX** | Audit trail — open issues, reconciliation log, full bibliography with verification status for every external claim |

**PheronAgent is one case study.** The methodology is the product.

---

## Quick Start

**To build a test battery for your own agent:**
→ Part II, Sections 4–10. Replace "PheronAgent Reference Implementation" fields with your own agent's tool names and expected outputs. The Universal Capability definitions require no changes.

**To understand which benchmarks to cite:**
→ Part I (61 benchmarks/standards/tools, categorized) + Part IX bibliography.

**To get blank, project-neutral templates:**
→ `templates/golden_dataset.template.json` and `templates/BLANK_TEST_BLOCK.template.md`

**To audit this document's own claims:**
→ Parts VII–IX — detected inconsistencies, resolution records, and verification status of every external citation.

**To read how this came to exist:**
→ `STORY.md` — the actual multi-week process: real bugs found in a running agent, real test runs, real corrections. Not a marketing narrative.

---

## Coverage

### Benchmark Categories (Part I)

- **Function-calling / Tool Use** — BFCL, API-Bank, ToolBench, NESTFUL, ToolSandbox, ComplexFuncBench, ACEBench, StableToolBench, MetaTool
- **Multi-step Reasoning** — GAIA, AgentBench, τ-bench, τ²-bench (dual-control, user simulator)
- **Web / Browser** — WebArena, Mind2Web, WebVoyager, BrowserGym, VisualWebArena, AssistantBench
- **OS / Desktop / Terminal** — OSWorld, AndroidWorld, Windows Agent Arena, Terminal-Bench
- **Software Engineering** — SWE-bench, SWE-Lancer, MLE-bench
- **Security / Adversarial** — InjecAgent, AgentDojo, AgentHarm, ToolEmu, R-Judge, SafeAgentBench, PrivacyLens, ST-WebAgentBench, Cybench + OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) full taxonomy
- **Memory / Long Context** — LongMemEval, LoCoMo, BEAM (1M and 10M token scale)
- **Harness Ecosystem** — OpenClaw/Hermes, WildClawBench, HAL, CLEAR

### Methodology Sections (Part I, Section 9)

| Section | Topic |
|---|---|
| 9.1 | LLM-as-Judge — known biases and mitigation strategies |
| 9.2 | pass@k vs. pass^k — when each applies, practical collapse table |
| 9.3 | Exact match vs. partial credit |
| 9.4 | Trajectory vs. end-state evaluation |
| 9.5 | Cost and latency metrics (CLEAR framework, HAL leaderboard approach) |
| 9.6 | Production observability — OpenTelemetry GenAI semantic conventions, LangSmith / Arize Phoenix / Langfuse / W&B Weave |
| 9.7 | Eval harness selection guide |
| 9.8 | Automated red-teaming — garak, PyRIT, DeepTeam |
| 9.9 | Benchmark reliability and anti-gaming |
| 9.10 | Multi-agent system testing |
| 9.11 | Regulatory alignment map — NIST AI RMF, MITRE ATLAS, EU AI Act, ISO/IEC 42001 |

### Security Coverage (Part I, Sections 6.11–6.12)

Full OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) taxonomy table with cross-mapping to the 6 universal security test blocks in Part II. Includes OWASP MCP Top 10 and MCP supply-chain security methodology (Section 8.5), plus a coverage-control survey of 40 agent safety benchmarks published April 2023–March 2026 (arXiv:2605.16282).

### Test Battery (Part II)

58 universal core blocks across 7 tiers:

| Tier | Blocks | Focus |
|---|---|---|
| L1 Basic | 21 | Routing, tool selection, parameter accuracy |
| L2 Intermediate | 11 | Chained tool calls, context carryover |
| L3 Advanced | 7 | Nested output passing, long-horizon planning |
| L4 Professional | 5 | Live inference, production-grade tasks |
| Error Recovery | 4 | Graceful failure, retry logic |
| Multi-Turn | 4 | Policy consistency, session memory |
| Security | 6 | Injection, privilege escalation, data exfiltration |

Each block specifies: prerequisite tier, test type, input prompt, expected behavior (universal), acceptance criteria, rejection criteria, and a PheronAgent reference run for comparison.

---

## Repository Structure

```
AgentTestMethodology/
├── METHODOLOGY.md                     # Primary document, English (v7, ~5750 lines)
├── METHODOLOGY_TR.md                  # Primary document, Turkish original (v7, ~5700 lines)
├── STORY.md                           # How this methodology actually came to be
├── README.md                          # This file
├── LICENSE                            # MIT — templates and code
├── LICENSE-docs.md                    # CC BY 4.0 — documentation and methodology
├── CHANGELOG.md                       # Version-by-version history
├── templates/
│   ├── BLANK_TEST_BLOCK.template.md   # Empty test block — fill in for your agent
│   └── golden_dataset.template.json   # Golden dataset schema
└── results/
    └── PheronAgent/
        ├── README.md                    # What this folder contains
        ├── datasets/                    # Filled-in golden-dataset examples (seed + smoke)
        └── run_qwen3.5-9b_*.{md,jsonl}  # 32 real result files, Section 2.7 naming — see folder README
```

---

## Reuse

**Documentation and methodology** (METHODOLOGY.md, METHODOLOGY_TR.md, README.md, all `.md` content): [CC BY 4.0](LICENSE-docs.md) — free to use, adapt, and distribute with attribution.

**Templates and code** (`templates/`, any scripts): [MIT](LICENSE) — no restrictions.

Attribution example: *"Based on AgentTestMethodology by Turgay Soysal (github.com/trgysvc/AgentTestMethodology), CC BY 4.0"*

---

## Scope and Honest Limitations

This document makes the following claims — and only these:

- The 58 universal test blocks in Part II are directly applicable to any agent architecture.
- The benchmark descriptions in Part I reflect published academic and industry sources; every external claim has a citation and a verification status in Part IX.
- PheronAgent results reflect actual test runs where stated; sections marked "EXECUTION PENDING" have not yet been run.
- Part V (cryptographic verifiability roadmap) is explicitly aspirational — not implemented, not planned for near-term, included for community discussion only.

What this document does not claim: that it covers every possible agent evaluation scenario, that the PheronAgent results are reproducible on other hardware without adjustment, or that any benchmark score from Part I applies to your agent without running it yourself.

---

## Contributing

Issues and pull requests are welcome for:

- Benchmark additions or corrections (with citation)
- Errors in the universal test blocks
- Template improvements
- Translations of the methodology sections

Please open an issue before submitting a PR for structural changes to Part II.

---

## Version History

See [`CHANGELOG.md`](CHANGELOG.md) for the full version-by-version history (currently at Version 7). For the story behind *why* each version changed what it changed — including the real bugs and dead ends that drove it — see [`STORY.md`](STORY.md).
