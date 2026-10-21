# Evaluation results — October 20, 2026

Latest revision: [business workflows — October 21, 2026](#business-workflows--october-21-2026). The October 20 findings below retain their original content identities.

The original and revised skills each passed all 10 development cases, both held-out cases, and all seven activation checks in this local sample. The three representative no-skill cases also passed. These results establish no observed regression on the covered contracts; they do **not** demonstrate higher decision accuracy or statistical reliability.

## Method

- Original: repository commit `0683ff5`, snapshotted before edits.
- Revised: the `SKILL.md` content identified by the hash below.
- Host: headless Linux, workloads launched through `agent-run` in the existing resource-controlled slice.
- Codex CLI: `0.162.1`; configured model `gpt-6.1-sol`, reasoning effort `xhigh`, unchanged across comparisons. JSON traces do not expose an independently verified provider model revision.
- Fresh temporary Git repository and ephemeral, read-only Codex session for each case. Respondents received the scenario, its input files, and the applicable skill; expectations and grading instructions were withheld.
- Apps, plugins, hooks, browser/computer use, delegation, web search, and the locally configured MCP server were disabled. Some discovery runs listed the host's empty MCP resource catalogs; no formal run used connected-data or web tools.
- Expectations were fixed before the skill edit. The two held-out cases were run after the skill body was frozen and did not lead to further skill changes.
- Grading: manual review of each expectation against the answer and trace, with independent arithmetic. This is not a blind external assessment or an automated keyword score. All expectations are critical; each reported pass satisfies every expectation for that case.

## Behavioral evidence

Every row passed with both the original and revised skill. Evidence below summarizes the observed calculations and decisions in both answers; wording differed.

| Case | Observed evidence |
| --- | --- |
| `cash-profit` | Both calculated a **$7,000 shortfall** and prioritized a dated funding/payment arrangement before Friday, with a cash forecast and no assumed credit facility. |
| `supplier-prepayment` | Both showed **$12,000 nominal savings**, **$108,000 prepayment**, and a **$63,000 cash gap before reserves**. Both declined the unfunded terms and proposed staged purchases or delivery-based net-30 payment, accounting for inventory risk. |
| `negative-contribution` | Both calculated **−$5 per order**, **−$13,000 current operating profit**, and **−$18,000 at doubled volume**. Both rejected scaling these economics and counted acquisition once. |
| `retention` | Both used **$20 monthly contribution**, **$40 expected lifetime contribution**, and **−$80 after $120 CAC**. Both prioritized repairing retention/economics; the revision explicitly stated there was no expected cohort payback. |
| `pre-revenue` | Both gave **four months of current runway**, distinguished interview interest from paid demand, and favored a bounded paid pilot over borrowing for the $200,000 factory. Neither invented financing terms or an affordable pilot budget. |
| `acquisition` | Both used **$420,000 total cash**, **$30,000 remaining**, a **$70,000 reserve gap**, and **8.4-year standalone payback**. Neither relied on speculative synergies or approved the unfunded deal; partnership returns remained unknown. |
| `profitable-growth` | Both recommended funding: **$6,000 acquisition**, **$3,000 monthly contribution**, **two-month payback**, **$30,000 first-year net contribution**, and **$194,000 cash after acquisition**. Both included a monitoring trigger instead of defaulting to cost cuts. |
| `conflicting-evidence` | Both identified the **$10,000 discrepancy**, ledger contribution **$36,000 / 40%** and residual **$16,000**, versus summary contribution **$46,000** and residual **$26,000**. Both cited files/metrics, separated cash and receivables, kept marketing conditional, and preserved files. The revision added explicit row references and described checking for blanks/duplicate records. |
| `investment-horizon` | Both preferred B over the supplied three-year horizon, included resale once, and respected the reserve. Original rounded NPVs to **$14,606 / $19,579**; revised gave **$14,605.56 / $19,579.26**, within the $2 tolerances. Both discussed resale sensitivity. |
| `narrow-answer` | Both returned **$5,000 contribution / 40% margin** in fewer than 30 words, without intake or a full review. |
| `utilization-holdout` | Both chose outsourcing: **$4,800 monthly** versus **$6,400 internal**, with **1,000 units/month** recurring-cost indifference. Both recognized that setup capital still needs recovery and has no payback at 600 units. |
| `cash-timing-holdout` | Both identified a **$6,000 Tuesday gap** despite **$14,000 Friday closing cash** and required cleared funds or an agreed deferral before Tuesday. Neither assumed borrowing or took external action. |

The no-skill subset (`cash-profit`, `profitable-growth`, `conflicting-evidence`) satisfied the same expectations. The revised source references were more specific in the spreadsheet case, but that qualitative observation does not establish a general improvement over either baseline.

## Activation evidence

| Case | Expected Rockefeller load | Original | Revised |
| --- | --- | --- | --- |
| `cash-discovery` | Yes | Loaded | Loaded |
| `supplier-discovery` | Yes | Loaded | Loaded |
| `growth-discovery` | Yes | Loaded | Loaded |
| `biography` | No | Not loaded | Not loaded |
| `portfolio` | No | Not loaded | Not loaded |
| `accounting-code` | No | Not loaded | Not loaded |
| `copywriting` | No | Not loaded | Not loaded |

For positive cases, completed trace events show `cat .agents/skills/rockefeller/SKILL.md` returning the skill body. Negative cases completed without reading Rockefeller. The copywriting case selected the existing copy-editing skill instead. This is actual local discovery evidence, not an agent's prediction of which skill it would use. User/system skills remained discoverable; plugin skills were disabled. Results may change with another host, catalog, model, or prompt.

The description was retained because this sample found neither a miss nor a false positive. No business calculator, normalized input schema, or forecast template was added: the cases showed no recurring arithmetic failure or preparation problem requiring one. Synthetic CSV fixtures demonstrate file-based input without imposing a universal accounting format.

## Infrastructure and structural checks

- **41 formal runs completed:** 12 behavioral + 7 activation for each version, plus 3 no-skill runs. All supplied CSV copies retained their original hashes. Traces contained completed turns and nonempty final answers.
- Unrestricted preflight runs were excluded and stopped after a discovery run attempted connected-app searches. Isolation flags were then added and all formal baselines rerun.
- An initial revised batch had **10 configuration errors before model startup**, caused by quoting a dotted MCP override key. The runner was fixed and the full revised batch rerun successfully. These errors are excluded from decision scores and retained in local diagnostics.
- Eight runner rejection checks passed: source-tree output, unknown case, wrong split, mixed splits, mismatched variant, invalid activation baseline, nonpositive timeout, and existing-output overwrite. None launched a model run.
- Skill frontmatter validation, runner syntax, JSONL parsing, local Markdown links, shell-example syntax, fixture integrity, and Git whitespace checks passed.

Raw prompts, answers, traces, manifests, and diagnostics were retained outside the checkout during this run. They are local evaluation artifacts, not part of the skill package. Use [the protocol](protocol.md) and [runner](run.py) to reproduce the comparison; do not treat this dated report as proof that later edits pass.

## Content identities

SHA-256 values for the evaluated skill bodies and frozen case sets:

| Artifact | SHA-256 |
| --- | --- |
| Original `SKILL.md` | `70bdc2ca9f5fd5461ef16def7a6e8f71bbc3434868c7a4f11ecd88c90d1cf8e5` |
| Revised `SKILL.md` | `89a00dd82710c148b8fee9c26ab58a533650a0f7ea5a028f0dc0f4575ee3ef80` |
| `cases.jsonl` | `fcdd9c9b0a8a80211fb681b9300e8effcfecfa138b15b0a65fb85ab1b9dbe69b` |
| `activation.jsonl` | `e5f2a16b05187b4e854d09ebf4d6ac8546a0b5c518f3ec7a0c2abed63948544a` |

## Portability checks — October 21, 2026

The core skill above is unchanged. Its frontmatter uses the standard `name` and `description` fields; the instructions require no named vendor tools, models, or CLIs. The README now documents the open format, multi-agent installation, native invocation, and manual use. The shared evaluation protocol also explains how to run the same cases with other hosts. The bundled runner remains an optional Codex adapter.

Using `skills` CLI **1.7.0**, project-scoped copy installations from both the local checkout and `AyushRajSinghParihar/rockefeller` on GitHub accepted all four requested targets: **Claude Code, Codex, Cursor, and GitHub Copilot**. Each install wrote `.claude/skills/rockefeller/SKILL.md` and the shared `.agents/skills/rockefeller/SKILL.md`; all copies matched the revised core SHA-256 above. Cursor and Copilot share the latter project path in this installer. These were isolated temporary project installations, not changes to personal skill directories.

This verifies installer acceptance and file integrity, not runtime discovery or decision quality in all four hosts. Claude Code **2.1.236** is present but its authentication status reported `loggedIn: false`; no Claude model run was attempted. The October 20 financial and activation scores remain Codex-only evidence. Other hosts can use the same cases and rubric, with host-specific discovery and tool isolation.

## Business workflows — October 21, 2026

The final revision passed **21 behavioral cases and 11 activation checks**. The baseline at `f7489ee` passed **20/21 behavioral cases and 11/11 activation checks**. A targeted no-skill subset passed **2/3**. The observed difference is an explicit operating assumption to monitor in a justified capital approval; all compared financial calculations and decisions passed. These are single-sample, manually graded outcomes, not evidence of general accuracy uplift or statistical reliability.

### Scope and method

- Baseline: the complete runtime package from `f7489ee`, snapshotted outside the checkout before editing. Final: the core and four references identified below; optional UI metadata unchanged.
- The nine new scenarios and expectations were frozen before core edits. Four additional activation prompts were frozen before either activation comparison. Seven new development scenarios and two held-outs join the existing 12 financial cases. The held-outs were excluded from development and did not cause further edits.
- Codex CLI **0.162.1**, configured **gpt-6.1-sol**, reasoning **xhigh**, matched within the comparison. No independently exposed provider model revision. Workloads used `agent-run`; concurrency was one or two cases per batch, so elapsed times are not a controlled benchmark.
- Fresh temporary Git workspaces, no answer keys, and identical prompts/settings within variants. Real sequential user turns used native `exec resume` and the same recorded thread ID. Record review used a second fresh, ephemeral session with a different ID and the first session's actual saved files; the original forecast was not repeated in its user prompt.
- Default sandbox read-only. Only the record case authorized workspace writes, limited to `business-context.md` and `decision.md`; per-turn snapshots and file-change checks preserved originals and installed resources. Both variants wrote only those files. The final record retained the complete original decision text and appended actuals.
- Manual grading inspected every expectation, final answers, per-turn artifacts and traces, with independent arithmetic. An independent reviewer also checked the disputed capital-monitoring criterion. Equivalent unit thresholds were accepted: 869.57 continuous units and 870 whole units correctly distinguish the new-cost case from the 80% development example.
- All four references were actually read in relevant final traces. Narrow-answer traces stayed proportionate. Apps, plugins, hooks, web search, browser/computer use, delegation, and configured MCP servers were disabled. Some activation runs listed empty MCP resource catalogs; no live financial data or web calls were used.

### Per-case evidence

Every case passed both variants except the baseline `premise-fund` monitoring expectation. The final variant passed every expectation.

| Case | Evidence in the compared answers/artifacts |
| --- | --- |
| `cash-profit` | $7,000 Friday gap; dated payment/collection plan; no assumed credit. |
| `supplier-prepayment` | $12,000 nominal savings, $108,000 prepayment, $63,000 gap before reserves; flexible counteroffer. |
| `negative-contribution` | -$5/order; -$13,000 current and -$18,000 at doubled volume; acquisition counted once. |
| `retention` | $20 monthly contribution; $40 expected lifetime contribution versus $120 CAC; -$80/customer and no expected payback. |
| `pre-revenue` | Four months of runway; interviews remain interest; bounded paid pilot before factory/debt. |
| `acquisition` | $420,000 total cash leaves $30,000; $70,000 reserve gap; 8.4-year standalone payback; no synergy reliance. |
| `profitable-growth` | Fund $6,000 acquisition; $3,000 monthly contribution; two-month payback; $30,000 annual net cash; reserve preserved and monitoring trigger. |
| `conflicting-evidence` | $10,000 discrepancy; ledger $36,000/40% contribution and $16,000 remainder versus summary $46,000/$26,000; sources traced, cash/receivables separated, originals preserved. |
| `investment-horizon` | A NPV $14,605.56 versus B $19,579.26 at 10%; resale counted once; both affordable, B preferred with resale sensitivity. |
| `narrow-answer` | $5,000 contribution and 40% margin, under 30 words with no unrelated intake. |
| `utilization-holdout` | $4,800 outsourcing versus $6,400 internal; 1,000-unit operating indifference; no setup payback at current volume. |
| `cash-timing-holdout` | $6,000 Tuesday gap despite $14,000 Friday arithmetic balance; arrange cleared funds or deferral before Tuesday. |
| `discovery-dialogue` | Three actual turns; paid-offer question, clinic-owner workaround/five-hour burden, then bounded priced manual pilot before hiring; five-month runway; proposed prices remain hypotheses. |
| `premise-factory` | Order release is the constraint; expansion leaves $70,000, breaching reserve by $30,000; price and pilot a smaller workflow intervention. |
| `premise-fund` | Buy the machine; $30,000 contribution, $18,000 net benefit, $68,000 remaining cash. Final revision explicitly monitors installation/throughput against delivery deadlines; original omits the monitoring premise. |
| `pricing-volume` | $40 to $50 unit contribution; 800 units/80% volume threshold; $42,500 at 850 and $37,500 at 750; bounded test without invented demand. |
| `capacity-mix` | 60 B and 20 A use 100 hours for $2,600; hourly contribution ranking respects demand caps. |
| `commitment-threshold` | Indifference at 1,333 1/3 used units, commitment cheaper from 1,334; $12,000 versus $16,000 at 1,000 and $19,200 versus $16,000 at 1,600; no invented probabilities. |
| `decision-record` | First session creates real files forecasting +$1,000 and $41,000 closing cash. A different fresh session reads them, preserves the dated forecast and adds -$1,600 actual impact, $38,400 closing cash, -$2,600 variance and -$600 recurring cash; scaling held. |
| `pricing-cost-holdout` | $46 proposed contribution; continuous threshold 869.57 units, rounded to 870 (87% whole-unit volume); 900 units produce $41,400, up $1,400; scenario remains hypothetical. |
| `two-resources-holdout` | 3 A and 2 B maximize contribution at $230; labor 8, machine 7; alternative 2 A/3 B earns $220 within both limits. |

The no-skill subset was `discovery-dialogue`, `premise-fund`, and `capacity-mix`; only `premise-fund` failed the monitoring criterion. Its arithmetic and approval were correct. The original and preliminary revised capital answers also provided a 1,600-unit break-even calculation but no identifiable delivery/contract premise to watch. This criterion has an interpretive boundary: a pure volume sensitivity was not credited as an operating monitoring condition. The final answer explicitly names timely installation and throughput, without reopening the supplied facts.

### Activation evidence

| Expected load | Cases | Baseline | Final |
| --- | --- | --- | --- |
| Yes | `cash-discovery`, `supplier-discovery`, `growth-discovery`, `startup-discovery`, `pricing-discovery`, `capacity-discovery` | 6/6 loaded | 6/6 loaded |
| No | `biography`, `portfolio`, `accounting-code`, `copywriting`, `hobby-project` | 5/5 not loaded | 5/5 not loaded |

Positive traces show completed reads of the installed Rockefeller body. Negative cases completed without a Rockefeller read. Competing user/system skills remained discoverable. The description was retained because this sample found no miss or false positive.

### Additional checks and run accounting

- **67 formal case runs:** 21 behavioral + 11 activation per variant, plus 3 no-skill cases. Multi-turn cases account for 75 actual CLI turns, rather than 67 simulated transcripts. All completed formal runs preserved immutable workspace files and produced complete traces/answers.
- A separate read-only draft smoke passed: the agent explicitly said the record was **not saved**, returned Markdown with a $200 forecast benefit/$5,200 closing cash, and created no workspace output. Its prompt and trace are retained locally; this is an additional integration check, not a matched baseline case.
- An independent forward check scheduled 15 standard/35 express repair jobs within 80 technician hours for $3,450 contribution, respected an existing ten-standard-job commitment, and rejected a machine that relieved no constraint and breached reserves.
- **Preliminary results retained:** nine completed candidate cases included the same missing-monitoring failure. Two in-progress candidate cases (`decision-record`, `retention`) were intentionally stopped when the rule was clarified. They are excluded from final scores, not passed or silently retried. The entire final 21-case behavioral suite and 11 activation cases were then run on the frozen final package.
- The first seven baseline scenarios used an earlier adapter iteration before runner-hash metadata and additional malformed-input guards were added. Their commands, prompts, skill hashes, per-turn IDs, answers and actual artifacts were captured; the prompt, sandbox and resumption behavior were unchanged. Later baseline and all final cases use the final adapter. The preliminary monitoring failure remains recorded in this report.
- Three standard-library test methods covered 15 CLI scenarios: invalid paths/arguments, overwrite preservation, held-out selection, malformed conversations and unsafe output paths. Python/JSONL/frontmatter, local Markdown links/fences, bash-example syntax, source fixture integrity, and Git whitespace checks passed.
- The original SVG parsed without scripts or remote dependencies, rendered headlessly at **1000px and 375px**, and was visually inspected for legibility and clipping. Text contrast against its background was **12.79:1**. The README worked example was independently recomputed; it is public explanatory material, not independent test evidence.
- Project copy installation of the final package through skills CLI **1.7.0** accepted Claude Code, Codex, Cursor and GitHub Copilot. Both `.claude/skills/rockefeller/` and the shared `.agents/skills/rockefeller/` contained the matching core, UI metadata and all references. This is installation/file-integrity evidence. Claude remains unauthenticated, so Claude runtime discovery and decision quality were not tested; runtime evidence here remains Codex-only.

Raw artifacts are outside the checkout under the local evaluation root. `comparison/original/` owns the baseline; `final/revised/` owns the final revision; `final/none/` owns the no-skill subset; `comparison/revised/` retains the preliminary candidate. Per-expectation decisions and evidence locations are retained in `grades.json`. Follow [the protocol](protocol.md) to reproduce; those temporary local paths are not packaged evidence or a promise of permanent storage.

### Content identities for this revision

The package identity hashes the sorted JSON mapping of runtime-relative filenames to their individual SHA-256 values (core, optional UI metadata, and four references). Per-run manifests retain those individual hashes.

| Artifact | SHA-256 |
| --- | --- |
| Baseline `SKILL.md` | `89a00dd82710c148b8fee9c26ab58a533650a0f7ea5a028f0dc0f4575ee3ef80` |
| Final `SKILL.md` | `5eafc65dc7a948f59291cdc66e0c9b2dc97e57ead53c209e114540a9444aee0f` |
| Final runtime package | `39b2c884e64b2f7140cee3edd7bfd3ca0a925371419dbcae6387027d708e41a2` |
| `evals/cases.jsonl` | `fcdd9c9b0a8a80211fb681b9300e8effcfecfa138b15b0a65fb85ab1b9dbe69b` |
| `evals/scenarios.jsonl` | `b14f2ac615619bd5131280bb2684e5ffc64dbbda5b4ae0f162946389bf68a246` |
| `evals/activation.jsonl` | `1da23e8f80f1f05e0a162b696e418356ea975fc0c122bb51e69a055bef981bdf` |
| `evals/run.py` | `c9d42306b8cbafb83b981aedc7ab8162d39c95e3f389b2b56e24f4dcf43c03ac` |
| `docs/assets/rockefeller-banner.svg` | `945bd67b3e2d29d96be6860ae9d8249e33272ee683ff49bc6e433e30c75ae54a` |
