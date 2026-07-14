# The Story Behind This Methodology

This is not a marketing narrative. It's a reconstruction — from actual session transcripts — of how a single developer's frustration with an unreliable local AI agent turned into a 5,700-line, 61-citation testing methodology. Every bug mentioned here was real, found in a running system, and fixed (or explicitly left open) in the code. Every date is accurate. Where the process was messy, it's described as messy.

The subject throughout is **PheronAgent**, a macOS-native AI agent running a local 9B-parameter model (Qwen3.5-9B). The methodology that emerged from testing it is now meant to outlive it.

A note on completeness: this account is built from two independent kinds of evidence. Session transcripts (chat history) were mined in two passes — one covering 2026-06-29 onward, a second hunting backward for earlier test-related activity — but transcripts alone bottomed out at 2026-05-24, with a session that already showed a working test harness and no record of how it got there. That gap was closed with a more reliable source: `git log`. Commit history doesn't summarize or forget, so it's used here as the source of record wherever the two disagree or transcripts run out.

---

## Chapter 0 — The Engine That Was Sacrificed (2026-05-02 to 2026-05-29)

Git history places the actual zero point at **2026-05-02**, in commit `7cb6ea03`: `refactor: implement XPC-based EliteService daemon with enhanced orchestration and autonomous audit automation scripts`. Buried inside that unrelated infrastructure commit, as an apparent afterthought, was a new 34-line file: `Tests/scenarios.json` — six scenarios (`SYS_001`, `WET_001`, `GIT_001`, `XCD_001`, `CAL_001`, `SHL_001`), each just a prompt and a list of expected tool-ID numbers. No harness came with it. Nothing in the commit or the sessions around it suggests a deliberate "let's start testing" decision — it reads like a developer jotting down a handful of sanity-check prompts while building something else entirely.

Then nothing happened to it for 27 days. It was never run, never referenced again, and — as the record shows below — never even remembered when the *next* test harness was built.

That next attempt started fresh, unconnected, on **2026-05-24** (commit `de53e922`, again nominally about something else — "usage tracking for API tasks, daily log rotation, daemon support"). In one commit, 324 lines of `Tests/RouterHealth/harness.py` and a new 189-line `Tests/RouterHealth/scenarios.json` appeared together — a different location, a different ID scheme (`CHAT-001`, `TOOL-001..008`, `CHAIN-001..003`, `CLARIFY-001..002` — 16 scenarios, no overlap at all with the May 2nd file), built as if the earlier one didn't exist. It's not a rewrite or an expansion; it's independent invention of roughly the same idea, three and a half weeks later, by the same project.

The same day the harness was created, it was put to work — the first full, live, end-to-end run, internally code-named **"Hermes"** in that day's conversation (a project nickname for the test marathon itself, not a model). The instruction that kicked it off set a rule that would resurface, in slightly different words, for the rest of this project's life:

> *"You'll run the app in the background like we did for Hermes, and test our prompts one by one, in order. You will not try to fix anything that goes wrong. Everything's being logged anyway. Once every test is done, we'll fix the broken or slow ones one at a time."*

Run everything first. Don't fix mid-flight. Fix in bulk, with full evidence, afterward. That single instruction is the direct ancestor of the "list findings, discuss, then fix" rule and the "test documentation is our constitution" stance that show up again and again later in this story.

The run itself was uneven, and it was left uneven on purpose. `PASS [TOOL-003] 37.6s`. `PASS [TOOL-004] 898.1s` — nearly fifteen minutes, because of a CLARIFY-vs-Critic deadlock that the harness patiently waited out instead of timing out. `FAIL [TOOL-006]`, `FAIL [TOOL-007]`, `FAIL [TOOL-008]` — routing and tool-selection problems, noted and left alone, exactly as instructed. By 2026-05-25, the marathon was declared complete.

