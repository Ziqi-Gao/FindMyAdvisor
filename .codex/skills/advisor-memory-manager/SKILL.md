---
name: advisor-memory-manager
description: Manage the private persistent advisor memory layer for long-running PhD advisor search, including append-only events, source records, generated snapshots, and handoff integration.
---

# Advisor Memory Manager

Use this skill when Codex needs to append memory events, maintain source records, regenerate memory snapshots, or explain how advisor-search state changed across sessions.

## Required Reading

1. `docs/CONTEXT.md`
2. `docs/source-policy.md`
3. `workflows/12-persistent-advisor-memory.md`
4. Existing `.advisor-memory/snapshots/`, if present locally
5. Relevant CSV trackers before treating any snapshot as current state

## Rules

- CSV trackers are operational truth.
- Memory events are append-only audit trail entries.
- Snapshots are generated read models, not source of truth.
- Real memory must stay under `.advisor-memory/` and must not be committed.
- Public examples must use fake people, fake programs, fake papers, and fake sources.
- Separate fact, inference, unknown, and risk lead.
- Every important decision should include source IDs, confidence, risk level, and next action.
- Never mark outreach approved without explicit user approval.

## Procedure

1. Confirm the meaningful change and relevant operational CSV row or file.
2. Identify source IDs and add or update source records when needed.
3. Append a memory event with before/after notes, evidence note, confidence, risk level, next actions, and files touched.
4. Regenerate snapshots with `tools/memory_snapshot.py` or propose snapshot changes if private memory is unavailable.
5. Validate events with `tools/memory_validate.py`.
6. Include created event IDs in the session handoff.

## Output

- Memory event IDs created or proposed.
- Source IDs used.
- Snapshot files regenerated or recommended.
- Unresolved unknowns or risks.
