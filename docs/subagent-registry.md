# Subagent Registry

Date created: 2026-06-10

Purpose: keep long-running advisor-search subagents reusable instead of opening new agents for every batch.

## Rule

Use this registry before spawning any new subagent.

Default policy:

```text
reuse existing role agent -> resume/send input -> wait only when needed -> close only when truly obsolete
```

If the current tool session cannot enumerate existing agents, do not spawn a replacement automatically. Use the known agent IDs from recent notifications, ask the user for missing IDs if needed, or continue locally until an existing agent can be resumed.

## Stable Role Pool

| Role | Preferred Use | Reuse Rule | Writes Files? |
|---|---|---|---|
| Batch Lead | Batch charter, final decision, final synthesis. | Main agent only. | Yes. |
| Scout-CS | CS/NLP/ML discovery lanes. | Reuse for all CS discovery prompts. | No. |
| Scout-Stats | Statistics/data science/biostat bridge lanes. | Reuse for all stats bridge prompts. | No. |
| Filter | Keep/defer/reject review. | Reuse for every batch's filtering pass. | No. |
| Source Auditor | Source verification and claim labels. | Reuse for source/audit passes. | No. |
| Paper Reader | Paper cards and paper-specific hooks. | Reuse; assign one paper set at a time. | No. |
| Difficulty Calibrator | Program/advisor difficulty evidence. | Reuse for difficulty and route audits. | No. |
| QA Auditor | CSV/ranking/report validation. | Reuse after CRM writes. | No. |
| CRM Tracker | Canonical CSV updates. | Main agent unless a disjoint write scope is explicitly assigned. | Yes, single writer. |
| Copywriter | Outreach drafts after approval. | Dormant until user approval. | No automatic sending. |

## Named UI Role Assignments

These assignments come from the visible Codex subagent panel screenshot provided on 2026-06-10. The screenshot shows nicknames but not tool-call agent IDs. Treat these as stable nickname-level assignments until IDs are available.

The screenshot shows 15 visible reusable subagents. Together with the two previously recorded closed agents, the registry now tracks 17 known subagent records.

| Nickname | Stable Role | Primary Module | Default Batch Assignment | Writes Files? |
|---|---|---|---|---|
| Mencius | Portfolio Strategist | Batch scope, portfolio balance, final keep/defer challenge. | Review the batch charter and check whether the candidate mix improves reach/target balance. | No |
| Dirac | Scout-CS Core | Mechanistic interpretability, LLM representations, activation steering, AI safety. | Find CS/NLP/ML faculty with direct RAPTOR-style fit. | No |
| Newton | Difficulty Calibrator | Application difficulty, program tier, penalty reasons. | Estimate difficulty buckets and positive offsets for serious candidates. | No |
| Fermat | Quant QA Auditor | Score consistency, rank sanity, duplicate checks. | Check composite-score logic, missing rows, duplicate IDs, and rank continuity. | No |
| Curie | Scout-Stats | Statistics, data science, biostatistics-method bridge. | Find statistics/theory candidates with high-dimensional or reliable-ML overlap. | No |
| Leibniz | Paper Reader | Paper-specific hooks and theory links. | Read recent papers and produce concise paper-hook notes. | No |
| Aquinas | Filter | Fit threshold, source threshold, ethical/source-policy gate. | Decide keep/defer/reject with reasons before CRM entry. | No |
| Beauvoir | Advising Risk Auditor | Lab culture, student outcomes, inclusion, mentoring signals. | Check student/lab pages and flag advising/culture unknowns or risks. | No |
| Helmholtz | Funding Auditor | NSF/NIH/industry grants, lab vitality, availability signals. | Collect funding and lab-capacity evidence. | No |
| Harvey | Program Route Auditor | Admissions route, contact policy, PhD program structure. | Verify direct advisor/rotation/committee/program-level path and contact rules. | No |
| Carson | Target-Reach Scout | Less obvious but plausible target/target-reach programs. | Search beyond elite clusters for strong-fit, more balanced programs. | No |
| Nietzsche | Contrarian Reviewer | Overclaim, prestige bias, weak fit, redundancy. | Argue against weak additions and identify false positives. | No |
| Russell | Evidence Logic Auditor | Fact/inference/unknown consistency and source reasoning. | Check whether claims in reports and rows are source-backed. | No |
| Anscombe | Contact Policy Auditor | Outreach eligibility and human-approval gate. | Verify no-email rules, contact norms, and whether outreach is premature. | No |
| Peirce | Citation Expansion Scout | Coauthor/citation trails, neighboring faculty, abductive leads. | Expand from strong papers/labs into adjacent faculty leads. | No |

