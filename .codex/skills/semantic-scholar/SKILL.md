---
name: semantic-scholar
description: Semantic Scholar based advisor-publication workflow. Use when Codex needs author disambiguation, citation context, influential papers, recent paper lists, coauthor networks, or citation trails for PhD advisor fit analysis.
---

# Semantic Scholar

Adapted from `Agents365-ai/semanticscholar-skill` as a workflow note. Use live API access only when it is available in the environment.

## Procedure

1. Search for the author and confirm identity with affiliation, coauthors, topics, and official page.
2. Pull recent papers, influential papers, citation counts, and coauthor patterns when available.
3. Compare Semantic Scholar results against at least one other source for important claims.
4. Use citation trails to identify neighboring faculty and research clusters.
5. Feed serious candidates into `professor-fit-analyzer`.

## Good Uses

- Finding related faculty through coauthor networks.
- Checking whether a professor's recent direction still matches the applicant.
- Identifying papers to mention in outreach.

## Cautions

- Author profiles can merge or split incorrectly.
- Citation counts are not fit scores.
- Missing metadata should be marked as unknown.