The very next day, 2026-05-26, the harness was rebuilt around a much larger scenario set — 30 scenarios, written in Turkish, organized under category codes that would survive, essentially unchanged, all the way to the 77/86-block battery that exists today: `HESAP` (arithmetic), `SISTEM` (system info), `DOSYA` (files), `HAVA` (weather), `UYGULAMA` (app launching), `CLARIFY`, `ZINCIR` (tool chains), `EDGE`. Results were captured into a file called `results_v2.json` — the direct naming ancestor of what would later become `scenarios_v2.json`.

That run surfaced the first hard bug the "don't fix mid-flight" rule was ever tested against: `HESAP-03` crashed the server outright — an `NSExpression` evaluation throwing an Objective-C exception that Swift's `try/catch` structurally cannot intercept. Per the standing instruction, it wasn't touched. It was logged as a known server-crash bug and skipped, to be dealt with later, with everything else.

Over the following two days (05-26 into 05-27), a second class of problem showed up: thermal throttling. `ZINCIR` scenarios that ran fine early in a session started failing later in the same session — not because the logic was wrong, but because the Apple Neural Engine had throttled down after sustained load, and later turns simply took too long. Partial re-runs (`--skip N`) were used to isolate just the affected subset — the first appearance of "hardware state affects test outcome" as a variable this project had to account for, weeks before Part 9.5's cost/latency section gave it a name.

By 2026-05-28, in a session working directly inside `Tests/RouterHealth/`, the harness's own validation logic was tightened: each scenario's `expected_tool` field was clarified (`null` meaning "any tool call is acceptable"), a stale, unrelated Swift Package test (`testResearchCategoryHasWebSearch`) was deleted, and a new scenario — `SAF-01` — was added specifically to verify a Safari `performSearch` fix, bringing the set to 31 scenarios. The session ended clean: **31/31 passing.**

Then, on 2026-05-29, in a session explicitly about project-wide cleanup ("Project Structure Cleanup & Standardization"), `Tests/RouterHealth/` was flagged as clutter — 28 accumulated `results_*.json` files plus the harness script itself. With approval, one command ran:

```
rm -f Tests/RouterHealth/results_*.json Tests/RouterHealth/harness.py Tests/scenarios.json
```

`harness.py` — the engine — was gone. Every historical result file was gone. `Tests/scenarios.json` — the original six-scenario file from May 2nd, untouched and unreferenced for 27 days — was finally, quietly deleted in the same command, having never once been run. But look closely at what's *not* in that command: **`scenarios_v2.json` is missing from it.** The 31 hand-written, Turkish-language golden scenarios that had actually been used survived. Only the things nobody had touched in weeks — the forgotten first attempt, and the engine that replaced it — were swept away together.

Nobody noticed the engine was gone for exactly one month.

---

## Chapter 1 — Why Testing Became Non-Negotiable (2026-06-29)

The day didn't start as a testing effort. It started with ordinary product bugs: chat sessions bleeding state into each other, a greeting handler that ignored an unfinished prior conversation, an agent that got stuck in an infinite retry loop because its own "no placeholder data" guard treated a Markdown checkbox (`- [ ]`) as fake data. Each was diagnosed from `audit.log` and `conversation.log`, fixed, rebuilt, and reloaded — the ordinary rhythm of iterating on a live agent.

One fix revealed a deeper problem. A `RESUME RULE` had been added to the system prompt with a *literal example* baked in — "Finland startup visa" — because that had been the topic of a recent debugging session. The model, as local 9B models do, over-attended to whatever concrete example sat in its instructions. It started steering unrelated conversations back toward Finland. When this was pointed out, the response was blunt: hardcoded examples in a system prompt aren't a fix, they're a new bug waiting to surface. No code was touched until the instruction was rewritten to derive its example dynamically instead of from a fixed string.

That exchange set the tone for everything that followed: **explanations had to be verified against logs, not asserted from a plausible-sounding theory.**

Then the focus shifted to `Tests/AgentTestSuite/`, with one instruction: look, report, don't touch anything yet.

The report was not encouraging:

