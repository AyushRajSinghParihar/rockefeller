# Rockefeller evaluation protocol

These evaluations check decisions and evidence, not compliance with particular wording. They use synthetic businesses, fixed inputs, and no live accounts or counterparties. The case data and grading method are agent agnostic; `run.py` is an optional Codex adapter, not a requirement for using or evaluating the skill.

## Contracts and cases

`cases.jsonl` owns the behavioral checks. Each case identifies the observable contract, the credible regression it detects, and independently calculated expectations. There was no existing behavioral coverage when these cases were added. Cases exercise the agent's answer boundary; no production exports, test-only flags, exact-heading checks, or keyword-based grading are needed.

`activation.jsonl` separately owns discovery checks. Explicitly invoking the skill tests its instructions, not whether the host chooses it automatically.

`scenarios.jsonl` adds business discovery, premise checks, pricing, constrained product mix, decision thresholds, and a saved-record lifecycle. Each row has either a `prompt` or ordered `turns`. A turn contains a `prompt` and optionally `new_session: true` to start without conversation memory. Only those prompts and permitted fixtures reach the respondent; future turns and expectations must remain unavailable until their turn. A conversation is an actual sequence of user messages and agent responses, not a single prompt asking the model to simulate both sides.

An optional `writable_outputs` list authorizes named Markdown outputs in the temporary workspace. All other files, including installed skill resources and supplied fixtures, stay immutable. The record-lifecycle case must start from missing output files, capture the first session's real saved forecast, then open those files in a fresh session with new actuals. A supplied ideal record or a claim that a file was saved does not establish persistence.

The `holdout` cases are excluded from development runs. Run them after the revision is frozen; if a holdout leads to a fix, retain it as a regression and use a new case for the next independent check.

## Run with any agent

1. Snapshot the original skill before editing and freeze the cases and expectations. Choose development or held-out cases from `cases.jsonl`; use `activation.jsonl` separately for discovery.
2. Start a fresh workspace and session per case. Install the chosen variant using the host's native skill directory, or supply `SKILL.md` directly for an instruction-quality check. Provide only the case's `prompt` and named files from `fixtures/`; withhold its expectations, regression description, and this grading protocol.
3. For behavioral comparisons, explicitly load the skill using that host's syntax. For no-skill baselines, omit it. Match model, tools, and settings within each host. Disable live connectors, browsing, hooks, and external actions for these synthetic cases using that host's controls, and preserve input files.
4. Capture the prompt, skill and input hashes, host/model/version/settings, final answer, available trace evidence, and failures. Apply the grading rules below. Do not combine results from different hosts into a single original-versus-revised comparison.

For activation checks, install the skill natively and use the exact natural prompt without naming or forcing the skill. Directly attaching `SKILL.md` cannot test automatic selection. Confirm loading through the host's observable trace; if that evidence is unavailable, report activation as unverified.

## Optional Codex runner

Requirements for evaluation only: Python 3.11+, Git, and an authenticated Codex CLI supporting the runner's isolation flags (verified with 0.162.1). Skill usage itself does not require this runner. Commands belong on the machine running Codex (THINKBOOK in the remote workstation setup). The runner disables apps, plugins, hooks, browser/computer use, delegation, web search, and locally configured MCP servers for these synthetic cases. It leaves the user's configuration files untouched. Inspect traces for any remaining host-provided tools before accepting a run.

Before editing, snapshot the original skill outside the checkout. Include `SKILL.md`, `agents/`, and any supporting resources. Use the same Codex model, configuration, and tools for each comparison. The runner records the CLI version, configured model and reasoning effort, prompts, skill-content hashes, input hashes, traces, answers, and elapsed time. Record a provider-resolved model revision when available; do not infer it from a configured alias.

```bash
agent-run python3 evals/run.py --skill /tmp/rockefeller-original --variant original --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill . --variant revised --output /tmp/rockefeller-results
agent-run python3 evals/run.py --variant none --case cash-profit --case profitable-growth --case conflicting-evidence --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill /tmp/rockefeller-original --variant original --holdout --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill . --variant revised --holdout --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill /tmp/rockefeller-original --variant original --activation --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill . --variant revised --activation --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill /tmp/rockefeller-original --variant original --suite scenarios --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill . --variant revised --suite scenarios --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill /tmp/rockefeller-original --variant original --suite scenarios --holdout --output /tmp/rockefeller-results
agent-run python3 evals/run.py --skill . --variant revised --suite scenarios --holdout --output /tmp/rockefeller-results
agent-run python3 evals/run.py --variant none --suite scenarios --case discovery-dialogue --case premise-fund --case capacity-mix --output /tmp/rockefeller-results
```

