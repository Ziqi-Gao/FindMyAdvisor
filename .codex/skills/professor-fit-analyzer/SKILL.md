---
name: professor-fit-analyzer
description: Faculty dossier and advisor-fit analysis skill for PhD applications. Use when Codex needs to evaluate a specific professor or small faculty set for research fit, funding signal, admissions path, advising risk, student outcomes, and outreach priority.
---

# Professor Fit Analyzer

Adapted from `voidful/academic-skills` professor-fit-analyser patterns.

## Procedure

1. Read the applicant profile and source policy.
2. For each faculty member, collect official profile, lab page, recent publications, grant signals, student/lab evidence, and admissions route.
3. Score research fit, evidence strength, funding signal, admissions path clarity, and risk.
4. Distinguish field-specific signals:
   - CS: conference continuity, DBLP, lab students, NSF/industry signal.
   - Statistics: methodology overlap, arXiv/journal continuity, NSF DMS, collaborations.
   - Biostatistics: PubMed continuity, NIH signal, clinical/public health collaborations, student first-author patterns.
5. Use `templates/advisor-dossier.md` for serious candidates.
6. Update `data/advisors.csv`.

## Risk Checks

- Stale personal page or no recent papers.
- No visible PhD students or unclear advising role.
- Publications have drifted away from applicant interest.
- Program admits by rotation or committee and professor contact has limited value.
- Funding exists but is unrelated to the applicant's target topic.

## Output

Produce a dossier with source URLs, fit score, evidence strength, risks, unknowns, and next action.
