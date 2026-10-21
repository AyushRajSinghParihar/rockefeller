# Rockefeller

An agent-agnostic business strategy skill focused on operating economics, cash resilience, and disciplined growth. Built on the open [Agent Skills format](https://agentskills.io/specification), it can be used by Claude Code, Codex, and other agents that load `SKILL.md` instructions.

Rockefeller uses a modern adaptation of John D. Rockefeller's emphasis on exact accounting, operating efficiency, patient capital, and compounding advantages. It helps turn business data into a priority, a defensible decision, and an execution plan.

## When to use it

- Revenue is growing, but cash or contribution profit is falling.
- You need to identify the bottleneck before cutting costs or scaling.
- You need to compare pricing, retention, acquisition payback, and capacity before funding growth.
- A supplier offers a discount in exchange for a larger commitment.
- You are comparing outsourcing with building or buying a capability.
- You need to assess borrowing, reinvestment, an acquisition, or a partnership.

The skill is designed for operating business decisions. Historical research about Rockefeller and personal portfolio advice are outside its intended scope.

## Install

Run installation commands where your agent runs. In a remote development setup, use the development server; for an agent running locally on your Mac, use the Mac.

### Choose your agent with the skills CLI

With Node.js available, run this in the project where you want the skill:

```bash
npx skills add AyushRajSinghParihar/rockefeller --skill rockefeller
```

The installer lets you choose supported agents. To target one or several directly:

```bash
# Claude Code
npx skills add AyushRajSinghParihar/rockefeller --skill rockefeller --agent claude-code

# Codex, Cursor, and GitHub Copilot
npx skills add AyushRajSinghParihar/rockefeller --skill rockefeller --agent codex cursor github-copilot
```

Add `--global` for a user-level installation. See the [skills CLI documentation](https://github.com/vercel-labs/skills) for supported agents and options. Node.js is needed for this installer, not for the skill itself.

### Manual installation

Choose one installation method. No package manager is required to clone the skill directly.

**Claude Code — personal installation:**

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/AyushRajSinghParihar/rockefeller.git "$HOME/.claude/skills/rockefeller"
```

For a project installation, use `.claude/skills/rockefeller/` inside your project. Invoke it with `/rockefeller`, or describe a matching business task. See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

**Codex — personal installation:**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AyushRajSinghParihar/rockefeller.git "$HOME/.agents/skills/rockefeller"
```

For a project installation, use `.agents/skills/rockefeller/`. Invoke it with `$rockefeller` or select it through `/skills`. See [Codex's skill documentation](https://learn.chatgpt.com/docs/build-skills).

**Other agents and chat apps:** put the `rockefeller` folder in your agent's documented skill directory, keeping `SKILL.md` at its top level. Use that host's invocation syntax. If native skills are unavailable, attach or paste `SKILL.md` as instructions and ask the agent to follow it for your task; this does not add automatic discovery to that host.

The core skill uses standard `name` and `description` metadata and contains no vendor-specific tool calls, model requirements, or CLI commands. `agents/openai.yaml` is optional Codex UI metadata; other hosts do not need it. Installation and automatic selection depend on the host. The examples below use plain language; replace the opening with `/rockefeller` in Claude Code or `$rockefeller` in Codex when you want explicit invocation.

Rockefeller's business analysis workflow is instruction-only and requires no additional packages, API keys, or MCP connections of its own. Live research and analysis of supplied files depend on the tools available to your agent; the skill does not supply accounting data or connect to your accounts. The optional development evaluation runner has separate requirements described below.

## Try it

### Review the business

```text
Use the Rockefeller skill to review my ecommerce business and identify the next priority.
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
Use the Rockefeller skill to evaluate a supplier offer. We buy 1,000 units a month
at $20 each, payable after 30 days. The supplier offers $18 per unit
if we prepay for 6,000 units. We have $45,000 of unrestricted cash
and $12,000 of monthly fixed cash costs. Demand fluctuates by 30%.
Compare the savings, cash commitment, and inventory exposure.
Suggest a counteroffer. Keep the answer focused on this decision.
```

### Compare an acquisition with organic growth

```text
Use the Rockefeller skill to compare acquiring a small competitor with growing organically.
Use the attached financial statements and proposed deal terms.
Separate purchase price from total cash required, evaluate the deal without
synergies, and show what changes under a downside case.
Identify missing evidence before recommending a commitment.
```

### Decide whether to fund growth

```text
Use the Rockefeller skill to review a proposed subscription growth investment.
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
| [agents/openai.yaml](agents/openai.yaml) | Optional Codex UI metadata; not required by other hosts |
| [evals/cases.jsonl](evals/cases.jsonl) | Agent-neutral decision cases and financial expectations, including two holdouts |
| [evals/activation.jsonl](evals/activation.jsonl) | Three positive and four negative discovery cases |
| [evals/fixtures/](evals/fixtures/) | Synthetic financial exports for evidence reconciliation |
| [evals/run.py](evals/run.py) | Optional runner for isolated Codex evaluation sessions |
| [evals/protocol.md](evals/protocol.md) | Agent-neutral evaluation method plus the optional Codex runner instructions |
| [evals/results.md](evals/results.md) | Dated results, evidence, and limitations |
| [README.md](README.md) | Installation, examples, and contributor guidance |

## Verification and development

On October 21, 2026, project installations from both this checkout and GitHub were checked with `skills` CLI 1.7.0 for Claude Code, Codex, Cursor, and GitHub Copilot. All installed core files matched the source. This checks installation and file integrity; runtime discovery and financial evaluations on other hosts remain separate checks. See [the portability results](evals/results.md#portability-checks--october-21-2026).

In Codex runs on October 20, 2026, the original and revised skill each passed **12 behavioral cases and seven activation checks**. Three representative no-skill cases also passed. These 41 formal runs found no regression on the covered checks; they do not establish a general accuracy improvement or statistical reliability. The revised spreadsheet answer provided more specific source references. See [the results](evals/results.md) for evidence and excluded infrastructure/preflight runs.

The prompts, fixtures, and grading expectations are reusable with any agent. Follow the host-neutral steps in [the protocol](evals/protocol.md) and use your host's installation, invocation, and trace controls. A result from one host does not establish discovery or behavior on another.

The bundled **optional Codex runner** requires Python 3.11+, Git, and an authenticated Codex CLI supporting its isolation flags; CLI 0.162.1 was verified. Those are development-tool requirements, not requirements to use Rockefeller in Claude Code or another agent. On this remote server, use `agent-run` for heavy evaluation workloads. Results belong outside the checkout; no extra Python packages are required.

Follow [the protocol](evals/protocol.md) to snapshot the baseline before editing, run matched comparisons, and grade every expectation using answer/trace evidence. The runner captures outputs and provenance; it does not automatically grade strategic judgment. Activation checks use natural prompts and actual skill-loading traces, separately from explicit invocation. The Codex runner disables connector and browsing access for the synthetic cases; other user/system skills can remain discoverable. Apply equivalent isolation when evaluating another host.

Keep the entrypoint self-contained. Add a financial helper or template when repeated use establishes a stable need, and move expanded specialist material into references when selective loading saves context. The current cases did not justify a mandatory input schema, forecast template, or business calculator. [OpenAI's authoring advice](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) similarly emphasizes concise, task-specific instructions.

Authoring references checked on October 20, 2026:

- [OpenAI: testing skills with evaluations](https://developers.openai.com/blog/eval-skills) — distinguish activation, outcomes, process, and efficiency.
- [Agent Skills: evaluating skills](https://agentskills.io/skill-creation/evaluating-skills) — compare behavior against concrete expectations and a baseline.
- [Agent Skills: optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) — evaluate when a skill is selected.
- [Agent Skills specification](https://agentskills.io/specification) — required metadata, optional resources, and progressive disclosure.
- [Anthropic: skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — concise guidance, appropriate degrees of freedom, and evaluation-driven iteration.
