---
name: advisor-batch-agent-roles
description: Fixed multi-agent advisor-search batch workflow for 2027 Fall PhD applications. Use when Codex needs to run advisor discovery batches, assign Scout/Filter/Auditor/Difficulty/Tracker/QA roles, use parallel subagents safely, enforce evidence gates, update CRM files, rebuild composite rankings, or write batch reports and handoffs.
---

# Advisor Batch Agent Roles

Use this skill for every advisor-search batch. The operating principle is:

> Many readers, one judge, one writer.

Parallel agents may gather evidence, but the Batch Lead owns final decisions and the CRM Tracker is the only writer to the core CSV files.

Before using any subagent, read `docs/subagent-registry.md`. Reuse registered agents whenever possible. Do not spawn a new subagent just because a task is new; first check whether an existing role agent can be resumed or sent a new bounded assignment. For large batches, use the registry's named UI role assignments and default fanout before inventing any new role.

## Fixed Roles

| Role | Ownership | Editing Rule | Required Output |
|---|---|---|---|
| Batch Lead | Batch scope, role assignment, final keep/defer decisions, final ranking interpretation. | Usually main agent. | Batch charter, final synthesis, handoff. |
| Scout-CS | CS/NLP/ML candidate discovery from public sources. | Read-only. | Candidate leads with source URLs and rough fit. |
| Scout-Stats | Statistics, data science, and method-oriented biostat bridge discovery. | Read-only. | Candidate leads with route and method-fit notes. |
| Filter | Removes weak, stale, off-route, duplicate, or strategically redundant leads. | Read-only. | Keep/defer/reject table with reasons. |
| Source Auditor | Verifies claims as Fact, Inference, Unknown, or Risk lead. Checks name collisions, stale pages, bad links, and unsupported claims. | Read-only. | Audit notes with confidence and blocking unknowns. |
| Paper Reader | Reads one concrete recent paper when a candidate needs a paper-specific hook. | Read-only. | Paper card or concise hook note. |
| Difficulty Calibrator | Scores applicant-specific program/advisor difficulty and portfolio bucket. | Read-only by default. | Difficulty row recommendation with penalty reasons and positive offsets. |
| CRM Tracker | Updates `data/advisors.csv`, `data/faculty-index.csv`, `data/evidence-matrix.csv`, and `data/program-difficulty.csv`. | Single writer. | Deduplicated CSV updates. |
| QA Auditor | Validates CSV parseability, duplicate keys, rank continuity, and report completeness. | Read-only by default. | Validation result and blocking issues. |
| Copywriter | Drafts outreach only after audit, paper read, contact-policy check, and explicit user approval. | No automatic sending. | Draft plus rationale and missing evidence. |

## Parallel Agent Protocol

1. Start locally with a batch charter: theme, target size, target difficulty mix, search lane, and exclusions.
2. Read `docs/subagent-registry.md` and identify reusable role agents.
3. Prefer `resume` or `send input` to existing agents over spawning new agents.
4. Spawn a new subagent only if the registry has no suitable agent and the spawn gate in `docs/subagent-registry.md` passes.
5. Give each subagent one role, one scope, and one expected artifact.
6. Do not assign overlapping write scopes. Keep file writes in the main thread unless a disjoint write scope is explicitly assigned.
7. Use parallel subagents for separate scouting lanes, publication recency checks, funding/admissions evidence, paper-card extraction, and first-pass risk scans.
8. Keep final scoring, deduplication, CRM writes, shortlist decisions, outreach approval, and final handoff in the main thread.
9. Update `docs/subagent-registry.md` when an agent is created, resumed, completed, or closed.
10. If subagents are unavailable or their IDs are not visible to the current tool session, continue locally or ask for the missing IDs; do not open replacement agents automatically.

## Batch Quality Gates

Do not mark a batch complete unless these gates pass.

### Gate 1: Required Context

Read before searching:

- `AGENTS.md`
- `docs/CONTEXT.md`
- `docs/source-policy.md`
- `docs/subagent-registry.md`
- relevant workflow files
- recent batch reports and `docs/advisor-search-status-2026-06-10.md`

### Gate 2: Minimum Candidate Evidence

Every candidate entering the CRM must have:

- An official faculty, department, program, or lab source.
- At least one recent publication, lab/student activity, grant/funding, or admissions/prospective-student signal.
- Source URLs recorded in the row.
- A fit rationale tied to the applicant profile: RAPTOR, LLM interpretability/control/reliability, high-dimensional statistical learning, trustworthy ML, or a clearly marked statistics/biostat bridge.
- Important claims labeled or phrased as Fact, Inference, Unknown, or Risk lead.

Defer instead of adding when:

- The only evidence is social media, anonymous reputation, or search snippets.
- The page is stale and no recent paper/lab/grant signal rescues the fit.
- The role or PhD-advising path is unclear.
- The candidate duplicates a stronger same-school/same-area candidate.
- A source appears compromised or unrelated.

### Gate 3: CRM Completeness

Every newly added serious candidate must have:

- One row in `data/advisors.csv`.
- One canonical row in `data/faculty-index.csv`.
- At least two rows in `data/evidence-matrix.csv`: `research_fit` and `admissions_capacity`.
- One row in `data/program-difficulty.csv`, unless explicitly running a pre-CRM discovery batch.
- A next action: dossier, paper card, route audit, defer, or archive.

Use stable IDs:

- `faculty_id`: lowercase hyphenated name, disambiguated if needed.
- `program_id`: lowercase school/program/faculty route, disambiguated if needed.

### Gate 4: Difficulty And Ranking

- Keep `fit_score` and `difficulty_score` separate.
- Every serious candidate gets a bucket: target, target-reach, reach, high-reach, or moonshot.
- No funded PhD program is a true safety.
- High-reach or moonshot candidates need a paper-card-backed hook before outreach or serious application effort.
- Rebuild `data/advisor-composite-scores.csv` and `docs/advisor-ranked-master-table.md` after CRM updates.
- User-facing rank order must follow `composite_score = positive_score - penalty_score`.

### Gate 5: Report And Handoff

For every substantial batch, write:

- Batch report: `docs/advisor-search-batch-###-topic.md`
- Updated `docs/CONTEXT.md` if durable state changes
- Updated `docs/advisor-search-status-2026-06-10.md` if counts, rankings, or priorities change
- Handoff: `docs/handoffs/YYYY-MM-DD-topic.md`

Batch report must include:

- Batch brief
- Added candidates
- Deferred or rejected candidates when applicable
- Evidence notes
- Risk and unknowns
- Ranking impact
- Next actions

### Gate 6: Validation

Before final response, validate:

- CSV files parse successfully.
- Counts match expected rows.
- No duplicate `(faculty_name, university)` in `data/advisors.csv`.
- No duplicate `faculty_id` in `data/faculty-index.csv`.
- No duplicate `faculty_id` in `data/program-difficulty.csv`.
- No duplicate `(faculty_id, criterion)` in `data/evidence-matrix.csv`.
- Composite ranks are continuous.
- New candidates appear in `data/advisor-composite-scores.csv`.

## Outreach Rule

Never send outreach automatically. Draft only after:

- Source audit passes.
- One paper-specific hook is read.
- Contact policy is checked.
- The user explicitly approves drafting.
