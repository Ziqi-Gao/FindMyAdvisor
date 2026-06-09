---
name: paper-search
description: Literature and publication evidence search skill for advisor matching. Use when Codex needs to find, deduplicate, and summarize recent papers for a faculty member, research cluster, or applicant-advisor fit decision using public bibliographic sources.
---

# Paper Search

Inspired by `openags/paper-search-mcp` and adapted for advisor-search evidence.

## Procedure

1. Identify the exact author identity before trusting paper matches.
2. Search across the best sources for the field: DBLP for CS, PubMed/PMC for biostatistics, arXiv and Google Scholar for statistics, and Semantic Scholar/OpenAlex/Crossref as cross-checks.
3. Deduplicate by title, DOI, venue, year, and author list.
4. Keep papers only when they support fit, risk, funding, student signal, or outreach specificity.
5. Summarize what each paper proves about advisor fit.

## Output Table

| Year | Paper | Venue | Source | Fit Evidence | Notes |
|---|---|---|---|---|---|

## Rules

- Do not create a generic literature dump.
- Do not cite inaccessible full text as if it was read.
- Use abstracts and metadata carefully when full text is unavailable.
- Mark author identity uncertainty when names collide.
