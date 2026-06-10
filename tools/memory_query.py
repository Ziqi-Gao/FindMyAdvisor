#!/usr/bin/env python3
"""Query advisor memory events."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_events(path: Path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def print_event(event):
    faculty = event.get("faculty_id") or "-"
    print(f"{event['timestamp']} {event['event_id']} {event['event_type']} faculty={faculty} :: {event['summary']}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Query advisor memory events.")
    parser.add_argument("command", choices=["recent", "faculty", "risks", "next-actions"])
    parser.add_argument("--events", default="examples/memory/events.example.jsonl")
    parser.add_argument("--faculty-id")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)
    events = read_events(Path(args.events))
    if args.command == "recent":
        for event in events[-args.limit:]:
            print_event(event)
    elif args.command == "faculty":
        if not args.faculty_id:
            parser.error("faculty command requires --faculty-id")
        for event in events:
            if event.get("faculty_id") == args.faculty_id:
                print_event(event)
    elif args.command == "risks":
        for event in events:
            if event.get("risk_level") in {"medium", "high", "blocking"} or event.get("event_type") == "risk_added":
                print_event(event)
    elif args.command == "next-actions":
        for event in events:
            for action in event.get("next_actions", []):
                print(f"{event['event_id']}: {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
