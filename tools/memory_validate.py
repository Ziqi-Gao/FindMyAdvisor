#!/usr/bin/env python3
"""Validate advisor memory JSONL files."""
from __future__ import annotations

import argparse
import csv
import json
import sys
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
REQUIRED = ["event_id", "timestamp", "actor", "event_type", "object_type", "object_id", "faculty_id", "program_id", "claim_ids", "source_ids", "summary", "before", "after", "evidence_note", "confidence", "risk_level", "next_actions", "files_touched", "human_approval_required", "human_approved"]
CONFIDENCE = {"low", "medium", "high", "unknown"}
RISK_LEVELS = {"none", "low", "medium", "high", "blocking", "unknown"}
RISK_QUERY_LEVELS = {"medium", "high", "blocking", "unknown"}


def load_events(path: Path):
    events = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                events.append((line_number, json.loads(line)))
    return events


def load_source_ids(path: Path | None):
    if path is None or not path.exists():
        return None
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row["source_id"] for row in csv.DictReader(handle) if row.get("source_id")}


def fallback_validate(events, source_ids=None):
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
        if event.get("actor") not in ACTORS:
            errors.append(f"line {line_number}: invalid actor {event.get('actor')}")
        if event.get("object_type") not in OBJECT_TYPES:
            errors.append(f"line {line_number}: invalid object_type {event.get('object_type')}")
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
        if event.get("event_type") in {"outreach_approved", "outreach_sent"}:
            if not event.get("human_approval_required"):
                errors.append(f"line {line_number}: {event.get('event_type')} requires human_approval_required=true")
            if not event.get("human_approved"):
                errors.append(f"line {line_number}: {event.get('event_type')} requires human_approved=true")
        if source_ids is not None:
            for source_id in event.get("source_ids", []):
                if source_id not in source_ids:
                    errors.append(f"line {line_number}: missing source_id {source_id} in sources CSV")
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
    parser.add_argument("--sources", default="examples/memory/sources.example.csv")
    args = parser.parse_args(argv)
    try:
        events = load_events(Path(args.events))
        source_ids = load_source_ids(Path(args.sources) if args.sources else None)
        errors = jsonschema_validate(events, Path(args.schema))
        errors = fallback_validate(events, source_ids) if errors is None else errors + fallback_validate(events, source_ids)
    except Exception as exc:
        print(f"memory validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    source_note = f" with sources from {args.sources}" if source_ids is not None else ""
    print(f"Validated {len(events)} memory events from {args.events}{source_note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
