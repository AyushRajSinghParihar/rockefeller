# Rockefeller

A business strategy skill for Codex focused on operating economics, cash resilience, and disciplined growth.

Rockefeller uses a modern adaptation of John D. Rockefeller's emphasis on exact accounting, operating efficiency, patient capital, and compounding advantages. It helps turn business data into a priority, a defensible decision, and an execution plan.

## When to use it

- Revenue is growing, but cash or contribution profit is falling.
- You need to identify the bottleneck before cutting costs or scaling.
- You need to compare pricing, retention, acquisition payback, and capacity before funding growth.
- A supplier offers a discount in exchange for a larger commitment.
- You are comparing outsourcing with building or buying a capability.
- You need to assess borrowing, reinvestment, an acquisition, or a partnership.

The skill is designed for operating business decisions. Historical research about Rockefeller and personal portfolio advice are outside its intended scope.

## Install in Codex

Run these commands on the machine where Codex runs. In a remote development setup, that means the development server.

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AyushRajSinghParihar/rockefeller.git "$HOME/.agents/skills/rockefeller"
```

For a project-specific installation, put the skill folder at `.agents/skills/rockefeller/` inside that project instead. Keep `SKILL.md` at the top of the `rockefeller` folder.

In Codex, select it through `/skills` or mention `$rockefeller` in a prompt. Codex can also select it when a request matches its description. If it does not appear after installation, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and installation details.

Rockefeller's business analysis workflow is instruction-only and requires no additional packages, API keys, or MCP connections of its own. Live research and analysis of supplied files depend on the tools available to your agent; the skill does not supply accounting data or connect to your accounts. The optional development evaluation runner has separate requirements described below.

## Try it

### Review the business

```text
Use $rockefeller to review my ecommerce business and identify the next priority.
All figures are USD for September 2026:
- Net revenue: $80,000 across 2,000 orders.
- Variable costs: $32,000 product, $10,000 fulfillment, $2,400 payment fees,
  $3,600 returns handling, and $12,000 paid acquisition. No overlap between categories.