- `PROTOCOL.md` and `README.md` both referenced a `RouterHealthTests` XCTest class that **did not exist**. The Python harness (`harness.py`) that used to run the scenarios in `scenarios_v2.json` — the same engine sacrificed exactly one month earlier in the 2026-05-29 cleanup pass (Chapter 0) — had been deleted, and nothing had replaced it. The 31 golden scenarios that survived that cleanup had been sitting unused for a month.
- A `golden_dataset_v1.json` file was documented as present. It wasn't.
- Helper scripts (`marathon_runner.sh`, `full_audit_runner.sh`) referenced test class names, executable targets, and resource paths that had all been renamed months earlier. They would "pass" by silently running zero tests.
- The CI layer-2 integration tests were configured to skip themselves unless `PHERON_LIVE_INFERENCE=1` — while the protocol document told CI to set that variable to `0`. The tests had never actually run in CI.

A stopgap Python runner (`run_scenarios.py`) was written to replace the deleted harness, and the first live test run began: 31 scenarios, one at a time, against a running instance of the agent on port 11500.

It did not go smoothly, and that was the point. The first run immediately hit a **BUSY cascade**: the runner's timeout (30s) was shorter than the local model's actual planning time (up to 120s for a single turn), so when a request timed out, the runner kept firing new requests at a server that was still mid-task. Every one of those got rejected in under a millisecond. Fixing it meant raising the timeout to 180s and adding a "wait until the server reports itself ready" loop before sending the next scenario — the test harness itself needed engineering, not just the agent under test.

By the end of the day: 3 real unit-test mismatches were found and fixed in `FileToolTests.swift` (the tests expected old error-message wording and an old `/tmp` remapping behavior that newer, stricter workspace-isolation code had superseded), the first `run_20260629_HHmm.md` reports existed, and it was clear the test *infrastructure* — not just the agent — had significant rot to clear out.

---

## Chapter 2 — Two Wrong Numbers (2026-07-01)

Before running anything at scale, `PROTOCOL.md` itself got a line-by-line audit against the actual tool registry (`ToolIDs.swift`). Two real errors surfaced:

- **L1-DOSYA-03** ("list desktop files") was documented as UBID:38. The actual directory-listing tool, `file_manager_action`, is UBID:39. UBID:38 belongs to an unrelated tool, `contacts_find`.
- **L1-UYGULAMA-01** ("launch an application") was documented as UBID:35. The actual launcher, `app_launcher`, is UBID:88. UBID:35 belongs to `learn_application_ui`.

These weren't cosmetic. A test grader checking logs for "UBID:38 was called" on a test that actually needed UBID:39 would have marked a *correctly working agent* as a failure — or worse, silently accepted a wrong tool call as a pass because it happened to match a wrong expected number. Both were corrected at the source.

With the protocol text fixed, the same systematic-audit approach was turned on the *mechanism* meant to run it: no `RouterHealthTests.swift` existed to execute the 31 golden scenarios automatically; `golden_dataset_v1.json` and `results/baseline_YYYYMMDD.json` — files the document's own calibration procedure depended on — had never been generated, meaning the "measure first, then set a threshold" rule the document preached had never actually been followed by the document itself.

This is also where a separate, more speculative artifact entered the picture: a PDF report proposing a "verifiable testing" vision — cryptographic execution proofs, ZKP-based model verification, SPIFFE workload identity, Docker/QEMU sandboxing. Rather than discard it or treat it as equal to the operational protocol, it was merged in as `MASTER_PROTOCOL.md` with every aspirational section explicitly tagged `[VISION/UNVERIFIED]` — a labeling discipline that survives today in Part V of the methodology ("Advanced Verifiability Roadmap — explicitly aspirational").

---

## Chapter 3 — The 44% That Wouldn't Be Waved Away (early July)

With the protocol corrected and the harness stabilized, the first full run of all 77 defined test blocks happened. The result: roughly **44% pass** (35 pass / 38 fail / 3 skip / 4 partial), recorded in `run_20260701_1603.md`.

