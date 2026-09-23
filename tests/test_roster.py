from mmc_scholars.models import Scholar, ALL_MILESTONES
from mmc_scholars.roster import (
    load_roster, get_scholar, list_by_cohort, list_by_mentor,
    mark_milestone, progress_percent,
)


def make_scholar(**overrides):
    defaults = dict(
        id="test-1", name="Test Scholar", cohort="2025-fall",
        mentor="Dana Whitfield", joined="2025-09-08",
    )
    defaults.update(overrides)
    return Scholar(**defaults)


def test_load_roster_reads_all_records():
    roster = load_roster()
    assert len(roster) == 9


def test_get_scholar_found():
    roster = load_roster()
    s = get_scholar(roster, "s003")
    assert s is not None
    assert s.name == "Keisha Wallace"


def test_get_scholar_not_found_returns_none():
    roster = load_roster()
    assert get_scholar(roster, "nope") is None


def test_list_by_cohort():
    roster = load_roster()
    fall = list_by_cohort(roster, "2025-fall")
    assert len(fall) == 5
    assert all(s.cohort == "2025-fall" for s in fall)


def test_list_by_mentor():
    roster = load_roster()
    mentees = list_by_mentor(roster, "Priya Anand")
    assert {s.id for s in mentees} == {"s005", "s008", "s009"}


def test_mark_milestone_adds_once():
    s = make_scholar()
    mark_milestone(s, "orientation")
    mark_milestone(s, "orientation")  # marking twice should not duplicate
    assert s.milestones_completed == ["orientation"]


def test_mark_milestone_rejects_unknown():
    s = make_scholar()
    try:
        mark_milestone(s, "not_a_real_milestone")
        assert False, "expected a ValueError"
    except ValueError:
        pass


def test_progress_percent_partial_completion():
    s = make_scholar(milestones_completed=["orientation", "resume_workshop"])
    assert progress_percent(s) == 40.0  # 2 of 5 milestones


def test_progress_percent_full_completion():
    s = make_scholar()
    for m in ALL_MILESTONES:
        mark_milestone(s, m)
    assert progress_percent(s) == 100.0
