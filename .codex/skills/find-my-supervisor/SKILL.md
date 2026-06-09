---
name: find-my-supervisor
description: Advisor discovery skill for 2027 Fall North American PhD applications in CS, Statistics, Biostatistics, and adjacent interdisciplinary fields. Use when Codex needs to build a faculty longlist, shortlist potential PhD supervisors, compare advisor fit, or plan advisor-search batches from public evidence.
---

# Find My Supervisor

Adapted from `Oisinwang/find_my_supervisor` for North American PhD applications.

## Procedure

1. Read `docs/CONTEXT.md` and `docs/source-policy.md`.
2. Clarify field, topic keywords, target institutions, and constraints.
3. Build a longlist from official program, department, lab, publication, and grant sources.
4. For each candidate, record university, program, faculty page, keywords, admissions path, source URLs, and first-pass fit.
5. Remove candidates with no plausible research overlap, stale evidence, incompatible program path, or weak relevance.
6. Promote strong candidates to `professor-fit-analyzer`.
7. Update `data/advisors.csv` and write a shortlist summary when the batch is complete.

## Evidence Rules

- Use public sources only.
- Label facts, inferences, and unknowns.
- Prefer recent evidence from the last 3 years.
- Never infer that a professor is recruiting solely because they have a grant.

## Output

Return a longlist table, removed-candidate table, shortlist candidates, unknowns, and next actions.
