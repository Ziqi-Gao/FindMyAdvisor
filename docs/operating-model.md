# Operating Model

## Primary Objective

Find and validate strong PhD advisor and program fit for the 2027 Fall cycle in CS, Statistics, Biostatistics, and interdisciplinary areas.

## Working Roles

- Applicant: makes final decisions, approves outreach, supplies personal materials.
- Codex researcher: gathers public evidence, builds dossiers, drafts reports, updates trackers.
- Auditor: checks source quality, hallucination risk, and unsupported claims.
- Human reviewer: approves shortlist changes, outreach, and final application choices.

## Candidate States

- discovered: found but not screened.
- screened: basic fit and source check complete.
- dossier-ready: enough evidence for a faculty dossier.
- outreach-ready: dossier is strong and email angle is specific.
- contacted: email sent by human.
- replied: response received and summarized.
- archived: removed with a reason.
- priority: active high-value target.

## Decision Rules

A candidate can become priority only when:

- Research fit is supported by at least two sources.
- The program/admissions path is known or marked as an important unknown.
- Recent activity exists or the lack of it is explained.
- Funding and availability have been checked when relevant.
- Risks and unknowns are written down.

Archive candidates when:

- The fit is too weak.
- The faculty member is not in a relevant PhD-granting path.
- Recent activity cannot be found after reasonable checking.
- Program constraints make the application impractical.

## Persistent Advisor Memory

CSV trackers are operational truth. Memory events are an append-only audit trail that explains how and why advisor, program, evidence, outreach, and decision state changed. Memory snapshots are generated read models for session resume and are not the source of truth.

Use memory after meaningful changes. Important decisions should include source IDs, confidence, risk level, and next actions.

## Maintenance Rule

Every meaningful change should update one of: CSV trackers, memory events, dossier files, handoff files, or weekly review notes. When memory events are created, list their event IDs in the handoff.
