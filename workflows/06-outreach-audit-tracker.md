# Outreach Audit And Tracker Workflow

Adapted from summer-research-agent human approval and tracker patterns.

## Rules

- Draft only for A-tier or strong B-tier candidates.
- Never send automatically.
- Every factual sentence must trace to the dossier or applicant profile.
- Keep outreach short and specific.
- Ask one useful question, not many.

## Procedure

1. Confirm the candidate has a dossier.
2. Draft from `templates/outreach-draft.md`.
3. Audit claims with `outreach-auditor`.
4. Mark approval status in `data/outreach.csv`.
5. Only the human sends the email.
6. Track follow-up and reply status.

## Approval States

- draft-needed
- drafted
- needs-evidence
- human-approved
- sent
- replied
- closed