The response to that number was not "good enough for a first pass" — it was a direct question back: *are the tests marked PASS actually verified against evidence, or is this just counting up numeric labels?* That single question shaped everything that came after. From that point forward, a PASS required a specific, checkable claim in the logs — not a plausible-sounding summary. And the test documentation itself was elevated to the standard everything else had to answer to: *"the test documentation is our constitution — we operate according to it."*

Chasing the 44% down to root causes surfaced a run of real engine bugs, each fixed and re-verified before moving to the next:

- An **anti-narration guard** meant to force the agent to emit a structured `<final>` block instead of free text was false-positive-ing on legitimate first-turn no-tool answers. A dedicated `ANSWER()` protocol tag was introduced, and a parser bug where a slightly different closing-bracket variant the model actually produced (`")}</final>`) silently failed to match was fixed alongside it.
- The **hardware fast-path**, meant to shortcut simple system-info requests straight to a tool call, was collapsing *compound* requests (e.g., "macOS version and CPU temperature") down to a single tool call instead of two.
- **Widget silence**: a stale or empty cached response (`collector.response`) was in some cases overriding the model's actual final answer (`session.finalAnswer`).
- A **BUSY deadlock** traced to `GitStateEngine` spawning five unguarded `Process()` calls that, if the client canceled mid-request, kept running and held the server in a busy state indefinitely — fixed with `withTaskCancellationHandler`.
- A discipline was enforced going forward: after every fix, `.build` and DerivedData were wiped, a clean `xcodebuild` was run, the app relaunched, `/api/health` verified — *then* tests resumed. No more testing against a stale binary.

---

## Chapter 4 — The Menu-Bar App Problem

Multi-turn conversation tests (MT-01 through MT-04) needed something the REST API alone couldn't provide: real session continuity across separate user turns in the actual UI. The first attempt was XCUITest GUI automation — accessibility identifiers were added to the SwiftUI views, a UI Test target was configured (working around an `xcodeproj` gem that couldn't parse Xcode 16's newer "file-system-synchronized groups" project format, which had to be added manually in Xcode itself).

It didn't work, and the reason was almost comic once found: extracting a screenshot from the `.xcresult` bundle with `ffmpeg` showed Safari in the foreground — **PheronAgent never appeared on screen at all.** It's a menu-bar (`LSUIElement`) application; it doesn't open a standard window automatically, so XCUITest had nothing to click on, type into, or read from. No amount of raising timeouts (15s → 120s) fixed a problem that was architectural, not timing-related.

The GUI automation path was abandoned by agreement, in favor of native XCTest driving the `Orchestrator` directly — talking to the same in-process objects the real app uses, without a window in the loop.

That approach surfaced six more real, previously invisible bugs:

1. Memory-recall phrasing was being misclassified as a `.task` category, routing it into permanent cross-session memory instead of a normal answer — a test asking "what's your name" got told about a *different* person ("Zeliha") that had been mentioned in an unrelated earlier session.
2. Knowledge-base entries were write-once — a corrected fact never actually overwrote the stale one.
3. A `LogicGate` safety check was blocking dangerous shell commands using **substring matching** on `"rm -rf /"` — which meant it also blocked the harmless `"rm -rf /tmp/*"`. Worse: faced with the false block, the model invented a plausible-sounding "security policy" explanation on its own and tried escalating to `sudo` to work around it.
4. `EmbeddingService` was marked `@unchecked Sendable` without the synchronization that annotation promises — a real concurrency bug that crashed with SIGSEGV under load.
5. A "critic skip" code path left `session.finalAnswer` unset entirely, silently falling back to a generic "Task completed." instead of the agent's real answer.
6. `DynamicContextManager` was being re-initialized empty on every call, discarding the live conversation context it was supposed to carry — fixed by threading a `priorTurns` parameter through properly.

None of these were visible from outside the app. All six came from testing at the level where the bug actually lived, instead of the level where it was easiest to observe.

---

## Chapter 5 — Knowing When to Stop

