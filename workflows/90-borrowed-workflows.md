# Borrowed Workflow Adaptations

This file records how useful external workflows were adapted without installing them verbatim.

## summer-research-agent

Local adaptation:

- Scout becomes advisor longlist discovery.
- Filter removes weak fit, stale web presence, unclear program route, and irrelevant directions.
- Auditor rechecks every source before a candidate reaches shortlist or outreach.
- Tracker maintains `data/advisors.csv` and `data/outreach.csv`.
- Copywriter writes only A-tier outreach drafts and never sends.
- Human approval is mandatory before any email is used.

## flonat/claude-research

Local adaptation:

- Persistent profile becomes `docs/CONTEXT.md`.
- Current focus is stored inside `docs/CONTEXT.md`.
- Session logs become `docs/handoffs/`.
- Audit habits are folded into `docs/source-policy.md` and `outreach-auditor`.

## co-researcher

Local adaptation:

- Bibliography and synthesis patterns become `workflows/07-critical-review-and-synthesis.md`.
- Ethics and critical review principles are used for source labeling and risk review.
- Grant/proposal thinking is kept secondary until advisor fit is clearer.

## PaperPilot

Local adaptation:

- Search protocol becomes `workflows/04-paper-evidence-protocol.md`.
- Inclusion/exclusion rules are used for advisor evidence.
- Deduplication is required before papers are used in dossiers.
- Output is a fit evidence table, not a broad literature dump.

## Research-Pilot

Local adaptation:

- Full local dashboard is not installed.
- Lightweight memory is implemented through `docs/CONTEXT.md`, CSV trackers, and handoffs.
- Decisions should be written into files, not only chat.

## mattpocock/skills

Local adaptation:

- `grill-with-docs` becomes applicant profile interrogation.
- `handoff` becomes `handoff-manager` and `templates/session-handoff.md`.
- `to-issues` becomes `issue-slicer` for advisor-search batches.
