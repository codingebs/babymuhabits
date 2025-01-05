import pytest
from habit import Habit
from storage import save_habit, load_habits, init_db

def test_create_habit():
    """
    Test the creation of a habit to make sure it starts correctly.
    """
    habit = Habit("Test Habit", "daily")
    assert habit.name == "Test Habit"
    assert habit.periodicity == "daily"

def test_complete_task():
    """
    Test marking a habit as completed to make sure the completion date is recorded.
    """
    habit = Habit("Test Habit", "daily")
    habit.complete_task()
    assert len(habit.completion_dates) == 1

def test_save_and_load_habit():
    """
    Test saving a habit to the database and then loading it to make sure it works.
    """
    init_db()
    habit = Habit("Test Habit", "daily")
    save_habit(habit)
    habits = load_habits()
    assert any(h.name == "Test Habit" for h in habits)

if __name__ == "__main__":
    pytest.main()