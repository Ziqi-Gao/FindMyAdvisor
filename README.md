# FindMyAdvisor

A Codex-first workflow repository for 2027 Fall North American PhD applications in Computer Science, Statistics, and Biostatistics.

The repository is organized around advisor discovery and evidence-backed due diligence. SOP writing is intentionally secondary.

## Core Loop

1. Clarify the applicant profile, research agenda, constraints, and application targets.
2. Build a faculty longlist from official, bibliographic, grant, and lab sources.
3. Filter weak, stale, or non-admitting matches.
4. Create evidence-backed professor dossiers.
5. Check funding, admissions path, program requirements, and availability signals.
6. Audit every claim before outreach.
7. Track shortlist, outreach, replies, weekly reviews, and decisions.

## What Is Installed

Project-scoped Codex skills live in `.codex/skills/`:

- `find-my-supervisor` - core advisor discovery workflow adapted for North America.
- `professor-fit-analyzer` - faculty dossier and fit scoring workflow.
- `paper-search` - multi-source paper discovery and evidence harvesting.
- `paper-reading-note` - structured reading cards for advisor papers.
- `semantic-scholar` - author, citation, and influence lookup workflow.
- `asta-literature` - optional Asta/Semantic Scholar literature search workflow when API access exists.
- `grill-with-docs` - profile intake and document interrogation before search.
- `statement-fit-review` - SOP and research statement review against advisor evidence.
- `handoff-manager` - durable handoff notes for long-running application work.
- `issue-slicer` - split advisor search into manageable GitHub issues.
- `research-pilot-memory` - project memory and decision log workflow.
- `academic-research-suite` - broader literature review and proposal support.
- `advisor-workflow-roles` - Scout, Filter, Auditor, Tracker, and Copywriter roles adapted from summer research agent workflows.
- `application-crm` - longlist, shortlist, outreach, and status tracking.
- `funding-signal-check` - NSF, NIH, and lab funding signal checks.
- `program-requirements-audit` - deadline, requirement, and faculty-contact-policy checks.
- `risk-and-evidence-audit` - source-backed evidence matrix and risk review.
- `outreach-auditor` - email draft review and human approval gate.

## Borrowed Workflows

Borrowed workflows are not installed verbatim. They are adapted into `workflows/` and templates:

- `summer-research-agent`: Scout, Filter, Auditor, Tracker, Copywriter, and human approval loop.
- `mattpocock/skills`: grill-with-docs, handoff, and issue slicing patterns.
- `flonat/claude-research`: project profile, current focus, session log, and audit habits.
- `co-researcher`: critical synthesis, ethics, bibliography, and proposal thinking.
- `PaperPilot`: search protocol, deduplication, inclusion/exclusion, and evidence report style.
- `Research-Pilot`: lightweight project memory, rather than a full local dashboard.

## Repository Map

- `.codex/skills/` - project-scoped skills for Codex.
- `workflows/` - reusable advisor-search workflows adapted from external projects.
- `templates/` - profile, dossier, report, outreach, funding, weekly review, and handoff templates.
- `schemas/` - lightweight JSON schemas for structured advisor and applicant data.
- `data/` - CSV trackers and local working datasets.
- `dossiers/` - faculty and program dossier templates, plus future per-candidate dossiers.
- `docs/` - profile context, decision notes, handoffs, source policy, and skill inventory.

## Day 0 Use

1. Fill `templates/applicant-profile.md` into `docs/CONTEXT.md`.
2. Ask Codex to use `grill-with-docs` to interrogate your CV, research summary, transcript notes, and project history.
3. Use `find-my-supervisor` and `advisor-workflow-roles` to build the first longlist.
4. Use `professor-fit-analyzer`, `paper-search`, and `funding-signal-check` on the top candidates.
5. Use `risk-and-evidence-audit` to keep every high-priority judgment source-backed.
6. Use `program-requirements-audit` before treating a program as application-ready.
7. Use `application-crm` to keep `data/advisors.csv`, `data/faculty-index.csv`, `data/evidence-matrix.csv`, and outreach trackers current.

## Safety Defaults

- Use public sources only.
- Separate facts, inferences, and unknowns.
- Never treat anonymous reputation as fact.
- Never use Sci-Hub or unauthorized paper downloads.
- Never send outreach automatically.
- Require human approval before any email is used.
- Prefer official department, lab, admissions, bibliographic, NSF, and NIH sources.
