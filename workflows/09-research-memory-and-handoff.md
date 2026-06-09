# Research Memory And Handoff Workflow

Adapted from Research-Pilot and claude-research memory patterns.

## Goal

Prevent long-running search work from losing context.

## Files

- `docs/CONTEXT.md`: persistent applicant profile and current focus.
- `data/advisors.csv`: candidate state.
- `data/outreach.csv`: outreach state.
- `docs/handoffs/`: session summaries.
- `docs/skill-inventory.md`: why each workflow exists.

## Procedure

1. Before work, read the latest handoff and `docs/CONTEXT.md`.
2. During work, update CSVs and templates as facts change.
3. After work, write a handoff using `templates/session-handoff.md`.
4. Include exact next actions so the next session can resume.

## Rule

Do not leave important decisions only in chat history.
