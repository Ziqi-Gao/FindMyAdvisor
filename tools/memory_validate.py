#!/usr/bin/env python3
"""Validate advisor memory JSONL files."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

EVENT_TYPES = {
    "applicant_profile_updated", "search_batch_started", "faculty_discovered", "faculty_screened", "faculty_archived",
    "faculty_priority_changed", "dossier_created", "dossier_updated", "evidence_added", "evidence_revised",
    "risk_added", "risk_resolved", "program_requirement_checked", "funding_checked", "paper_reading_note_added",
    "outreach_drafted", "outreach_audited", "outreach_approved", "outreach_sent", "reply_received",
    "meeting_logged", "decision_made", "weekly_review_completed", "handoff_written",
}
REQUIRED = ["event_id", "timestamp", "actor", "event_type", "object_type", "object_id", "faculty_id", "program_id", "claim_ids", "source_ids", "summary", "before", "after", "evidence_note", "confidence", "risk_level", "next_actions", "files_touched", "human_approval_required", "human_approved"]
CONFIDENCE = {"low", "medium", "high", "unknown"}
RISK_LEVELS = {"none", "low", "medium", "high", "blocking"}


def load_events(path: Path):
    events = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                events.append((line_number, json.loads(line)))
    return events


def fallback_validate(events):
    errors = []
    seen = set()
    for line_number, event in events:
        for field in REQUIRED:
            if field not in event:
                errors.append(f"line {line_number}: missing {field}")
        event_id = event.get("event_id")
        if event_id in seen:
            errors.append(f"line {line_number}: duplicate event_id {event_id}")
        seen.add(event_id)
        if event.get("event_type") not in EVENT_TYPES:
            errors.append(f"line {line_number}: invalid event_type {event.get('event_type')}")
        if event.get("confidence") not in CONFIDENCE:
            errors.append(f"line {line_number}: invalid confidence {event.get('confidence')}")
        if event.get("risk_level") not in RISK_LEVELS:
            errors.append(f"line {line_number}: invalid risk_level {event.get('risk_level')}")
        for name in ["claim_ids", "source_ids", "next_actions", "files_touched"]:
            if name in event and not isinstance(event[name], list):
                errors.append(f"line {line_number}: {name} must be an array")
        for name in ["before", "after"]:
            if name in event and not isinstance(event[name], dict):
                errors.append(f"line {line_number}: {name} must be an object")
        for name in ["human_approval_required", "human_approved"]:
            if name in event and not isinstance(event[name], bool):
                errors.append(f"line {line_number}: {name} must be boolean")
        if event.get("event_type") in {"outreach_approved", "outreach_sent"} and not event.get("human_approved"):
            errors.append(f"line {line_number}: {event.get('event_type')} requires human_approved=true")
    return errors


def jsonschema_validate(events, schema_path: Path):
    try:
        import jsonschema  # type: ignore
    except Exception:
        return None
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)
    errors = []
    for line_number, event in events:
        for error in validator.iter_errors(event):
            location = ".".join(str(part) for part in error.path) or "<root>"
            errors.append(f"line {line_number}: {location}: {error.message}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate advisor memory event JSONL.")
    parser.add_argument("--events", default="examples/memory/events.example.jsonl")
    parser.add_argument("--schema", default="schemas/memory-event.schema.json")
    args = parser.parse_args(argv)
    try:
        events = load_events(Path(args.events))
        errors = jsonschema_validate(events, Path(args.schema))
        errors = fallback_validate(events) if errors is None else errors + fallback_validate(events)
    except Exception as exc:
        print(f"memory validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(events)} memory events from {args.events}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