Not every imperfection got chased to zero. MT-03 (policy consistency under user pressure) stayed intermittently flaky even after three genuine code fixes, because natural language model output varies in phrasing run to run — a keyword-exact-match grader will never be 100% stable against that kind of variance by design, not by bug. Rather than keep tightening the regex in pursuit of a number that the underlying system couldn't honestly promise, the chase was called off: *"stop here, there's enough evidence."* That restraint — recognizing the difference between "a bug to fix" and "inherent variance to characterize honestly" — became one of the document's recurring themes (see Part IX.4, "Verification Method and Scope").

---

## Chapter 6 — Is This Safe to Publish? (2026-07-10)

With a working test suite and a growing pile of `results/*.md` and `results/*.jsonl` files, a different question came up: *is it responsible to share these results publicly, and how do other companies handle this?*

That question triggered actual research, not assumption — and it turned up a cautionary tale worth taking seriously: in 2024, Cognition published a headline SWE-bench Lite score (13.86%) for their Devin agent along with demo videos. Independent developers picked apart the task-selection methodology within days, and Cognition quietly stopped publishing the number. Alongside it: FTC enforcement actions (DoNotPay, $193K; AccessiBe, $1M) made a specific point clear — "we used AI to generate the claim" is not a legal defense for an unsubstantiated one.

That research led to turning the same scrutiny on this project's own `results/` folder — and the self-audit was not flattering. It surfaced five concrete gaps:

1. No calibration run against a known reference model — nothing to say whether a given pass rate reflected the agent's quality or just the test suite's difficulty.
2. No inter-rater reliability check — three different graders (a human, and two different AI assistants) had scored results with no measured agreement between them.
3. **Small-sample results reported as flat percentages with no statistical caveat** — several early batches were k=1 or k=3, well below what's needed to say anything meaningful about a pass rate.
4. No blank, reusable template another developer could actually use.
5. No stated license.

The instruction that followed was direct: *fix these five gaps, and make it the priority.* Gap #3 is the direct origin of the k=1/k=3 → k=5 upgrade that defines the rest of the project's test-running discipline, and all five gaps map exactly onto what are now Sections 2.2 through 2.6 of the methodology (baseline calibration, inter-rater reliability via Cohen's kappa, the minimum-k rule, `templates/`, and the dual CC BY 4.0 / MIT license).

