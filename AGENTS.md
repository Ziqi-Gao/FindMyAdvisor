# Agent Instructions

This repository is a long-running workflow for 2027 Fall North American PhD applications in CS, Statistics, and Biostatistics. The main objective is finding strong advisor and program fit. SOP drafting is secondary.

## Operating Rules

- Start by reading `docs/CONTEXT.md`, `docs/source-policy.md`, and the relevant workflow file.
- If `.advisor-memory/snapshots/` exists locally, read those snapshots at session start as resume aids, then verify operational state from CSV trackers.
- Keep advisor work evidence-backed. Label every important claim as fact, inference, or unknown.
- Prefer public sources: official faculty pages, department pages, lab pages, admissions pages, recent papers, DBLP, PubMed, OpenAlex, Semantic Scholar, Google Scholar, NSF Award Search, NIH RePORTER, and official student/lab pages.
- Do not rely on anonymous reputation claims as facts. They may be logged as unverified risk leads only.
- Do not automatically send outreach. Draft only, then require explicit human approval.
- Update `data/advisors.csv` and `data/outreach.csv` when a candidate or outreach status changes.
- After meaningful advisor, program, evidence, outreach, or decision changes, append a private memory event when `.advisor-memory/` is available.
- Write a handoff in `docs/handoffs/` after any substantial session, including memory event IDs when events were created.
- Use concise English for repository artifacts unless the user asks for Chinese output.

## Advisor Fit Priorities

Score fit across these dimensions:

1. Research overlap with the applicant's actual projects and next-step interests.
2. Evidence strength from recent publications, grants, labs, and student outcomes.
3. Admissions path: direct advisor match, rotation, committee, or program-level admission.
4. Funding and availability signals.
5. Advising risk, including stale web presence, no recent students, poor publication continuity, or unclear PhD admission route.
6. Strategic portfolio balance across reach, target, and safer programs.

## Persistent Advisor Memory

- CSV trackers are operational truth.
- Memory events are an append-only audit trail explaining how and why state changed.
- Memory snapshots are generated read models and are not the source of truth.
- Real memory stays local in `.advisor-memory/` and must not be committed.
- Public examples must use fake people, fake programs, fake papers, and fake sources.

## Output Style

For advisor searches, produce:

- A longlist table.
- A shortlist table.
- Dossier notes for serious candidates.
- Risk and unknowns.
- Next actions with source URLs.

For outreach, produce:

- Draft email only.
- A source-backed rationale for why the faculty member is worth contacting.
- Explicit missing evidence.
- A human approval checkbox.
