#!/usr/bin/env python3
"""Append one event to a private advisor memory JSONL file."""
from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

ACTORS = {"Codex", "User", "Applicant", "Human reviewer", "Subagent", "Automation", "System"}
OBJECT_TYPES = {
    "applicant_profile", "search_batch", "faculty", "program", "evidence", "risk", "dossier", "paper",
    "funding", "program_requirement", "outreach", "reply", "meeting", "decision", "weekly_review", "handoff",
    "source", "snapshot",
}
EVENT_TYPES = {
    "applicant_profile_updated", "search_batch_started", "faculty_discovered", "faculty_screened", "faculty_archived",
    "faculty_priority_changed", "dossier_created", "dossier_updated", "evidence_added", "evidence_revised",
    "risk_added", "risk_resolved", "program_requirement_checked", "funding_checked", "paper_reading_note_added",
    "outreach_drafted", "outreach_audited", "outreach_approved", "outreach_sent", "reply_received",
    "meeting_logged", "decision_made", "weekly_review_completed", "handoff_written",
}
RISK_LEVELS = ["none", "low", "medium", "high", "blocking", "unknown"]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Append an advisor memory event.")
    parser.add_argument("--events", default=".advisor-memory/events.jsonl")
    parser.add_argument("--event-type", required=True, choices=sorted(EVENT_TYPES))
    parser.add_argument("--object-type", required=True, choices=sorted(OBJECT_TYPES))
    parser.add_argument("--object-id", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--actor", choices=sorted(ACTORS), default="Codex")
    parser.add_argument("--faculty-id")
    parser.add_argument("--program-id")
    parser.add_argument("--claim-id", action="append", default=[])
    parser.add_argument("--source-id", action="append", default=[])
    parser.add_argument("--evidence-note", default="")
    parser.add_argument("--confidence", choices=["low", "medium", "high", "unknown"], default="medium")
    parser.add_argument("--risk-level", choices=RISK_LEVELS, default="none")
    parser.add_argument("--next-action", action="append", default=[])
    parser.add_argument("--file-touched", action="append", default=[])
    parser.add_argument("--human-approval-required", action="store_true")
    parser.add_argument("--human-approved", action="store_true")
    args = parser.parse_args(argv)
    if args.human_approved and not args.human_approval_required:
        raise SystemExit("human approval cannot be marked approved unless approval was required")
    if args.event_type in {"outreach_approved", "outreach_sent"} and (not args.human_approval_required or not args.human_approved):
        raise SystemExit(f"{args.event_type} requires --human-approval-required and --human-approved")
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    event = {
        "event_id": "evt_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "_" + uuid.uuid4().hex[:8],
        "timestamp": now,
        "actor": args.actor,
        "event_type": args.event_type,
        "object_type": args.object_type,
        "object_id": args.object_id,
        "faculty_id": args.faculty_id,
        "program_id": args.program_id,
        "claim_ids": args.claim_id,
        "source_ids": args.source_id,
        "summary": args.summary,
        "before": {},
        "after": {},
        "evidence_note": args.evidence_note,
        "confidence": args.confidence,
        "risk_level": args.risk_level,
        "next_actions": args.next_action,
        "files_touched": args.file_touched,
        "human_approval_required": bool(args.human_approval_required),
        "human_approved": bool(args.human_approved),
    }
    path = Path(args.events)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, separators=(",", ":")) + "\n")
    print(event["event_id"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
