# Workflow Overview

This repository is designed for repeated advisor-search cycles.

## Cycle

1. Intake: use `grill-with-docs` to clarify applicant fit signals.
2. Scout: use `find-my-supervisor` and `advisor-workflow-roles` to build a longlist.
3. Filter: remove weak, stale, or impossible matches.
4. Dossier: use `professor-fit-analyzer` to produce evidence-backed profiles.
5. Literature: use `paper-search`, `semantic-scholar`, or `asta-literature` where useful.
6. Funding: use `funding-signal-check` for NSF, NIH, and lab signals.
7. Audit: use `outreach-auditor` before any email draft is approved.
8. Track: use `application-crm` to update CSVs.
9. Handoff: use `handoff-manager` after each serious session.

## Default Batch Size

Search in batches of 5-15 faculty. Deep-dive only after the first filter pass.

## Done Definition

A candidate is shortlist-ready only when the repository has:

- At least two public sources supporting fit.
- A clear program/admissions path or a marked unknown.
- A recent publication, project, grant, or lab signal.
- A risk/unknown section.
- A next action.
