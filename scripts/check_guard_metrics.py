#!/usr/bin/env python
r"""Fail when a model exists but its guard metrics are still unfilled.

    py scripts/check_guard_metrics.py
    py scripts/check_guard_metrics.py --quiet     # exit code only

AGENTS.md section 4.5 ships a blank guard-metrics table on purpose, and says so
loudly. That is correct for a fresh clone with no model yet - and it is the
sentence an agent quotes to justify leaving it blank forever.

The hole this closes: a project that ALREADY HAS A MODEL is not a fresh clone.
Three repositories in this family were upgraded to the current workflow and
inherited the blank table along with it, each with a working `.nlogox` and real
headless runs behind them. Nothing in the prose distinguishes "not yet needed"
from "overdue", because the prose cannot see the filesystem.

So the rule is expressed as a condition rather than a reminder:

    a .nlogox exists  AND  the table still says [FILL IN   ->  overdue

WHY IT MATTERS RATHER THAN BEING TIDINESS. A headless exit code proves the model
compiled and `go` ran without throwing on the paths it reached. It does not prove
the model did anything. Guard metrics are the only evidence a run was
non-degenerate, and an unfilled table means every headless result reported from
this repository is unguarded - a number nobody can distinguish from the same
number produced by a dead model.

WHAT THIS DELIBERATELY DOES NOT DO: judge whether the reporters are any good. It
checks that a human or agent has committed to specific expressions. Section 4.5's
"what broken model would still pass this?" test is a judgement call and stays
with the person making it.

Exit codes: 0 nothing overdue; 1 could not read AGENTS.md; 3 overdue.
"""

from __future__ import annotations

import argparse
import io
import os
import re
import sys
from pathlib import Path

# The placeholder markers section 4.5 ships with. A row still carrying any of
# these has not been decided; matching on the literal text rather than on the
# table structure keeps this working if rows are added or reordered.
PLACEHOLDER = re.compile(r"\[FILL IN|\[cumulative counter\]|\[one terminal outcome\]"
                         r"|\[a stock, budget", re.I)
SECTION = "## 4.5"


def main() -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--agents", default="AGENTS.md")
    ap.add_argument("-q", "--quiet", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    doc = root / args.agents
    if not doc.is_file():
        print("no {} here - is this the project root?".format(args.agents),
              file=sys.stderr)
        return 1

    # A model anywhere in the tree counts, but skip build/backup noise so a
    # stray copy in a temp directory cannot trigger this on a fresh clone.
    models = [p for p in root.rglob("*.nlogox")
              if not any(x in p.parts for x in
                         (".git", "build", "backup", "backups", "archive", "_old"))]

    text = io.open(doc, encoding="utf-8", errors="replace").read()
    i = text.find(SECTION)
    if i < 0:
        if not args.quiet:
            print("  {} has no {} section - nothing to check".format(args.agents, SECTION))
        return 0
    j = text.find("\n## ", i + 1)
    section = text[i:j if j > 0 else len(text)]
    holes = PLACEHOLDER.findall(section)

    if not args.quiet:
        print("  models found        : {}".format(len(models)))
        for m in models[:5]:
            print("     {}".format(m.relative_to(root)))
        print("  unfilled placeholders in {} : {}".format(SECTION, len(holes)))

    if models and holes:
        print("\n  OVERDUE: this project has a model but its guard metrics are"
              " still the template's placeholders.\n"
              "  Every headless result reported from here is unguarded - there is"
              " no evidence\n  a run was non-degenerate rather than dead.\n\n"
              "  Fill the table in {} {} with reporters from the model, then re-run"
              " this.\n"
              "  Section 4.5 explains how to choose the four; the test to apply to"
              " each row is\n  \"what broken model would still pass this?\"".format(
                  args.agents, SECTION), file=sys.stderr)
        return 3

    if not args.quiet:
        if not models:
            print("\n  ok - no model yet, so a blank table is the expected state.")
        else:
            print("\n  ok - guard metrics are declared.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
