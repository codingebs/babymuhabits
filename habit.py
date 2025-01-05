from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        """
        Start a new habit with a name and periodicity.
        
        Param:
        The name of the habit (for example, "Feed BabyMü").
        How often the habit should be done (for example, "daily" or "weekly").
        """
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completion_dates = []

    def complete_task(self):
        """
        Mark the habit as completed by adding the current date and time to the list of completion dates.
        """
        self.completion_dates.append(datetime.now())

    def __repr__(self):
        """
        Provide a string representation of the habit in order to debug.
        """
        return f"Habit(name={self.name}, periodicity={self.periodicity}, creation_date={self.creation_date}, completion_dates={self.completion_dates})"

    def __str__(self):
        """
        Provides a nicely formatted string of the habit to make it look more neat when printed.
        """
        completion_dates_str = ', '.join(date.strftime('%Y-%m-%d %H:%M:%S') for date in self.completion_dates)
        return (f"Habit: {self.name}\n"
                f"Periodicity: {self.periodicity}\n"
                f"Created on: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Completion Dates: {completion_dates_str if completion_dates_str else 'None'}\n")