---
name: asta-literature
description: Optional Asta or Semantic Scholar literature search workflow for advisor discovery and research cluster mapping. Use when Codex has Asta/Semantic Scholar API access or needs to plan such a search for faculty fit, related work, or adjacent advisor discovery.
---

# Asta Literature

Adapted from `Agents365-ai/asta-skill`. This repository does not assume an API key is present.

## Use When

- API access exists and a query needs stronger literature graph support.
- A faculty candidate has many papers and manual triage is slow.
- A research cluster needs related-paper expansion.

## Procedure

1. Start from a precise topic, paper title, or faculty author profile.
2. Retrieve candidate papers or related work.
3. Cross-check key findings against official pages or bibliographic sources.
4. Convert results into advisor-fit evidence, not broad summaries.
5. Mark unavailable API access as a blocker and provide a manual fallback.

## Fallback

Use `paper-search` with DBLP, PubMed, OpenAlex, Google Scholar, arXiv, Crossref, and official lab pages.