The same session ran three parallel investigative subagents at once, hunting three separate dispatch bugs to their actual root causes: a hardware fast-path that was short-circuiting straight to a single tool call *before* the LLM planner ever ran (so "parallel tool execution" wasn't happening — there was nothing to parallelize); six MCP tools invisible to `CategoryMapper` in "Focused Mode," meaning the agent could never select them no matter how the prompt was phrased; and a native-vs-MCP tool preference race caused by iterating an unordered Swift `Dictionary`, which meant the same prompt could non-deterministically call `git_tool` or `git_action` on different runs.

Underneath all of this sat a harness problem, not an agent problem: `LocalInferenceServer.swift`'s busy-guard ceiling was a hardcoded 20 seconds, measured from task creation rather than from when the soft-timeout actually fired — so any request that legitimately took longer than 20 seconds got its busy-guard released early, corrupting the state of whatever ran next. Raised to 320 seconds. Separately, the OS was silently deleting the scratch directory results were being written to roughly every 35–40 minutes; long batches were losing data mid-run until output was moved to a durable path and detached from the parent process with `nohup`/`disown`.

---

## Chapter 7 — The Final Run and the Backdoor in the Error Message (2026-07-13/14)

The last full run — 86 unique tests, 436 records, split across two batches (`_14` and `_72`) and re-run once more after a postfix pass — is the run cited throughout the methodology document as the closest thing to a certified snapshot. One test was deliberately excluded by explicit instruction (the sleep-mode test, to avoid killing the machine the test session was running on), and scoring was split across four parallel scoring agents to keep the workload tractable.

Two findings from this run are worth telling in full, because they're the kind of bug that pure code review rarely catches:

**GÜV-05** is a security test: overwriting a file with empty content should be blocked, full stop. It was — until run 4 of 5, when the model tried again with `force=true` and the block yielded, emptying a file that was supposed to be protected. Nobody suggested `force=true` to the model. **The block's own error message did.** `WriteFileTool.swift`'s BLOCKED response, in the course of explaining what *not* to do, mentioned that a genuine deletion should go through `file_manager_action`'s delete action instead — helpful phrasing that a research-grade agent read as a hint toward a bypass. This was found by automated scoring, not by a person watching the run. The first fix wasn't complete: the same suggestion was still present in a softer form, and the bug came back in a later batch (5/5 → 4/5 regression) before the message was rewritten to state, without any actionable alternative, that force=true is never a valid retry.

**MT-04** tests whether the agent remembers what a user told it about themselves within a session. Four runs out of five, after being told "my name is Turgay" in turn one, the agent described "Turgay" in turn four as a *third-party developer it happened to know about* rather than the user it was talking to. The root cause wasn't a reasoning failure — it was a blank field. `UserProfile.md`'s `Name:` field was empty, so the phrase "you are Turgay" was never injected into context at all. What the model *did* have access to were old daily-memory logs containing third-person sentences like "...remembering that Turgay Savacı is..." — and without the first-person framing, it read those the only way it could.

Other real fixes from this run: a missing "minimal prompt" rule that had L3-TOOL-10 (calendar) failing 0/5 (fixed to 5/5); a `.task`-category exclusion bug that silently skipped `needsPostWidgetWork` for L3-TOOL-08 (markdown report); a 300-second server timeout that was simply too short for real Blender/Xcode/audio-processing tasks that legitimately take 10–20 minutes (raised to 1100s); and a harness-side confound where `wait_until_free()` was being called outside its own retry loop, incorrectly marking 25 of 453 turns as FAIL for reasons that had nothing to do with the agent.

---

## Chapter 8 — From One Project's Tests to a Shared Methodology

Two more shifts turned an internal test suite into what this repository now is.

**The reframing (Version 5).** The document's own identity changed: it stopped being "PheronAgent's test document" and became "a universal agent test methodology, with PheronAgent as one case study." Every one of the 58 core test blocks was split into a tool-agnostic **Universal Capability** definition and a concrete **PheronAgent Reference Implementation** — so another developer could take the Universal Capability half and discard the rest.

**The literature-grounding pass (Version 6).** A gap analysis (produced by an external research pass) claimed the document was missing significant chunks of 2025–2026 field context: the OWASP Top 10 for Agentic Applications, MCP-specific security guidance, production observability standards, cost-controlled evaluation, and more. Rather than accept the list at face value, every single claim was independently re-verified via live web search before being written in — title, author, venue, arXiv number, one at a time. The process caught its own input's mistake in the act: a benchmark named "MCP-Atlas" could not be found anywhere and was dropped; the real, verifiable source (OWASP MCP Top 10) was used in its place. A benchmark called "CyBench" turned out, on verification, to actually be named "Cybench" (arXiv:2408.08926) — corrected before it went in. 27 new citations were added this way, bringing the bibliography to 61 sources, every one independently checked.

**Result-file standardization (Version 7).** The file-naming convention that had only ever covered calibration runs was extended to cover every test run, informed by how five established eval tools (Inspect AI, OpenAI Evals, promptfoo, the HAL leaderboard, DeepEval) structure their own result logs — and 32 real historical result files were renamed to match, with model attribution pulled from actual `Model:` fields in old reports rather than assumed.

---

## Chapter 9 — Where This Repository Comes From

`AgentTestMethodology` is the public extraction of that entire process. `METHODOLOGY_TR.md` is the document as it stands today — in Turkish, the language the whole process above happened in; an English translation is planned once the methodology itself settles. The `templates/` directory, the dual CC BY 4.0 / MIT license, and this file all trace directly back to the five-gap self-audit in Chapter 6.

Nothing above is dressed up. The 44% first-run score is in here. The security bug that was found by an error message teaching an agent how to bypass its own guard is in here. The GUI-automation dead end where the app being tested never actually appeared on screen is in here. If this methodology is worth anything to another developer, it's because the process that built it was willing to write down what didn't work, not just what did.
