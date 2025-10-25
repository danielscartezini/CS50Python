# Harvard's introduction to programming with Python (CS50P).
An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and “debug” it. Designed for students with or without prior programming experience who’d like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems.


# Python Habit Tracker

A straightforward, command-line application designed to help users establish and maintain good habits by tracking daily progress and calculating current and longest consecutive streaks.

Video Demo: https://www.google.com/search?q=https://youtu.be/QTLY9tHpuIs

Author: Daniel Costa Scartezini

Location: Brasília, Brazil


# Project Overview:

The Python Habit Tracker is a command-line interface (CLI) application built entirely in Python. It offers a clean, text-based experience for logging daily habit completions and instantly viewing motivational statistics.
The project addresses the fundamental challenge of habit formation: consistency. By providing real-time feedback in the form of streaks and total completions, it serves as a simple yet effective motivational tool for any user who wants to track routines like "Excercise," "Read 10 pages," or "Hydrate."


# In-Memory Data Structure:

Inside the application, the load_data function transforms the raw CSV rows into a Python dictionary for efficient manipulation:


# The Streak Calculation Logic:

The get_stats function is responsible for accurately determining both the longest and current streak.

# Data Preparation: It first collects all unique completion dates for a given habit, converts them to datetime.date objects, and sorts them chronologically.

Longest Streak: This is calculated by iterating through the sorted dates and checking if each consecutive date is exactly one day after the previous one (dates[i] == dates[i-1] + timedelta(days=1)).

Current Streak: To be considered current, a streak must end either today or yesterday. The function iterates backward from the most recent completion date. If the last date is older than yesterday, the current streak is reset to zero, ensuring the stats accurately reflect active, recent performance.

