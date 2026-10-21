# Portable business context and decision review

Use when the user supplies earlier business notes, requests a saved decision, or returns to compare a forecast with actuals. Ordinary analysis does not require creating files or a memory service. Use a user-provided path; otherwise propose ordinary Markdown filenames in the user's project. Keep generated business records outside the installed skill package. Saving a requested record authorizes that document, not external commercial actions.

## Reuse context carefully

Read supplied context before repeating intake. Distinguish stable business facts from dated metrics and hypotheses; check which changed inputs could affect today's decision. Do not treat an old cash balance, quote, or forecast as current evidence. If saving is requested and supported, write the actual file and report its path. If writing is unavailable, provide a draft and say it has not been saved.

A compact `business-context.md` can capture:

- Business, buyer/segment, jurisdiction, currency, and objective.
- Dated operating and cash metrics, sources, and relevant definitions.
- Current constraint and evidence; commitments, reserve policy, and capacity.
- Open assumptions, existing decisions, and links to review records.

Use only relevant fields. Do not require this filename, a directory tied to an agent, or a fixed schema to use Rockefeller.

## Capture the decision before the outcome

For a requested `decision.md`, use enough structure to preserve the original prediction:

```markdown
# Decision: [business choice]

## Original decision — [date]
Objective and decision:
Evidence and sources, with periods and units:
Assumptions and unresolved questions:
Alternatives and reasons:
Expected incremental cash effect, timing, and reserve impact:
Condition that changes the choice:
Action, owner, review date or trigger:

## Review — [later date]
New evidence and sources:
Actual result versus the original forecast:
What changed and what remains uncertain:
Revised decision and next review trigger:
```

Keep the original dated forecast and rationale. Append later outcomes and revisions rather than rewriting the past to resemble what happened. Do not populate actual results before evidence exists.

## Reconcile actuals

Compare the same period, volume, scope, currency, and cash/accounting basis. Explain price, volume, fulfillment, quality, working-capital, and timing differences where supported. Count one-time setup/switching costs once; separate their first-period effect from recurring economics. Distinguish an observed variance from a proven cause.

For example, $2,000 monthly purchase savings less a $1,000 one-time switch gives a $1,000 first-month forecast benefit. Additional first-month rework of $2,600 changes the result to a $1,600 loss, a $2,600 adverse variance. If rework recurs at that volume, ongoing net savings are negative $600/month; do not keep charging the one-time switch monthly. Explain what repair or evidence would justify scaling again.

If actuals are missing, retain an open review rather than manufacturing success. Update the recommendation when evidence changes, and preserve the distinction between the prior forecast and the latest operating view.

Inspiration: [shared product context](https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md) and [gstack decision lineage](https://github.com/garrytan/gstack/blob/main/office-hours/sections/design-and-handoff.md), adapted to plain, user-controlled files that any agent can read.
