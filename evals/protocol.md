# Rockefeller evaluation protocol

These evaluations check decisions and evidence, not compliance with particular wording. They use synthetic businesses, fixed inputs, and no live accounts or counterparties.

## Contracts and cases

`cases.jsonl` owns the behavioral checks. Each case identifies the observable contract, the credible regression it detects, and independently calculated expectations. There was no existing behavioral coverage when these cases were added. Cases exercise the agent's answer boundary; no production exports, test-only flags, exact-heading checks, or keyword-based grading are needed.

`activation.jsonl` separately owns discovery checks. Explicitly invoking `$rockefeller` tests its instructions, not whether Codex chooses it automatically.

The `holdout` cases are excluded from development runs. Run them after the revision is frozen; if a holdout leads to a fix, retain it as a regression and use a new case for the next independent check.

## Run

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
```

Omit `agent-run` on machines without that local resource-control launcher. Results must live outside the source checkout and installed skill directories. The runner creates a fresh temporary Git repository for every case and copies only its prompt, permitted input files, and selected skill. It does not give the responding agent the expectations or evaluation protocol. Financial cases ask for analysis, not external execution or current legal/market claims.

Inspect each run's `run.json` skill hashes before grading a comparison. Freeze cases and expectations before running either version. Keep holdout outputs separate. Do not silently retry failed runs or omit them from the report. A transport failure is an infrastructure error, not a failed financial decision; report it and any rerun separately.

## Grade

For every expectation, record pass/fail and quote or reference the answer's evidence. Check numerical results with independent arithmetic, using the case's tolerances. Accept different justified recommendations where the case permits them. Do not award a pass merely because an answer includes the right heading, formula, or phrase.

All financial and scope expectations are critical. A case passes only when all its expectations pass. Review actionability and proportionality qualitatively; do not hide a serious failure behind an aggregate score. Compare the original and revised skill, using no-skill runs on a representative subset to estimate whether the skill adds value. A tie is a tie, not proof of improvement. Single runs establish neither statistical reliability nor a causal explanation for a difference.

Review the traces as well as final answers: source-file access, calculation commands, unwanted actions, and skill loading can change the interpretation. Reject runs that accessed answer keys or outside financial evidence. Record whether other installed skills were loaded; isolation of the temporary repository does not disable machine-wide skills.

## Activation

Activation prompts contain no explicit invocation or instruction to load Rockefeller. Install exactly one variant inside the temporary repository's `.agents/skills/rockefeller/`. A positive case passes only when the trace shows the agent actually reading that `SKILL.md`; a statement that it would use the skill is insufficient. Negative cases require a completed answer and no Rockefeller load. Diagnose ambiguous commands manually; the runner does not infer selection from text matching.

Record the host's available competing skills and model when interpreting discovery. Do not claim activation across all hosts or catalogs from this local sample. Change the description only when observed misses or false positives justify it, then repeat affected activation cases and check for regressions.

## Report

Keep raw runs outside the skill package. Check in a compact `results.md` with the date, versions/settings, case identifiers, per-case evidence, infrastructure failures, critical misses, and limits. Run the skill validator, check local links and fixture integrity, and run `git diff --check`. Update the root README after the implementation and evaluations describe the same final revision.
