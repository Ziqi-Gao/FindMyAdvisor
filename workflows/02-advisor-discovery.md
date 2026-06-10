# Advisor Discovery Workflow

Adapted from `find_my_supervisor` and the Scout role.

## Required Skill

Use `skills/advisor-batch-agent-roles/` for every substantial advisor-search batch.
Read `docs/subagent-registry.md` before assigning subagent work.

Core rule:

```text
many readers, one judge, one writer
```

Parallel subagents may scout, filter, audit, read papers, or collect difficulty evidence. The Batch Lead keeps final decision ownership, and the CRM Tracker is the single writer for core CSV files.

Do not open a new subagent until the existing role pool has been checked. Prefer resuming or sending input to registered agents.

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

1. Write a batch charter: search lane, target size, target difficulty mix, exclusions, and expected artifacts.
2. Check `docs/subagent-registry.md` for reusable agents and assign fixed roles from `advisor-batch-agent-roles`.
3. Resume or send input to existing subagents before spawning any new subagent.
4. Use parallel subagents for independent read-only tasks when available and authorized.
5. Build a longlist with source URLs for every candidate.
6. Record field, program, keywords, source strength, and rough overlap.
7. Mark admissions path when visible: direct advisor, rotation, program-level, committee, or unknown.
8. Filter candidates with no recent activity, no plausible fit, incompatible program structure, duplicate stronger alternatives, or compromised/unrelated sources.
9. Apply `admission-difficulty-calibrator` before treating a high-fit candidate as strategically balanced.
10. Update all required CRM tables for every serious candidate:
   - `data/advisors.csv`
   - `data/faculty-index.csv`
   - `data/evidence-matrix.csv`
   - `data/program-difficulty.csv`
11. Rebuild `data/advisor-composite-scores.csv` and `docs/advisor-ranked-master-table.md`.
12. Promote only evidence-backed candidates to dossier review.
13. Write a batch report, update durable context/status files, update `docs/subagent-registry.md`, and write a handoff.
14. Run the validation gate from `advisor-batch-agent-roles` before final response.

## Minimum Evidence Threshold

Before a candidate can enter the CRM, require:

- Official faculty, department, lab, or program source.
- At least one recent publication, lab/student, grant/funding, or admissions/prospective-student signal.
- A research-fit rationale tied to the applicant's current profile.
- Evidence labels for important claims: Fact, Inference, Unknown, or Risk lead.

If these are missing, keep the lead in the batch report as deferred rather than adding it to the CRM.

## Output

- Longlist table.
- Removed-candidate table with reasons.
- Difficulty/portfolio flags for serious candidates.
- Next search batch.
- CRM delta and validation summary.
