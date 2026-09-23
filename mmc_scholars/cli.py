#!/usr/bin/env python3
"""
MMC Scholar Roster CLI — quick lookups for mentors.

Usage:
  python3 -m mmc_scholars.cli cohort <cohort_name>
  python3 -m mmc_scholars.cli mentor <mentor_name>
  python3 -m mmc_scholars.cli progress <scholar_id>
"""

import sys

from .roster import load_roster, list_by_cohort, list_by_mentor, get_scholar, progress_percent


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command, arg = sys.argv[1], sys.argv[2]
    roster = load_roster()

    if command == "cohort":
        for s in list_by_cohort(roster, arg):
            print(f"{s.id}  {s.name:20s}  {progress_percent(s):6.1f}%  mentor: {s.mentor}")
    elif command == "mentor":
        for s in list_by_mentor(roster, arg):
            print(f"{s.id}  {s.name:20s}  {progress_percent(s):6.1f}%  cohort: {s.cohort}")
    elif command == "progress":
        s = get_scholar(roster, arg)
        if not s:
            print(f"No scholar with id {arg}")
            sys.exit(1)
        done = ", ".join(s.milestones_completed) or "(none yet)"
        print(f"{s.name} — {progress_percent(s)}% complete")
        print(f"Completed: {done}")
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
