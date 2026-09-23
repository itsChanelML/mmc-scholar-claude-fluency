"""
MMC Scholar Roster — operations

Loads scholar records from data/scholars.json and provides the lookups
and reports a mentor actually needs day to day.
"""

import json
from pathlib import Path
from typing import List, Optional

from .models import Scholar, ALL_MILESTONES

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "scholars.json"


def load_roster(path: Path = DATA_FILE) -> List[Scholar]:
    with open(path) as f:
        raw = json.load(f)
    return [Scholar(**r) for r in raw]


def get_scholar(roster: List[Scholar], scholar_id: str) -> Optional[Scholar]:
    for s in roster:
        if s.id == scholar_id:
            return s
    return None


def list_by_cohort(roster: List[Scholar], cohort: str) -> List[Scholar]:
    return [s for s in roster if s.cohort == cohort]


def list_by_mentor(roster: List[Scholar], mentor: str) -> List[Scholar]:
    return [s for s in roster if s.mentor == mentor]


def mark_milestone(scholar: Scholar, milestone: str) -> None:
    if milestone not in ALL_MILESTONES:
        raise ValueError(f"Unknown milestone: {milestone}. Valid: {ALL_MILESTONES}")
    if milestone not in scholar.milestones_completed:
        scholar.milestones_completed.append(milestone)


def progress_percent(scholar: Scholar) -> float:
    """Percent of milestones this scholar has completed."""
    return round(len(scholar.milestones_completed) / len(ALL_MILESTONES) * 100, 1)