- Fixed operating costs: $18,000.
- Unrestricted cash: $35,000. A $25,000 inventory payment is due in two weeks.
- No debt. I want to grow without taking outside equity.
Give a provisional diagnosis, flag the most important missing input,
and recommend the immediate next step.
```

### Evaluate a supplier offer

```text
Use $rockefeller to evaluate a supplier offer. We buy 1,000 units a month
at $20 each, payable after 30 days. The supplier offers $18 per unit
if we prepay for 6,000 units. We have $45,000 of unrestricted cash
and $12,000 of monthly fixed cash costs. Demand fluctuates by 30%.
Compare the savings, cash commitment, and inventory exposure.
Suggest a counteroffer. Keep the answer focused on this decision.
```

### Compare an acquisition with organic growth

```text
Use $rockefeller to compare acquiring a small competitor with growing organically.
Use the attached financial statements and proposed deal terms.
Separate purchase price from total cash required, evaluate the deal without
synergies, and show what changes under a downside case.
Identify missing evidence before recommending a commitment.
```

### Decide whether to fund growth

```text
Use $rockefeller to review a proposed subscription growth investment.
We can acquire 100 customers for $60 each upfront. Each signs a 12-month
contract paying $50 monthly, with $20 monthly variable service costs.
Assume no churn or missed payments during the term. Existing capacity covers
the cohort, with no extra fixed costs or capex. Cash is $200,000 and the
required reserve is $100,000; existing obligations are funded. All USD.
Compare incremental contribution, cash payback, and liquidity.
Recommend whether to fund it and give a monitoring trigger.
```

## What to provide

Start with the decision, business model, geography, period, and currency. Add the numbers relevant to that decision:

| Decision | Helpful inputs |
| --- | --- |
| Operating review | Revenue, units or customers, variable and fixed costs, retention, capacity |
| Growth investment | Pricing, acquisition spending, cohort retention, contribution per active customer, collection timing, available capacity |
| Cash resilience | Unrestricted cash, collections, payment dates, inventory, taxes, debt service, capital spending |
| Supplier negotiation | Delivered cost, purchase volumes, payment terms, service levels, alternatives, commitments |
| Build, buy, or partner | Setup costs, utilization, operating costs, capabilities, working capital, switching costs |
| Acquisition or financing | Financial statements, valuation or loan terms, liabilities, integration costs, downside assumptions |

Use estimates or ranges when exact figures are unavailable, and label them. A narrow decision does not require a complete business dossier. The skill should use what you have, explain uncertainty, and identify the missing information that could change the recommendation.

CSV exports, spreadsheets, and financial statements can be supplied in their existing format. Include the reporting period, currency, and accounting basis. If two files disagree, provide both rather than silently merging them. The skill should preserve the originals, trace important figures to their file and metric or row, and keep decisions conditional where differences remain unresolved. See the synthetic [ledger](evals/fixtures/september-ledger.csv) and [management summary](evals/fixtures/management-summary.csv) for a small worked input pair.

## What you should get

A focused answer should identify the constraint, show relevant arithmetic, recommend an intervention, and explain the cash required, principal downside, and conditions that would change the decision.

A full review also covers market evidence, operating leverage, build/buy/partner options, and the capital plan. It closes with an execution ledger containing actions, proposed owners, deadlines, measurable targets, cash commitments, and stop or review triggers. Questions about one decision should receive a proportionate answer.

Growth decisions should use retained contribution and cash payback rather than revenue alone. Material investment comparisons should use a common horizon, incremental cash flows, and supported residual values; discounted cash flows apply when timing changes the choice. The skill should explain uncertain inputs instead of inventing a universal hurdle rate or payback benchmark.

Current market, financing, and legal claims need current sources and the relevant jurisdiction. When those cannot be verified, recommendations should remain conditional. The skill supports analysis and drafting; actions such as contacting a supplier or moving funds require authorization for that action.

## Repository

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent instructions, financial definitions, decision playbook, and output guidance |
| [agents/openai.yaml](agents/openai.yaml) | Codex display name and short description |
| [evals/cases.jsonl](evals/cases.jsonl) | Ten development cases and two held-out decisions with financial expectations |
| [evals/activation.jsonl](evals/activation.jsonl) | Three positive and four negative discovery cases |
| [evals/fixtures/](evals/fixtures/) | Synthetic financial exports for evidence reconciliation |
| [evals/run.py](evals/run.py) | Optional runner for isolated Codex evaluation sessions |
| [evals/protocol.md](evals/protocol.md) | Baselines, isolation, grading, and reproduction instructions |
| [evals/results.md](evals/results.md) | Dated results, evidence, and limitations |
| [README.md](README.md) | Installation, examples, and contributor guidance |

## Verification and development

On October 20, 2026, the original and revised skill each passed **12 behavioral cases and seven activation checks**. Three representative no-skill cases also passed. These 41 formal runs found no regression on the covered checks; they do not establish a general accuracy improvement or statistical reliability. The revised spreadsheet answer provided more specific source references. See [the results](evals/results.md) for evidence and excluded infrastructure/preflight runs.

Evaluation requires **Python 3.11+, Git, and an authenticated Codex CLI** supporting the runner's isolation flags; CLI 0.162.1 was verified. Run evaluations on the machine running Codex, using `agent-run` on the THINKBOOK where available. Results belong outside the checkout. No extra Python packages are required.

Follow [the protocol](evals/protocol.md) to snapshot the baseline before editing, run matched comparisons, and grade every expectation using answer/trace evidence. The runner captures outputs and provenance; it does not automatically grade strategic judgment. Activation checks use natural prompts and actual skill-loading traces, separately from explicit invocation. Connector and browsing access are disabled for the synthetic cases; other user/system skills can remain discoverable.

Keep the entrypoint self-contained. Add a financial helper or template when repeated use establishes a stable need, and move expanded specialist material into references when selective loading saves context. The current cases did not justify a mandatory input schema, forecast template, or business calculator. [OpenAI's authoring advice](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) similarly emphasizes concise, task-specific instructions.

Authoring references checked on October 20, 2026:

- [OpenAI: testing skills with evaluations](https://developers.openai.com/blog/eval-skills) — distinguish activation, outcomes, process, and efficiency.
- [Agent Skills: evaluating skills](https://agentskills.io/skill-creation/evaluating-skills) — compare behavior against concrete expectations and a baseline.
- [Agent Skills: optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) — evaluate when a skill is selected.
- [Agent Skills specification](https://agentskills.io/specification) — required metadata, optional resources, and progressive disclosure.
- [Anthropic: skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — concise guidance, appropriate degrees of freedom, and evaluation-driven iteration.
