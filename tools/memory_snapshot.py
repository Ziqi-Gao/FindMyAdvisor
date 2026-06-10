#!/usr/bin/env python3
"""Generate advisor memory snapshots from JSONL events."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

WARNING = "CSV trackers remain operational truth. Memory snapshots are generated read models, not source of truth."


def read_events(path: Path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_sources(path: Path):
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def write_markdown(path: Path, title: str, lines):
    body = [f"# {title}", "", f"Warning: {WARNING}", ""]
    body.extend(lines or ["- No entries."])
    path.write_text("\n".join(body) + "\n", encoding="utf-8")


def build_snapshots(events):
    current_state, next_actions, risks = [], [], []
    for event in events:
        label = f"{event['event_id']}: {event['summary']}"
        current_state.append(f"- {label}")
        for action in event.get("next_actions", []):
            next_actions.append(f"- {event['event_id']}: {action}")
        if event.get("risk_level") in {"medium", "high", "blocking"} or event.get("event_type") == "risk_added":
            risks.append(f"- {event['risk_level']}: {label}")
    return current_state, next_actions, risks


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate advisor memory snapshots.")
    parser.add_argument("--events", default="examples/memory/events.example.jsonl")
    parser.add_argument("--sources", default="examples/memory/sources.example.csv")
    parser.add_argument("--out", default=".advisor-memory/snapshots")
    args = parser.parse_args(argv)
    events = read_events(Path(args.events))
    read_sources(Path(args.sources))
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    current_state, next_actions, risks = build_snapshots(events)
    write_markdown(out_dir / "current-state.md", "Current State", current_state)
    write_markdown(out_dir / "next-actions.md", "Next Actions", next_actions)
    write_markdown(out_dir / "risk-register.md", "Risk Register", risks)
    snapshot = {
        "snapshot_id": "snapshot_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "generated_from_event_ids": [event["event_id"] for event in events],
        "read_model_warning": WARNING,
        "current_state": current_state,
        "next_actions": next_actions,
        "risk_register": risks,
    }
    (out_dir / "memory-snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"Generated memory snapshots in {out_dir} from {len(events)} events")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
