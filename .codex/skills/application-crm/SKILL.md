---
name: application-crm
description: PhD application CRM skill for maintaining advisor longlists, shortlists, evidence matrix, program requirements, outreach status, replies, follow-ups, and decision notes. Use when Codex needs to update or summarize application tracking CSVs.
---

# Application CRM

## Files

- `data/advisors.csv`: simple advisor candidate tracker.
- `data/faculty-index.csv`: canonical faculty index.
- `data/evidence-matrix.csv`: source-backed fit and risk evidence.
- `data/programs.csv`: program requirements and deadlines.
- `data/outreach.csv`: simple outreach tracker.
- `data/outreach-log.csv`: detailed outreach audit log.
- `data/interaction-log.csv`: meetings, replies, and other interactions.
- `data/application-crm.csv`: overall application state.
- `.advisor-memory/events.jsonl`: private local audit trail for meaningful CRM changes.

## Procedure

1. Before changing status, identify the source or reason.
2. Keep one canonical row per faculty candidate in `data/faculty-index.csv`.
3. Keep evidence rows in `data/evidence-matrix.csv`, not only in prose.
4. Keep outreach rows in `data/outreach-log.csv` or `data/outreach.csv`.
5. Use stable statuses: discovered, screened, dossier-ready, outreach-ready, contacted, replied, archived, priority.
6. Create or propose memory events for meaningful CRM changes when `.advisor-memory/` is available.
7. Never mark outreach as approved unless the user explicitly approved it.
8. Summarize changes after updates, including memory event IDs when events were created.

## Rule

The CSVs are the operational truth. Memory events are the audit trail. Memory snapshots are generated read models and are not the source of truth. Reports and chat summaries should agree with the CSVs.