The main agent remains Batch Lead and CRM Tracker unless an explicit disjoint write scope is assigned. This preserves the single-writer rule.

## Active/Reusable Agents

Fill this table whenever a subagent is created, resumed, or completed. Do not rely on memory alone.

| Agent ID | Nickname | Stable Role | Status | Last Assigned Task | Last Result/Handoff | Reuse Notes |
|---|---|---|---|---|---|---|
| `019eb38c-9e0c-7d51-9fc0-5499711080a8` | Socrates | QA / Quality Gate Auditor | closed | Read workflow files and identify batch quality gates. | Incorporated into `skills/advisor-batch-agent-roles/` and workflow updates. | Reopen only if thread resume is useful and available. |
| `019eb38c-9f4b-75d3-b950-f1e20e9812cf` | Dewey | Role Design Auditor | closed | Propose fixed multi-agent role split. | Incorporated into `skills/advisor-batch-agent-roles/`. | Reopen only if thread resume is useful and available. |
| unknown | Mencius | Portfolio Strategist | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Dirac | Scout-CS Core | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Newton | Difficulty Calibrator | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Fermat | Quant QA Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Curie | Scout-Stats | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Leibniz | Paper Reader | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Aquinas | Filter | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Beauvoir | Advising Risk Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Helmholtz | Funding Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Harvey | Program Route Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Carson | Target-Reach Scout | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Nietzsche | Contrarian Reviewer | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Russell | Evidence Logic Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Anscombe | Contact Policy Auditor | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |
| unknown | Peirce | Citation Expansion Scout | visible in UI | Not yet assigned through tool layer. | Nickname captured from screenshot. | Add tool-call agent ID when available. |

## Default Large-Batch Fanout

For a substantial advisor-search batch, use this ordering:

1. Main agent writes the batch charter and checks this registry.
2. Dirac, Curie, Carson, and Peirce scout independent lanes.
3. Harvey, Helmholtz, Beauvoir, and Newton collect route, funding, advising, and difficulty evidence for promising leads.
4. Aquinas and Nietzsche filter weak or strategically redundant leads.
5. Russell audits source labels and claim logic.
6. Leibniz reads papers only for candidates that survive filtering.
7. Fermat validates CSV/ranking consistency after the main agent writes CRM updates.
8. Mencius reviews portfolio balance and next-batch direction.

Do not use all agents for tiny tasks. Use all visible agents only when the batch is large enough to avoid duplicate work.

## Assignment Template

When reusing a subagent, use a bounded prompt:

```text
Resume your stable role: <role>.
Batch: <batch id/topic>.
Read: <files or URLs>.
Task: <one concrete task>.
Return: <artifact shape>.
Do not edit files unless explicitly assigned.
Do not duplicate work assigned to <other role>.
```

## Spawn Gate

Spawn a new subagent only when all are true:

- No existing registered agent can handle the role.
- The task is independent and materially advances the batch.
- The task does not require immediate next-step blocking context.
- The write scope is read-only or explicitly disjoint.
- The new agent is added to this registry immediately.

## Close Gate

Close an agent only when:

- Its result has been integrated into a report, CSV, handoff, or decision log.
- Its stable role is no longer useful for the current workflow.
- The registry row has been updated with the final result and reuse note.