Omit `agent-run` on machines without that local resource-control launcher. Results must live outside the source checkout and installed skill directories. The runner creates a fresh temporary Git repository for every case and copies only its prompt, permitted input files, and selected skill. It does not give the responding agent the expectations or evaluation protocol. Financial cases ask for analysis, not external execution or current legal/market claims.

All cases default to a read-only sandbox. Only cases declaring `writable_outputs` receive a workspace-write sandbox, with workspace changes checked against that list after every turn. This list is an evaluation check, not a separate operating-system filesystem boundary. Do not put real accounts or sensitive files in these workspaces. The runner snapshots actual output documents under each turn's `artifacts/` folder, including the original before a subsequent update.

For conversations, the Codex adapter uses the CLI's native `exec resume` with the exact recorded thread ID. Such sessions must be persisted in Codex's normal session store so they can resume; single-turn cases and cases with only fresh-session turns remain ephemeral. Each turn has its own prompt, trace, answer, command, session ID, and file-change evidence. Check matching IDs on resumed turns and different IDs when a fresh session is required. Never use `--last`, which could select an unrelated conversation. Core skill usage has no session-store or CLI dependency.

The timeout applies to each actual CLI turn. A write-unavailable smoke can be run in any host's read-only session: request a compact decision record for a chosen one-month pilot with $100 upfront cost, $300 forecast cash savings, $5,000 opening cash, a $4,000 reserve, funded existing obligations and an otherwise flat cash baseline. Ask to save if supported, otherwise return a Markdown draft and state whether it was saved. Verify a clearly unsaved draft, $200 forecast benefit/$5,200 forecast closing cash, and no workspace output. Keep this separate from matched case scores unless it was frozen and run for each variant.

Inspect each run's `run.json` skill hashes before grading a comparison. Freeze cases and expectations before running either version. Keep holdout outputs separate. Do not silently retry failed runs or omit them from the report. A transport failure is an infrastructure error, not a failed financial decision; report it and any rerun separately.

## Grade

For every expectation, record pass/fail and quote or reference the answer's evidence. Check numerical results with independent arithmetic, using the case's tolerances. Accept different justified recommendations where the case permits them. Do not award a pass merely because an answer includes the right heading, formula, or phrase.

For saved records, inspect the actual per-turn artifact snapshots and completed file-read/write traces. Confirm the fresh session reads the first session's real output, that the original forecast remains distinguishable from later actuals, and that no unrelated files changed. For guided discovery, check each response against only the evidence available at that turn; do not credit an early guess as knowledge of a later answer.

All financial and scope expectations are critical. A case passes only when all its expectations pass. Review actionability and proportionality qualitatively; do not hide a serious failure behind an aggregate score. Compare the original and revised skill, using no-skill runs on a representative subset to estimate whether the skill adds value. A tie is a tie, not proof of improvement. Single runs establish neither statistical reliability nor a causal explanation for a difference.

Review the traces as well as final answers: source-file access, calculation commands, unwanted actions, and skill loading can change the interpretation. Reject runs that accessed answer keys or outside financial evidence. Record whether other installed skills were loaded; isolation of the temporary repository does not disable machine-wide skills.

## Activation

Activation prompts contain no explicit invocation or instruction to load Rockefeller. Install exactly one variant in the host's native project skill directory: for example, `.claude/skills/rockefeller/` for Claude Code or `.agents/skills/rockefeller/` for Codex. A positive case passes only when the trace shows the agent actually reading that `SKILL.md`; a statement that it would use the skill is insufficient. Negative cases require a completed answer and no Rockefeller load. Diagnose ambiguous commands manually; the runner does not infer selection from text matching.

Record the host's available competing skills and model when interpreting discovery. Do not claim activation across all hosts or catalogs from this local sample. Change the description only when observed misses or false positives justify it, then repeat affected activation cases and check for regressions.

## Report

Keep raw runs outside the skill package. Check in a compact `results.md` with the date, versions/settings, case identifiers, per-case evidence, infrastructure failures, critical misses, and limits. Run the skill validator, check local links and fixture integrity, and run `git diff --check`. Update the root README after the implementation and evaluations describe the same final revision.
