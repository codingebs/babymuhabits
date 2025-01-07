# babymuhabits


# Overview

Baby-Mü Habits is a habit tracking app, which is Python-based and helps it's users to create, track, update, and analyze their daily/weekly goals. 

# Features:

- Create habits by periodicities
- List available habits
- Mark specific habit as complete
- Analyze habits, for example insights for the longest streak
- Delete habit by name

# Requirements:

-Python 3.8 or higher

# Setup:

Option 1: Cloning of Repository
-If you have access to Git:

Clone Repository:
$ git clone https://github.com/codingebs/babymuhabits

Go to the extracted folder:
$ cd babymuhabits

Install dependencies:
$ pip install pytest sqlite3


Option 2: Manual Download of Code
-If you don't have access to Git, please install the application by downloading the code directly. 
1. Go to the repository on GitHub.(https://github.com/codingebs/babymuhabits)
2. Click on the "Code" button and select "Download ZIP."
3. Unzip the downloaded ZIP file on your device.
4. Navigate to the extracted folder:

$ cd babymuhabits

# Installation of Dependencies:

Manual installation of the following when not already installed:
-pytest
-sqlite3

# Usage: 

In order to run the application you need to start the habit tracker by executing main.py file:

$ python main.py

Create habit: User can create a new habit by name and periodicity
List available habits: User gets an overview of all available habits
Complete habit: User can mark a habit as completed for that specific day
Analyze habit: Gives insights to habits, like the longest streak
Delete habit: User can remove habit by name
Bye: User exits application

# Project Strucure:

main.py : Provides command-lines interface for user to work with in the habit app

habit.py : Includes the Habit class, which describes the properties and methods for for managing habits

storage.py : Takes charge of database operations like saving, or loading habits by using SQLite

analytics.py : Provides functions in order to analyze habits, for example the calculation of the longest streak

predfined_habits.py : Includes pre-defined habits that the user can add to their tracker

test_habit_tracker.py : Includes unit tests for the habit app to make sure the main functionalities work as required

test_analytics_py : Contains unit tests for the analytics module to make sure the analytics options work and required

This project was created for the Object Oriented and Functional Programming with Python module at IU International University of Applied Sciences. 
