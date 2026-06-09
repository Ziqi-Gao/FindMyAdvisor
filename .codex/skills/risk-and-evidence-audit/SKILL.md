---
name: risk-and-evidence-audit
description: Evidence matrix and risk audit skill for advisor search. Use when Codex needs to verify that advisor fit scores, shortlist decisions, outreach claims, funding interpretations, and program feasibility judgments are source-backed, dated, confidence-labeled, and free of hallucinated claims.
---

# Risk And Evidence Audit

## Procedure

1. Read the relevant dossier, CSV rows, and source policy.
2. For every important judgment, identify source URL, checked date, confidence, and evidence note.
3. Update or propose rows for `data/evidence-matrix.csv`.
4. Flag missing sources, stale sources, weak inferences, name-collision risks, and overconfident funding claims.
5. Separate fact, inference, unknown, and risk lead.
6. Recommend downgrade, removal, or further checking when evidence is weak.

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
- Unsupported claims.
- Risk list.
- Priority recommendation.
