# Skill Inventory

This is the implementation record for the skill and workflow search.

## Installed As Project Skills

| Skill | Source Inspiration | Local Path | Purpose |
|---|---|---|---|
| find-my-supervisor | https://github.com/Oisinwang/find_my_supervisor | `.codex/skills/find-my-supervisor/` | Core advisor discovery and shortlist workflow. |
| professor-fit-analyzer | https://github.com/voidful/academic-skills | `.codex/skills/professor-fit-analyzer/` | Faculty dossier, fit scoring, and risk review. |
| paper-search | https://github.com/openags/paper-search-mcp | `.codex/skills/paper-search/` | Multi-source paper evidence harvesting. |
| paper-reading-note | PaperPilot and Research-Pilot patterns | `.codex/skills/paper-reading-note/` | Turn advisor papers into structured fit notes. |
| semantic-scholar | https://github.com/Agents365-ai/semanticscholar-skill | `.codex/skills/semantic-scholar/` | Author, citation, and influence lookup workflow. |
| asta-literature | https://github.com/Agents365-ai/asta-skill | `.codex/skills/asta-literature/` | Optional Asta/Semantic Scholar search pattern when credentials exist. |
| grill-with-docs | https://github.com/mattpocock/skills | `.codex/skills/grill-with-docs/` | Applicant-profile interrogation before searching. |
| statement-fit-review | grill-with-docs plus advisor-fit workflow | `.codex/skills/statement-fit-review/` | Review SOP/research statement against advisor evidence. |
| handoff-manager | https://github.com/mattpocock/skills | `.codex/skills/handoff-manager/` | Durable session handoffs. |
| issue-slicer | https://github.com/mattpocock/skills | `.codex/skills/issue-slicer/` | Turn advisor search plans into GitHub issues. |
| research-pilot-memory | https://github.com/QZhang2111/Research-Pilot | `.codex/skills/research-pilot-memory/` | Lightweight project memory and decision logs. |
| academic-research-suite | https://github.com/Imbad0202/academic-research-skills-codex | `.codex/skills/academic-research-suite/` | Literature review and proposal support. |
| advisor-workflow-roles | https://github.com/jiasiqi312/summer-research-agent | `.codex/skills/advisor-workflow-roles/` | Scout, Filter, Auditor, Tracker, Copywriter roles adapted for PhD advisor search. |
| application-crm | Adapted from tracker workflows | `.codex/skills/application-crm/` | Keep longlist, shortlist, outreach, and status data current. |
| funding-signal-check | Advisor-search extension | `.codex/skills/funding-signal-check/` | NSF, NIH, and lab funding signal review. |
| program-requirements-audit | Self-built from application workflow needs | `.codex/skills/program-requirements-audit/` | Deadlines, requirements, contact policy, and program feasibility. |
| risk-and-evidence-audit | Self-built from advisor-search risk controls | `.codex/skills/risk-and-evidence-audit/` | Evidence matrix, confidence, source dates, and risk cleanup. |
| outreach-auditor | Adapted from summer-research-agent human approval loop | `.codex/skills/outreach-auditor/` | Review outreach drafts before human approval. |

## Borrowed, Not Installed Verbatim

| Workflow | Local Adaptation |
|---|---|
| summer-research-agent | `workflows/90-borrowed-workflows.md`, `advisor-workflow-roles`, `outreach-auditor`, `application-crm` |
| flonat/claude-research | `docs/CONTEXT.md`, `docs/handoffs/`, `research-pilot-memory` |
| co-researcher | `workflows/07-critical-review-and-synthesis.md`, `academic-research-suite` |
| PaperPilot | `workflows/04-paper-evidence-protocol.md`, `paper-search`, `paper-reading-note` |
| Research-Pilot | `research-pilot-memory`, `templates/session-handoff.md` |
| mattpocock/skills | `grill-with-docs`, `handoff-manager`, `issue-slicer`, `statement-fit-review` |

## Explicitly Excluded For Now

| Item | Reason |
|---|---|
| paper-fetch / Sci-Hub fallback workflows | Legal and ethical risk; not needed for advisor search. |
| Huge generic skill packs | Too much noise for the current advisor-search objective. |
| Awesome-list repositories as runtime skills | Useful for browsing, but not actionable enough as installed skills. |
