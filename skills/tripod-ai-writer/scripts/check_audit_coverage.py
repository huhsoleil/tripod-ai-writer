#!/usr/bin/env python3
"""Check a TRIPOD+AI audit for coverage and internal consistency.

Usage:
    python scripts/check_audit_coverage.py tripod_ai_checklist.md [issues_to_resolve.md]

Checks
  1. Every TRIPOD+AI audit unit (52 main: 1-27c; 13 abstract: A1-A13) has
     exactly one row in the output checklist.
  2. Every row carries exactly one valid status.
  3. Rows marked "Partially reported", "Not reported", or "Cannot determine"
     cite at least one issue ID.
  4. Rows marked "Not applicable" carry some justification text.
  5. (If the issues file is given) every issue ID cited in the checklist is
     defined in the issues file, and the gate status line matches the number
     of unresolved Critical issues.

Only the Python standard library is used. Exit code 0 = pass, 1 = problems.
"""

import re
import sys
from pathlib import Path

MAIN_UNITS = [
    "1", "2", "3a", "3b", "3c", "4", "5a", "5b", "6a", "6b", "6c", "7",
    "8a", "8b", "8c", "9a", "9b", "9c", "10", "11",
    "12a", "12b", "12c", "12d", "12e", "12f", "12g",
    "13", "14", "15", "16", "17",
    "18a", "18b", "18c", "18d", "18e", "18f", "19",
    "20a", "20b", "20c", "21", "22", "23a", "23b", "24",
    "25", "26", "27a", "27b", "27c",
]
ABSTRACT_UNITS = [f"A{i}" for i in range(1, 14)]
ALL_UNITS = set(MAIN_UNITS) | set(ABSTRACT_UNITS)

STATUSES = [
    "Adequately reported",
    "Partially reported",
    "Not reported",
    "Not applicable",
    "Cannot determine",
]
NEEDS_ISSUE = {"Partially reported", "Not reported", "Cannot determine"}
ISSUE_RE = re.compile(r"\b(C|M|m|IR)-\d{2,}\b")


def parse_rows(text):
    """Yield (unit_id, cells, raw_line) for table rows whose first cell is an audit unit."""
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells:
            continue
        first = cells[0].strip("*` ")
        if first in ALL_UNITS:
            yield first, cells, s


def check_checklist(path):
    text = Path(path).read_text(encoding="utf-8")
    problems, seen, cited = [], {}, set()

    for unit, cells, raw in parse_rows(text):
        seen.setdefault(unit, 0)
        seen[unit] += 1
        found = [st for st in STATUSES if any(c == st or c.startswith(st) for c in cells)]
        if len(found) != 1:
            problems.append(f"{unit}: expected exactly one status, found {found or 'none'}")
            continue
        status = found[0]
        ids = set(m.group(0) for m in ISSUE_RE.finditer(raw))
        cited |= ids
        if status in NEEDS_ISSUE and not ids:
            problems.append(f"{unit}: status '{status}' but no issue ID cited")
        if status == "Not applicable":
            other = [c for c in cells[1:] if c and c not in STATUSES
                     and c not in ("D", "E", "D;E") and not c.startswith("(")]
            if len(" ".join(other)) < 10:
                problems.append(f"{unit}: 'Not applicable' without justification")

    for unit in MAIN_UNITS + ABSTRACT_UNITS:
        n = seen.get(unit, 0)
        if n == 0:
            problems.append(f"{unit}: missing from checklist")
        elif n > 1:
            problems.append(f"{unit}: appears {n} times")

    covered_main = sum(1 for u in MAIN_UNITS if seen.get(u))
    covered_abs = sum(1 for u in ABSTRACT_UNITS if seen.get(u))
    return problems, cited, text, (covered_main, covered_abs)


def check_issues(path, cited, checklist_text):
    text = Path(path).read_text(encoding="utf-8")
    problems = []
    defined = set(m.group(0) for m in ISSUE_RE.finditer(text))
    for i in sorted(cited - defined):
        problems.append(f"issue {i} cited in checklist but not defined in {Path(path).name}")

    # Unresolved Critical issues: '### C-xx' blocks whose Status line is not 'Resolved'
    unresolved = 0
    blocks = re.split(r"^###\s+", text, flags=re.M)
    for b in blocks:
        m = re.match(r"(C-\d{2,})", b)
        if not m:
            continue
        st = re.search(r"Status:\s*([^\n]+)", b)
        status = st.group(1).strip() if st else "Unresolved"
        if not status.startswith("Resolved"):
            unresolved += 1

    for name, t in (("issues file", text), ("checklist", checklist_text)):
        g = re.search(r"Gate status:\s*([^\n]+)", t)
        if not g:
            problems.append(f"{name}: no 'Gate status:' line")
            continue
        gate = g.group(1)
        if unresolved and "BLOCKED" not in gate:
            problems.append(f"{name}: {unresolved} Critical unresolved but gate is '{gate.strip()}'")
        if not unresolved and "BLOCKED" in gate:
            problems.append(f"{name}: gate BLOCKED but no unresolved Critical issue found")
        n = re.search(r"BLOCKED\s*\((\d+)", gate)
        if n and int(n.group(1)) != unresolved:
            problems.append(f"{name}: gate says {n.group(1)} Critical unresolved; found {unresolved}")
    return problems, unresolved


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__)
        return 1
    problems, cited, ctext, (cm, ca) = check_checklist(argv[1])
    unresolved = None
    if len(argv) == 3:
        p2, unresolved = check_issues(argv[2], cited, ctext)
        problems += p2

    print(f"Main units covered: {cm}/{len(MAIN_UNITS)}; abstract units covered: {ca}/{len(ABSTRACT_UNITS)}")
    if unresolved is not None:
        print(f"Unresolved Critical issues: {unresolved}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("OK: coverage and consistency checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
