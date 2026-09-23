"""
MMC Scholar Roster — data model
"""

from dataclasses import dataclass, field
from typing import List

ALL_MILESTONES = [
    "orientation",
    "resume_workshop",
    "mock_interview",
    "technical_project",
    "capstone_presentation",
]


@dataclass
class Scholar:
    id: str
    name: str
    cohort: str
    mentor: str
    joined: str  # ISO date string
    milestones_completed: List[str] = field(default_factory=list)
