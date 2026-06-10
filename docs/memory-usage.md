# Persistent Advisor Memory Usage

## Session Startup

1. Read `docs/CONTEXT.md`.
2. Read `docs/source-policy.md`.
3. Read the relevant workflow.
4. Read the latest handoff.
5. If `.advisor-memory/snapshots/` exists locally, read snapshots as resume aids, then verify operational state from CSV trackers.

Memory snapshots are not the source of truth.

## When To Append Events

Append a private memory event after meaningful changes: applicant profile updates, search batches, faculty discovery/screening/archiving, priority changes, dossier updates, evidence/risk changes, program requirement checks, funding checks, paper reading notes, outreach state changes, replies, meetings, decisions, weekly reviews, and handoffs.

Every important decision should include source IDs, confidence, risk level, and next actions.

## Privacy

Write real memory only under `.advisor-memory/`. Public examples in `examples/memory/` are fake by design.

## Commands

```bash
python tools/memory_validate.py --events examples/memory/events.example.jsonl --schema schemas/memory-event.schema.json
python tools/memory_snapshot.py --events examples/memory/events.example.jsonl --sources examples/memory/sources.example.csv --out examples/memory/generated
python tools/memory_query.py recent --events examples/memory/events.example.jsonl
python tools/memory_query.py risks --events examples/memory/events.example.jsonl
```

Handoffs should list memory event IDs created during the session, or explain why no event was created.
