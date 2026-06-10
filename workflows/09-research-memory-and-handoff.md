# Research Memory And Handoff Workflow

Adapted from Research-Pilot and claude-research memory patterns.

## Goal

Prevent long-running search work from losing context.

## Files

- `docs/CONTEXT.md`: persistent applicant profile and current focus.
- `data/advisors.csv`: candidate state.
- `data/outreach.csv`: outreach state.
- `.advisor-memory/events.jsonl`: private local append-only memory events.
- `.advisor-memory/sources.csv`: private local source records for memory events.
- `.advisor-memory/snapshots/`: generated read models for session resume.
- `docs/handoffs/`: session summaries.
- `docs/skill-inventory.md`: why each workflow exists.

## Procedure

1. Before work, read the latest handoff and `docs/CONTEXT.md`.
2. If local memory snapshots exist, read them as resume aids, then verify operational state from CSV trackers.
3. During work, update CSVs and templates as facts change.
4. After meaningful changes, append memory events with source IDs, confidence, risk level, and next actions.
5. Regenerate memory snapshots after batch, weekly review, or handoff work.
6. After work, write a handoff using `templates/session-handoff.md`.
7. Include memory event IDs and exact next actions so the next session can resume.

## Rule

Do not leave important decisions only in chat history. CSV trackers are operational truth; memory events are the audit trail; memory snapshots are generated read models and are not the source of truth.
