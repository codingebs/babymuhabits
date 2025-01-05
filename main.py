from storage import init_db, save_habit, load_habits, delete_habit
from habit import Habit
from analytics import get_all_habits, get_habits_by_periodicity, get_longest_streak, get_longest_streak_for_habit
from predefined_habits import add_predefined_habits

print("Welcome to BabyMü Habits!")

def main_menu():
    """
    Shows the main menu and checks user input to navigate through available options.
    """
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Create a new habit")
        print("2. List all available habits")
        print("3. Complete habit")
        print("4. Analyze habits")
        print("5. Delete a habit")
        print("6. Bye")
        choice = input("Enter your choice: ").lower()

        if choice == "1":
            create_habit()
        elif choice == "2":
            list_all_habits()
        elif choice == "3":
            complete_habit()
        elif choice == "4":
            habit_analyzation()
        elif choice == "5":
            delete_habit_task()
        elif choice == "6":
            print("Thank you for visiting BabyMü Habits. Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

def create_habit():
    """
    Asks the user to create a new habit by entering habit name and periodicity.
    """
    name = input("Please enter the name of the habit: ").lower()
    periodicity = input("Enter the periodicity (daily/weekly): ").lower()
    habit = Habit(name, periodicity)
    save_habit(habit)
    print(f"Your new habit '{name}' with periodicity '{periodicity}' is created.")

def list_all_habits():
    """
    Lists all habits in a neat and readable format, including predefined and user-created habits.
    """
    habits = load_habits()
    for habit in habits:
        print(habit)

def complete_habit():
    """
    Requests the user to mark a habit task as completed by entering the habit's name.
    """
    name = input("Enter the name of the habit to complete: ").lower()
    habits = load_habits()
    for habit in habits:
        if habit.name == name:
            habit.complete_task()
            save_habit(habit)
            print(f"Thank you! Your selected habit '{name}' was completed.")
            return
    print(f"Your selected habit '{name}' was not found.")

def delete_habit_task():
    """
    Asks the user to delete a habit by entering the name.
    """
    name = input("Enter the name of the habit to delete: ").lower()
    if delete_habit(name):
        print(f"Your selected habit {name} was deleted.")
    else:
        print(f"Habit {name} does not exist.")

def habit_analyzation():
    """
    Analytics menu that analyzes selected user habits. User is asked to enter their choice by number.
    """
    print("\nAnalytics Menu:")
    print("1. List all currently tracked habits")
    print("2. List habits by periodicity")
    print("3. Longest run streak of all habits")
    print("4. Longest run streak for a specific habit")
    choice = input("Enter your choice: ")

    if choice == '1':
        habits = get_all_habits()
        for habit in habits:
            print(habit)
    elif choice == '2':
        periodicity = input("Enter the periodicity (daily/weekly): ")
        habits = get_habits_by_periodicity(periodicity)
        for habit in habits:
            print(habit)
    elif choice == '3':
        habit = get_longest_streak()
        print(f"Longest streak is for habit '{habit.name}' with {len(habit.completion_dates)} completions.")
    elif choice == '4':
        name = input("Enter the name of the habit: ").lower()
        streak = get_longest_streak_for_habit(name)
        print(f"Longest streak for habit '{name}' is {streak} completions.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    init_db()  # Starts the database
    add_predefined_habits()  # Adds predefined habits to the database
    main_menu()  # Shows the main menu