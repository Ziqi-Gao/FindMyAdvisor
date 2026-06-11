# Application Difficulty And Portfolio Workflow

Use after an advisor longlist or dossier batch. This workflow adds applicant-specific admission difficulty without overwriting research fit.

## Role Ownership

This workflow is owned by the `Difficulty Calibrator` role from the installed `advisor-batch-agent-roles` project skill.

The Difficulty Calibrator may gather evidence and recommend rows, but the CRM Tracker remains the single writer for `data/program-difficulty.csv`.

## Inputs

- `docs/CONTEXT.md`
- `docs/source-policy.md`
- `data/advisors.csv`
- `data/faculty-index.csv`
- `data/programs.csv`
- `data/program-difficulty.csv`
- Advisor dossiers and program-requirements audits

## Procedure

1. For each advisor-program pair, identify the real admissions route: direct advisor, rotation, committee, program-level, or unknown.
2. Record official evidence for deadline, GRE/English rules, funding language, faculty contact policy, and any public admission-rate statistics.
3. Score applicant-specific difficulty using `admission-difficulty-calibrator`.
4. Keep `fit_score` and `difficulty_score` separate.
5. Mark a portfolio bucket: target, target-reach, reach, high-reach, or moonshot.
6. Update `data/program-difficulty.csv`.
7. If a program is moonshot/high-reach, require a paper-card-backed hook before spending outreach/application effort.
8. If the portfolio has too many high-reach/moonshot programs, launch a search batch for strong-fit target-reach programs.
9. Rebuild the composite score table and ranked master table after difficulty changes.
10. Run the validation gate from `advisor-batch-agent-roles`.

## Output

- Program difficulty table.
- Penalty reasons and positive offsets.
- Portfolio mix summary.
- Recommended next search batch.

## Rule

No funded PhD program is a true safety. Use "target" or "target-reach" instead.

Unknown admissions path is a penalty, not a neutral value. Do not silently treat unknown route or unknown capacity as acceptable.
