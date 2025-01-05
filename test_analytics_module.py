import unittest
from datetime import datetime
from habit import Habit
from storage import save_habit, init_db, load_habits
from analytics import get_all_habits, get_habits_by_periodicity, get_longest_streak, get_longest_streak_for_habit

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        # Starts the database and add predefined habits
        init_db()
        self.clear_database()
        self.add_predefined_habits()

    def clear_database(self):
        # Clears the database to ensure a clean test environment is given.
        habits = load_habits()
        for habit in habits:
            self.delete_habit(habit.name)

    def delete_habit(self, habit_name):
        # Deletes a habit from the database by using the name.
        import sqlite3
        conn = sqlite3.connect("habits.db")
        c = conn.cursor()
        c.execute("DELETE FROM habits WHERE name = ?", (habit_name,))
        conn.commit()
        conn.close()

    def add_predefined_habits(self):
        """
        Adds 5 predefined habits to the database with specific dates for data collection purposes.
        """
        predefined_habits = [
            {
                "name": "feed babymü",
                "periodicity": "daily",
                "completion_dates": [
                    "2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07",
                    "2023-10-08", "2023-10-09", "2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14",
                    "2023-10-15", "2023-10-16", "2023-10-17", "2023-10-18", "2023-10-19", "2023-10-20", "2023-10-21",
                    "2023-10-22", "2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27", "2023-10-28"
                ]
            },
            {
                "name": "walk 10k steps",
                "periodicity": "daily",
                "completion_dates": [
                    "2023-10-01", "2023-10-02", "2023-10-03", "2023-10-05", "2023-10-06", "2023-10-07",
                    "2023-10-08", "2023-10-09", "2023-10-10", "2023-10-12", "2023-10-13", "2023-10-14",
                    "2023-10-15", "2023-10-16", "2023-10-17", "2023-10-19", "2023-10-20", "2023-10-21",
                    "2023-10-22", "2023-10-23", "2023-10-24", "2023-10-26", "2023-10-27", "2023-10-28"
                ]
            },
            {
                "name": "read 20 pages",
                "periodicity": "daily",
                "completion_dates": [
                    "2023-10-01", "2023-10-02", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07",
                    "2023-10-08", "2023-10-09", "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14",
                    "2023-10-15", "2023-10-16", "2023-10-18", "2023-10-19", "2023-10-20", "2023-10-21",
                    "2023-10-22", "2023-10-23", "2023-10-25", "2023-10-26", "2023-10-27", "2023-10-28"
                ]
            },
            {
                "name": "clean house",
                "periodicity": "weekly",
                "completion_dates": [
                    "2023-10-01", "2023-10-08", "2023-10-15", "2023-10-22"
                ]
            },
            {
                "name": "grocery shopping",
                "periodicity": "weekly",
                "completion_dates": [
                    "2023-10-01", "2023-10-08", "2023-10-15", "2023-10-22"
                ]
            }
        ]

        for habit_data in predefined_habits:
            habit = Habit(habit_data["name"], habit_data["periodicity"])
            habit.completion_dates = [datetime.strptime(date, "%Y-%m-%d") for date in habit_data["completion_dates"]]
            save_habit(habit)

    def test_get_all_habits(self):
        # Tests to check if all habits are returned correctly
        habits = get_all_habits()
        self.assertEqual(len(habits), 5)  #5 habits expected
        habit_names = [habit.name for habit in habits]
        self.assertIn("feed babymü", habit_names)
        self.assertIn("walk 10k steps", habit_names)
        self.assertIn("read 20 pages", habit_names)
        self.assertIn("clean house", habit_names)
        self.assertIn("grocery shopping", habit_names)

    def test_get_habits_by_periodicity_daily(self):
        # Test to check if daily habits are filtered correctly
        daily_habits = get_habits_by_periodicity("daily")
        self.assertEqual(len(daily_habits), 3)  #3 daily habits
        habit_names = [habit.name for habit in daily_habits]
        self.assertIn("feed babymü", habit_names)
        self.assertIn("walk 10k steps", habit_names)
        self.assertIn("read 20 pages", habit_names)

    def test_get_habits_by_periodicity_weekly(self):
        # Test to check if weekly habits are filtered correctly
        weekly_habits = get_habits_by_periodicity("weekly")
        self.assertEqual(len(weekly_habits), 2)  # 2 weekly habits
        habit_names = [habit.name for habit in weekly_habits]
        self.assertIn("clean house", habit_names)
        self.assertIn("grocery shopping", habit_names)

    def test_get_longest_streak(self):
        # Test to check if the habit with the longest streak is identified correctly
        habit = get_longest_streak()
        self.assertEqual(habit.name, "feed babymü")  # feed babymü has the longest streak

    def test_get_longest_streak_for_habit(self):
        # Test to check the longest streak for a specific habit
        streak = get_longest_streak_for_habit("feed babymü")
        self.assertGreaterEqual(streak, 28)  # Streak should be at 28

if __name__ == '__main__':
    unittest.main()