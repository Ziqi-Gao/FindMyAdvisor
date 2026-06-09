---
name: advisor-workflow-roles
description: Multi-role advisor search workflow skill. Use when Codex needs to run Scout, Filter, Auditor, Tracker, or Copywriter roles for PhD advisor discovery, screening, source checking, CRM updates, and outreach drafting with human approval.
---

# Advisor Workflow Roles

Adapted from `summer-research-agent`, but retargeted from summer research to PhD advisor search.

## Roles

- Scout: find faculty candidates from public sources.
- Filter: remove weak fit, stale, non-admitting, or irrelevant candidates.
- Auditor: re-check sources and label facts, inferences, unknowns, and risk leads.
- Tracker: update `data/advisors.csv` and `data/outreach.csv`.
- Copywriter: draft short outreach only for A-tier candidates.

## Procedure

1. Choose one role for the current task.
2. Work in small batches.
3. Keep source URLs with every candidate.
4. Audit before shortlist and before outreach.
5. Never send email automatically.

## Output

Role-specific result plus file updates or recommended updates.
