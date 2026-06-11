# FindMyAdvisor

A Codex-first workflow repository for 2027 Fall North American PhD applications in Computer Science, Statistics, and Biostatistics.

The repository is organized around advisor discovery and evidence-backed due diligence. SOP writing is intentionally secondary.

## Core Loop

1. Clarify the applicant profile, research agenda, constraints, and application targets.
2. Build a faculty longlist from official, bibliographic, grant, and lab sources.
3. Filter weak, stale, or non-admitting matches.
4. Create evidence-backed professor dossiers.
5. Check funding, admissions path, program requirements, and availability signals.
6. Audit every claim before outreach.
7. Track shortlist, outreach, replies, weekly reviews, and decisions.

## Persistent Advisor Memory

This repository includes a lightweight persistent advisor memory layer for long-running search work.

- `.advisor-memory/` is the private local workspace for real memory events, source records, and generated snapshots.
- Memory events are append-only audit trail entries that explain how and why advisor, program, evidence, outreach, and decision state changed.
- Source records give stable source IDs for event evidence.
- Snapshots are generated read models for session resume, such as current state, next actions, and risk register.
- CSV trackers remain the operational truth. Memory snapshots are not the source of truth.
- Public examples under `examples/memory/` use fake people, fake programs, fake papers, and fake sources.
- Real applicant memory, private advisor notes, emails, and local exports are ignored by Git and must stay private.

Useful commands:

```bash
python tools/memory_validate.py --events examples/memory/events.example.jsonl --schema schemas/memory-event.schema.json
python tools/memory_snapshot.py --events examples/memory/events.example.jsonl --sources examples/memory/sources.example.csv --out examples/memory/generated
python tools/memory_query.py recent --events examples/memory/events.example.jsonl
python tools/memory_query.py risks --events examples/memory/events.example.jsonl
```

## What Is Installed

Project-scoped Codex skills live in `.codex/skills/`:

- `find-my-supervisor` - core advisor discovery workflow adapted for North America.
- `professor-fit-analyzer` - faculty dossier and fit scoring workflow.
- `paper-search` - multi-source paper discovery and evidence harvesting.
- `paper-reading-note` - structured reading cards for advisor papers.
- `semantic-scholar` - author, citation, and influence lookup workflow.
- `asta-literature` - optional Asta/Semantic Scholar literature search workflow when API access exists.
- `grill-with-docs` - profile intake and document interrogation before search.
- `statement-fit-review` - SOP and research statement review against advisor evidence.
- `handoff-manager` - durable handoff notes for long-running application work.
- `issue-slicer` - split advisor search into manageable GitHub issues.
- `research-pilot-memory` - project memory and decision log workflow.
- `advisor-memory-manager` - local append-only advisor memory events, source records, and generated snapshots.
- `academic-research-suite` - broader literature review and proposal support.
- `advisor-workflow-roles` - Scout, Filter, Auditor, Tracker, and Copywriter roles adapted from summer research agent workflows.
- `advisor-batch-agent-roles` - fixed large-batch advisor-search role ownership, quality gates, and subagent registry protocol.
- `application-crm` - longlist, shortlist, outreach, and status tracking.
- `funding-signal-check` - NSF, NIH, and lab funding signal checks.
- `program-requirements-audit` - deadline, requirement, and faculty-contact-policy checks.
- `admission-difficulty-calibrator` - applicant-specific admission difficulty and portfolio balance scoring.
- `risk-and-evidence-audit` - source-backed evidence matrix and risk review.
- `outreach-auditor` - email draft review and human approval gate.

## Borrowed Workflows

Borrowed workflows are not installed verbatim. They are adapted into `workflows/` and templates:

- `summer-research-agent`: Scout, Filter, Auditor, Tracker, Copywriter, and human approval loop.
- `mattpocock/skills`: grill-with-docs, handoff, and issue slicing patterns.
- `flonat/claude-research`: project profile, current focus, session log, and audit habits.
- `co-researcher`: critical synthesis, ethics, bibliography, and proposal thinking.
- `PaperPilot`: search protocol, deduplication, inclusion/exclusion, and evidence report style.
- `Research-Pilot`: lightweight project memory, rather than a full local dashboard.

## Repository Map

- `.codex/skills/` - project-scoped skills for Codex.
- `workflows/` - reusable advisor-search workflows adapted from external projects.
- `templates/` - profile, dossier, report, outreach, funding, weekly review, and handoff templates.
- `schemas/` - lightweight JSON schemas for structured advisor and applicant data.
- `data/` - CSV trackers and local working datasets.
- `dossiers/` - faculty and program dossier templates, plus future per-candidate dossiers.
- `docs/` - profile context, decision notes, handoffs, source policy, and skill inventory.
- `examples/memory/` - fake memory examples for tests and documentation.
- `tools/` - lightweight standard-library utilities for memory validation, snapshots, queries, and appends.

## Day 0 Use

1. Fill `templates/applicant-profile.md` into `docs/CONTEXT.md`.
2. Ask Codex to use `grill-with-docs` to interrogate your CV, research summary, transcript notes, and project history.
3. Use `find-my-supervisor` and `advisor-workflow-roles` to build the first longlist.
4. Use `professor-fit-analyzer`, `paper-search`, and `funding-signal-check` on the top candidates.
5. Use `risk-and-evidence-audit` to keep every high-priority judgment source-backed.
6. Use `program-requirements-audit` before treating a program as application-ready.
7. Use `application-crm` to keep `data/advisors.csv`, `data/faculty-index.csv`, `data/evidence-matrix.csv`, and outreach trackers current.
8. Use `advisor-memory-manager` after meaningful changes to append private memory events and regenerate snapshots.

## Safety Defaults

- Use public sources only.
- Separate facts, inferences, and unknowns.
- Never treat anonymous reputation as fact.
- Never use Sci-Hub or unauthorized paper downloads.
- Never send outreach automatically.
- Require human approval before any email is used.
- Prefer official department, lab, admissions, bibliographic, NSF, and NIH sources.
- Keep real applicant memory local and private under `.advisor-memory/`.
