# Persistent Advisor Memory Workflow

## Goal

Maintain a durable local memory layer for long-running PhD advisor search without making memory snapshots the source of truth.

## Core Rules

- CSV trackers are operational truth.
- Memory events are append-only audit trail entries.
- Source records explain evidence used by memory events.
- Snapshots are generated read models for session resume.
- Snapshots are not the source of truth.
- Real private memory stays local in `.advisor-memory/` and must not be committed.
- Public examples must use fake people, fake programs, fake papers, and fake sources.

## Procedure

1. At session start, read memory snapshots if present, then verify operational state from CSV trackers.
2. Before appending an event, identify the object changed, source IDs, confidence, risk level, and next action.
3. Append an event after each meaningful change.
4. Maintain source records for source IDs used in events.
5. Regenerate snapshots after a batch, weekly review, handoff, or several related events.
6. Include memory event IDs in handoffs.
7. Never mark outreach approved unless the user explicitly approved it.

## Meaningful Changes

Append events for applicant profile updates, search batches, faculty state changes, dossiers, evidence and risk changes, program checks, funding checks, paper notes, outreach state, replies, meetings, decisions, weekly reviews, and handoffs.

## Validation

Use `tools/memory_validate.py` before trusting an event log. Use `tools/memory_snapshot.py` to regenerate snapshots. Use `tools/memory_query.py` to inspect recent events, faculty-specific events, risks, and next actions.
