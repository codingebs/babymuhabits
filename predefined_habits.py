from habit import Habit
from storage import save_habit, load_habits

def add_predefined_habits():
    """
    Add 5 predefined habits to the database.
    """
    predefined_habits = [
        Habit("feed babymü", "daily"),
        Habit("walk 10k steps", "daily"),
        Habit("read 20 pages", "daily"),
        Habit("clean house", "weekly"),
        Habit("grocery shopping", "weekly")
    ]

    existing_habits = load_habits()
    existing_habit_names = {habit.name for habit in existing_habits}

    for habit in predefined_habits:
        if habit.name not in existing_habit_names:
            save_habit(habit)

