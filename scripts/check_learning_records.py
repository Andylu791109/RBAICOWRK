"""Check the structure and links of public learning records.

This does not determine whether a record is safe to publish or whether a
learner has improved. Those decisions require human review.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


RECORD_ID = re.compile(r"\d{8}-\d{3}\Z")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
KNOWLEDGE_ROW = re.compile(r"^\|\s*([a-z_]+)\s*\|\s*(.*?)\s*\|$")
NEEDED_FOR_COMPARISON = {
    "department", "task_type", "case_type", "task_goal", "final_status", "skill_evidence"
}


def record_fields(body: str) -> dict[str, str]:
    """Read the value column from the three-column learning report table."""
    fields: dict[str, str] = {}
    for line in body.splitlines():
        cells = line.split("|", 3)
        if len(cells) < 4 or cells[0].strip():
            continue
        key = cells[1].strip()
        if re.fullmatch(r"[a-z_]+", key):
            fields[key] = cells[3].rsplit("|", 1)[0].strip()
    return fields


def table_fields(body: str, pattern: re.Pattern[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in body.splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def required_record_fields(root: Path) -> set[str]:
    template = root / "templates" / "AI_LEARNING_REPORT_TEMPLATE.md"
    return set(record_fields(template.read_text(encoding="utf-8")))


def check(root: Path) -> tuple[list[str], int, int]:
    problems: list[str] = []
    record_ids: set[str] = set()
    expected = required_record_fields(root)
    record_files = sorted((root / "records").glob("*/*.md"))

    for path in record_files:
        fields = record_fields(path.read_text(encoding="utf-8"))
        label = path.relative_to(root).as_posix()
        missing = sorted(expected - fields.keys())
        if missing:
            problems.append(f"{label}: missing fields: {', '.join(missing)}")
        for name in expected & fields.keys():
            if not fields[name]:
                problems.append(f"{label}: empty {name}")
        for name in NEEDED_FOR_COMPARISON & fields.keys():
            if fields[name] == "未提供":
                problems.append(f"{label}: {name} is needed for later comparison")

        record_id = fields.get("record_id", "")
        if not RECORD_ID.fullmatch(record_id):
            problems.append(f"{label}: record_id must be YYYYMMDD-NNN")
        if path.stem != record_id:
            problems.append(f"{label}: filename does not match record_id")
        if record_id in record_ids:
            problems.append(f"{label}: duplicate record_id {record_id}")
        record_ids.add(record_id)
        if fields.get("learner_id", "") in {"", "未提供"}:
            problems.append(f"{label}: learner_id is needed for cross-period comparison")
        if not DATE.fullmatch(fields.get("used_at", "")):
            problems.append(f"{label}: used_at must be YYYY-MM-DD")
        if fields.get("reviewer_status", "") not in {"未驗收", "主管確認", "需重做"}:
            problems.append(f"{label}: invalid reviewer_status")

    knowledge_files = sorted((root / "knowledge").glob("*/*.md"))
    for path in knowledge_files:
        fields = table_fields(path.read_text(encoding="utf-8"), KNOWLEDGE_ROW)
        label = path.relative_to(root).as_posix()
        if fields.get("knowledge_id") != path.stem:
            problems.append(f"{label}: filename does not match knowledge_id")
        if fields.get("status") != "主管確認":
            problems.append(f"{label}: only supervisor-confirmed knowledge may be published")
        if not DATE.fullmatch(fields.get("reviewed_at", "")):
            problems.append(f"{label}: reviewed_at must be YYYY-MM-DD")
        if fields.get("reviewer_role", "") in {"", "待填"}:
            problems.append(f"{label}: reviewer_role is missing")
        sources = re.findall(r"\d{8}-\d{3}", fields.get("source_record_ids", ""))
        if not sources:
            problems.append(f"{label}: no source_record_ids")
        for source in sources:
            if source not in record_ids:
                problems.append(f"{label}: source record {source} does not exist")

    return problems, len(record_files), len(knowledge_files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (mainly for local fixture checks)",
    )
    args = parser.parse_args()
    problems, records, knowledge = check(args.root.resolve())
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"Structure OK: {records} records, {knowledge} knowledge entries")
    print("Human privacy and evidence review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
