# Advisor Discovery Workflow

Adapted from `find_my_supervisor` and the Scout role.

## Inputs

- Applicant profile from `docs/CONTEXT.md`.
- Target institutions, programs, or research keywords.
- Field focus: CS, Statistics, Biostatistics, or interdisciplinary.

## Discovery Sources

- Official department faculty pages.
- Lab pages and project pages.
- Program admissions pages.
- DBLP for CS.
- PubMed and NIH RePORTER for biostatistics and biomedical data science.
- Google Scholar, Semantic Scholar, OpenAlex, arXiv, bioRxiv, medRxiv, Crossref.
- NSF Award Search for CS/statistics/methodology funding.

## Procedure

1. Build a longlist with source URLs for every candidate.
2. Record field, program, keywords, and source strength.
3. Mark admissions path when visible: direct advisor, rotation, program-level, committee, or unknown.
4. Filter candidates with no recent activity, no plausible fit, or incompatible program structure.
5. Update `data/advisors.csv`.
6. Promote only evidence-backed candidates to dossier review.

## Output

- Longlist table.
- Removed-candidate table with reasons.
- Next search batch.
