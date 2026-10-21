# Evaluation results — October 20, 2026

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
