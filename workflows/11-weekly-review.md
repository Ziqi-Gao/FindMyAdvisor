# Weekly Review Workflow

## Procedure

1. Read `docs/CONTEXT.md`, the latest handoff, and `docs/weekly-review.md`.
2. If `.advisor-memory/snapshots/` exists locally, read generated snapshots as resume aids.
3. Check active rows in `data/application-crm.csv`.
4. Find candidates with missing evidence, stale last-checked dates, or unclear next actions.
5. Rebalance the portfolio across field and risk tier.
6. Identify the next 3-5 concrete tasks.
7. Regenerate memory snapshots after the weekly review if memory events changed.
8. Write a weekly review note from `templates/weekly-review.md`.
9. Append a `weekly_review_completed` memory event when `.advisor-memory/` is available.

## Done Definition

- Every priority candidate has a next action.
- Every outreach item has a status.
- Every urgent deadline has been checked against an official page.
- New risks are visible in the CRM, memory event log, or weekly review note.
- Memory snapshots have been regenerated when memory events changed.

## Rule

CSV trackers remain operational truth. Weekly memory snapshots are generated read models, not source of truth.
