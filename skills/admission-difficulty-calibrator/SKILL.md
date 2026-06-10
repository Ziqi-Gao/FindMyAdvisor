---
name: admission-difficulty-calibrator
description: Applicant-specific PhD admission difficulty and portfolio-balance skill. Use when Codex needs to estimate reach/target/moonshot difficulty, add a difficulty penalty to advisor or program fit, balance an application portfolio, compare programs beyond research fit, or decide whether a high-fit advisor is strategically worth applying to.
---

# Admission Difficulty Calibrator

## Purpose

Research fit is not admission probability. Use this skill to score how hard a specific advisor-program pair is for the applicant and to prevent a list of only ultra-reach programs.

## Inputs

- Applicant profile from `docs/CONTEXT.md`.
- Advisor fit from `data/advisors.csv` and dossiers.
- Program route from `data/programs.csv` or official admissions pages.
- Difficulty tracker: `data/program-difficulty.csv`.
- Source policy: `docs/source-policy.md`.

## Evidence Rules

- Label every important item as Fact, Inference, Unknown, or Risk lead.
- Prefer official program/admissions pages, faculty pages, department FAQs, public admissions statistics, and official dashboards.
- If acceptance rates are unavailable, mark `program_selectivity_signal=unknown` and use weak proxy signals only.
- Do not use undergraduate admission rates as PhD admission evidence.
- Do not equate ranking with probability. Ranking is only a weak selectivity proxy.
- Never say an applicant "cannot get in." Use portfolio labels: target, target-reach, reach, high-reach, moonshot.
- For funded PhD applications, do not call any program a true safety.

## Difficulty Factors

Score 0-10, where higher means harder for this applicant.

### 1. Program Selectivity

Use official admit rate if available.

- 9-10: ultra-selective top CS/AI/ML program or official admit rate below 5%.
- 8-9: top-tier selective program, or official admit rate around 5-10%.
- 7-8: strong R1 / top field program, or official admit rate around 10-20%.
- 5-7: solid R1 program with several plausible faculty and less extreme field congestion.
- Unknown: use 7 for strong CS/AI PhD, 6 for strong statistics/data-science PhD, then lower confidence.

### 2. Advisor Capacity And Gatekeeping

Add difficulty for:

- Unknown Fall 2027 capacity.
- Famous/highly visible lab with many applicants.
- Small junior lab with only a few slots.
- Faculty on leave, not recruiting, or no recent students.
- Rotation/program-level admission where advisor fit has less direct leverage.

Reduce difficulty for:

- Current official "recruiting PhD students" statement.
- Faculty says they review applications mentioning their name.
- Multiple active students in the exact area.
- Public funding/lab activity signal, without treating funding as slot guarantee.

If a faculty page says they are not accepting students, archive or defer; do not merely apply a penalty.

### 3. Applicant-Program Match

Increase difficulty when:

- Applicant profile has a visible weakness for that program, such as GPA/test/prerequisite concern.
- The target field is a pivot without strong evidence or recommenders.
- The route requires a statement style that conflicts with the applicant's best evidence.
- English/GRE/admin requirements create risk.

Reduce difficulty when:

- There is a public paper/preprint directly matching the advisor's current work.
- The applicant has a strong recommender in the target discipline.
- The applicant has prior collaboration, reply, interview, or strong faculty-specific hook.
- The program values interdisciplinary quantitative backgrounds and the applicant's profile fits that route.

### 4. Field Congestion

Add difficulty for saturated topics:

- LLM interpretability, mechanistic interpretability, AI safety, foundation models, and top NLP/ML labs in elite CS programs.
- Small theory groups where slots are scarce.

Reduce difficulty only when the applicant has unusually specific evidence, such as a directly related paper, tool, or collaborator.

## Portfolio Labels

Use both `difficulty_score` and evidence confidence.

- `moonshot`: 9.0-10.0. Apply only if the fit is unusually strong or strategic.
- `high-reach`: 8.0-8.9. Keep sparingly; needs strong hook.
- `reach`: 7.0-7.9. Good fit but competitive.
- `target-reach`: 6.0-6.9. Plausible if materials are strong.
- `target`: 4.5-5.9. Reasonable relative to profile, still not safe.
- `fit-probe`: below 4.5. Use for low-cost exploratory programs, not as a guarantee.

## Adjustment Rule

Keep `fit_score` separate from `difficulty_score`.

Recommended fields:

- `fit_score`: research match.
- `difficulty_score`: applicant-specific admission difficulty.
- `difficulty_tier`: target, target-reach, reach, high-reach, moonshot.
- `adjusted_priority`: apply, maybe, defer, archive.
- `penalty_reasons`: why difficulty is high.
- `positive_offsets`: why the applicant still has a plausible path.

Guideline:

- A high fit plus moonshot difficulty can remain on the list, but should not dominate the portfolio.
- A lower fit with lower difficulty is not automatically better; weak research fit should still be filtered out.
- A strong portfolio normally needs a mix of high-reach, reach, target-reach, and target programs.

## Procedure

1. Read `docs/CONTEXT.md`, `docs/source-policy.md`, and the relevant advisor/program dossier.
2. Check official admissions route, contact policy, funding language, GRE/English requirements, and any public admit-rate data.
3. Score difficulty with explicit facts, inferences, unknowns, and risk leads.
4. Update `data/program-difficulty.csv`.
5. If the score changes advisor strategy, update `data/advisors.csv` next action, not the raw fit score.
6. Summarize portfolio balance and recommend next programs to fill gaps.

## Output

- Difficulty table by advisor-program pair.
- Penalty reasons and positive offsets.
- Portfolio bucket recommendation.
- Unknowns requiring official verification.
- Next action: apply, audit, paper card, outreach draft, defer, or archive.
