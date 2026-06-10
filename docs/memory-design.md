# Persistent Advisor Memory Design

The persistent advisor memory layer records how and why advisor-search state changed across long-running sessions. CSV trackers remain the operational truth. Memory events are an append-only audit trail. Snapshots are generated read models for resuming work.

This PR does not add a dashboard, SQLite database, or non-standard runtime dependency.

## Privacy Boundary

Real memory belongs in `.advisor-memory/`, which is ignored by Git. Public examples must use fake people, fake programs, fake papers, and fake sources.

Do not commit real applicant memory, real private advisor notes, private dossier drafts, emails, local CSV exports, or secrets.

## Suggested Local Layout

```text
.advisor-memory/
  events.jsonl
  sources.csv
  snapshots/
    current-state.md
    next-actions.md
    risk-register.md
    memory-snapshot.json
```

## Layer Responsibilities

| Layer | Responsibility | Source of truth? |
|---|---|---|
| CSV trackers | Operational advisor, program, evidence, outreach, and decision state | Yes |
| Memory events | Append-only explanation of state changes | No |
| Source records | Stable source IDs used by events | No |
| Snapshots | Generated resume aids | No |

If a snapshot conflicts with a CSV tracker, trust the CSV tracker and regenerate the snapshot after reviewing events.

## Event Requirements

Every important decision should include source IDs, confidence, risk level, next actions, files touched, and whether human approval was required or granted.

Outreach approval must never be inferred. `outreach_approved` and `outreach_sent` events require explicit human approval.
