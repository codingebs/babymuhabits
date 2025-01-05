import sqlite3
from datetime import datetime
from habit import Habit

def init_db():
    """
    Starts the database by creating the "habits" table if it doesn't already exist.
    """
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits
                 (id INTEGER PRIMARY KEY, name TEXT, periodicity TEXT, creation_date TEXT, completion_dates TEXT)''')
    conn.commit()
    conn.close()

def save_habit(habit):
    """
    Saves a habit to the database.
    
    Parameters:
    habit (Habit): The habit object to save.
    """
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("INSERT INTO habits (name, periodicity, creation_date, completion_dates) VALUES (?, ?, ?, ?)",
              (habit.name, habit.periodicity, habit.creation_date.isoformat(), ','.join(map(lambda x: x.isoformat(), habit.completion_dates))))
    conn.commit()
    conn.close()

def load_habits():
    """
    Loads all habits from the database and returns them as a list of Habit objects.
    
    Returns:
    A list of Habit objects.
    """
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    rows = c.fetchall()
    conn.close()
    habits = []
    for row in rows:
        habit = Habit(row[1], row[2])
        habit.creation_date = datetime.fromisoformat(row[3])
        habit.completion_dates = [datetime.fromisoformat(date) for date in row[4].split(',') if date]
        habits.append(habit)
    return habits

def delete_habit(habit_name):
    """
    Delete a habit from the database by its name.
    
    Param:
    The name of the habit to delete.
    
    Returns:
    Boolean True if the habit was found and deleted, False otherwise.
    """
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("DELETE FROM habits WHERE name = ?", (habit_name,))
    if c.rowcount == 0:
        conn.close()
        return False
    conn.commit()
    conn.close()
    return True
