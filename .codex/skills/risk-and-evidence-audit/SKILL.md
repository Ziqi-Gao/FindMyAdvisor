---
name: risk-and-evidence-audit
description: Evidence matrix and risk audit skill for advisor search. Use when Codex needs to verify that advisor fit scores, shortlist decisions, outreach claims, funding interpretations, and program feasibility judgments are source-backed, dated, confidence-labeled, and free of hallucinated claims.
---

# Risk And Evidence Audit

## Procedure

1. Read the relevant dossier, CSV rows, source policy, and memory snapshots if present locally.
2. For every important judgment, identify source URL, source ID when available, checked date, confidence, and evidence note.
3. Update or propose rows for `data/evidence-matrix.csv`.
4. Append or propose memory events for evidence additions, evidence revisions, risk additions, and risk resolutions when `.advisor-memory/` is available.
5. Flag missing sources, stale sources, weak inferences, name-collision risks, and overconfident funding claims.
6. Separate fact, inference, unknown, and risk lead.
7. Recommend downgrade, removal, or further checking when evidence is weak.

## Criteria

- research_fit
- method_fit
- domain_fit
- recent_activity
- funding_signal
- student_mentoring_signal
- admissions_feasibility
- outreach_priority
- program_requirements_risk

## Output

- Evidence matrix updates.
- Memory event IDs or proposed events for evidence/risk changes.
- Unsupported claims.
- Risk list.
- Priority recommendation.

## Rule

CSV trackers are operational truth. Memory events explain how and why evidence or risk state changed. Memory snapshots are not the source of truth.
