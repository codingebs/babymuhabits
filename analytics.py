from storage import load_habits

def get_all_habits():
    """
    Get all habits from the database.
    
    Returns:
    A list of all Habit objects.
    """
    return load_habits()

def get_habits_by_periodicity(periodicity):
    """
    Get habits that match a specific periodicity (like  "daily" or "weekly").
    
    Param:
    periodicity (str): Periodicity to filter habits.
    
    Returns:
    A list of Habit objects with specified periodicity.
    """
    return [habit for habit in load_habits() if habit.periodicity == periodicity]

def get_longest_streak():
    """
    Find the habit with the longest completion streaks.
    
    Returns:
    The habit with the longest streak.
    """
    habits = load_habits()
    return max(habits, key=lambda habit: len(habit.completion_dates))

def get_longest_streak_for_habit(habit_name):
    """
    Find the longest streak for a specific habit by entering the name of it.
    
    Param:
    habit_name (str): The name of the habit to find the streak for.
    
    Returns:
    The longest streak for the selected habit.
    """
    habits = load_habits()
    for habit in habits:
        if habit.name == habit_name:
            return len(habit.completion_dates)
    return 0