# Blank Agent Test Block Template

License: CC BY 4.0 — see `../LICENSE`. Fork freely, attribution appreciated.

This is a project-agnostic fill-in template for a single agent test block, extracted
from the Pheron Agent test documentation methodology (Kısım II — Operasyonel Test
Protokolü). It is **format only** — no Pheron-specific tool names, UBIDs, or prompts
are implied by this template. Copy this block once per test case into your own suite.

See `golden_dataset.template.json` for the machine-readable equivalent of the same
fields — keep both in sync if you extend either.

---

## Test Block Anatomy

| Field | Fill in |
|---|---|
| **Test ID** | `<LEVEL>-<CATEGORY>-<NN>` (e.g. `L1-MATH-01`) — your own naming scheme |
| **Level** | Which tier of your suite this belongs to (define your own L1..Ln or equivalent) |
| **Category** | Functional area this block probes |
| **Prompt** | Exact input given to the agent, verbatim, reproducible |
| **Layer** | Unit \| Integration \| E2E \| Live (adapt to your architecture — see note below) |
| **Yakalayan katman / Resolving layer** | Which internal component is expected to handle this (deterministic rule, classifier, small model, LLM, etc.) |
| **Evaluation type** | `STATE` (exact/structural match) \| `KEYWORD` (substring/keyword match) \| `JUDGE` (semantic, requires a scored judge — calibrate against human raters, target Cohen's kappa >= 0.6) |
| **Expected outcome** | What must be true for PASS — tool called, parameters, result content, etc. |
| **Fail patterns** | Concrete, enumerable conditions that constitute FAIL — not a vague description |
| **k (repetitions)** | Minimum 5 before this block's result may be reported as a published pass rate. k<5 is exploratory/bug-hunting only. |
| **Threshold** | Do not hardcode a number until you have measured a baseline first (measure, then set the threshold — never the reverse) |
| **Tester** | Fixed identity string of whoever ran/graded this (human or model) — required for inter-rater tracking |
| **Run type** | `exploratory` (k<5) or `published` (k>=5, externally shareable) |
| **Teardown** | Exact commands/state resets needed after this block runs, so re-runs start clean |

### Four-layer test architecture (adapt, don't copy verbatim)

```
Layer 4 — LIVE
  Requires: full app/service running + real network + real credentials
  Runs in CI: NO (network-dependent, rate limits, provider variance)

Layer 3 — E2E
  Requires: full app/service running, no network needed
  Runs in CI: depends on whether your CI environment has the required runtime
              (e.g. GPU/accelerator access)

Layer 2 — Integration
  Requires: mocked provider/backend, no real model or network
  Runs in CI: YES

Layer 1 — Unit
  Requires: language runtime only
  Runs in CI: YES
```

### Minimum-k and publishing rule (carry this rule over, it's not optional)

A pass rate computed from fewer than 5 trials (k<5) has wide, usually unstated
uncertainty. Do not publish a percentage derived from k<5 as a result — label it
`exploratory` and use it only to find and fix bugs. Only report a percentage
externally once k>=5 for that block, and prefer pairing it with a pass^k figure
(the probability that all k trials succeed, not just at least one) when the
target use case is unattended/autonomous execution — a single pass@1 figure can
look deceptively strong while pass^k for repeated autonomous runs is much lower.

### Calibration note

If you intend to publish comparative numbers (e.g. "our agent scores X on this
suite"), run the identical block set through at least one independently known
reference system first, using the same grading rubric. This tells a third-party
reader whether a low score reflects a weak agent or an unusually strict suite —
without it, your own percentage is not interpretable by anyone outside your team.

---

## Fill-in block (copy this section per test case)

**Test ID:**
**Level:**
**Category:**
**Prompt:**
**Layer:**
**Yakalayan katman / Resolving layer:**
**Evaluation type:**
**Expected outcome:**
**Fail patterns:**
**k:**
**Threshold:**
**Tester:**
**Run type:**
**Teardown:**
**Notes:**
