
import sys
import datetime
import argparse

from habit_manager import HabitManager, Habit
from calendar_view import CalendarView
from data_store import DataStore
from utils import parse_date_string, format_date_to_string

def add_habit_cli(habit_manager: HabitManager, args):
    """Adds a new habit based on CLI arguments."""
    name = args.name
    description = args.description if args.description else ""
    frequency = args.frequency

    if frequency not in ["daily", "weekdays", "weekends"] and \
       not all(day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] for day in frequency):
        print("Error: Invalid frequency. Use 'daily', 'weekdays', 'weekends', or a comma-separated list of weekday names.")
        return

    if isinstance(frequency, str) and ',' in frequency:
        frequency = [d.strip() for d in frequency.split(',')]

    habit = habit_manager.add_habit(name, description, frequency)
    print(f"Habit \'{habit.name}\' (ID: {habit.id[:8]}...) added successfully.")

def mark_habit_complete_cli(habit_manager: HabitManager, args):
    """Marks a habit as complete for a given date based on CLI arguments."""
    habit_id = args.id
    date_str = args.date

    if habit_manager.mark_habit_complete(habit_id, date_str):
        print(f"Habit {habit_id[:8]}... marked complete for {date_str}.")
    else:
        print(f"Failed to mark habit {habit_id[:8]}... complete for {date_str}.")

def view_habits_cli(habit_manager: HabitManager):
    """Displays all defined habits."""
    habits = habit_manager.get_all_habits()
    if not habits:
        print("No habits defined yet.")
        return

    print("\n--- Your Habits ---")
    for habit in habits:
        print(f"ID: {habit.id[:8]}...")
        print(f"  Name: {habit.name}")
        print(f"  Description: {habit.description if habit.description else 'N/A'}")
        print(f"  Frequency: {', '.join(habit.frequency) if isinstance(habit.frequency, list) else habit.frequency}")
        print(f"  Created: {format_date_to_string(habit.created_at.date())}")
        print("---------------------")

def main():
    """Main function to handle command-line arguments and orchestrate the habit tracker application."""
    data_store = DataStore("data/habits.json")
    habit_manager = HabitManager(data_store)
    calendar_view = CalendarView(habit_manager)

    parser = argparse.ArgumentParser(description="A simple command-line habit tracker.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add habit command
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", type=str, help="Name of the habit")
    add_parser.add_argument("-d", "--description", type=str, help="Description of the habit")
    add_parser.add_argument("-f", "--frequency", type=str, default="daily",
                            help="Frequency (daily, weekdays, weekends, or comma-separated days like Mon,Tue)")
    add_parser.set_defaults(func=lambda args: add_habit_cli(habit_manager, args))

    # Mark complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a habit as complete for a date")
    complete_parser.add_argument("id", type=str, help="ID of the habit to mark complete")
    complete_parser.add_argument("date", type=str, default=format_date_to_string(datetime.date.today()),
                                 help="Date to mark complete (YYYY-MM-DD, defaults to today)")
    complete_parser.set_defaults(func=lambda args: mark_habit_complete_cli(habit_manager, args))

    # View habits command
    view_parser = subparsers.add_parser("view", help="View all defined habits")
    view_parser.set_defaults(func=lambda args: view_habits_cli(habit_manager))

    # Weekend calendar command
    calendar_parser = subparsers.add_parser("calendar", help="Display weekend habit calendar")
    calendar_parser.add_argument("-s", "--start-date", type=str, default=format_date_to_string(datetime.date.today()),
                                 help="Start date for the calendar (YYYY-MM-DD, defaults to today)")
    calendar_parser.add_argument("-w", "--weeks", type=int, default=4,
                                 help="Number of weeks to display (default: 4)")
    calendar_parser.set_defaults(func=lambda args: calendar_view.display_weekend_calendar(
        parse_date_string(args.start_date), args.weeks))

    # Delete habit command
    delete_parser = subparsers.add_parser("delete", help="Delete a habit")
    delete_parser.add_argument("id", type=str, help="ID of the habit to delete")
    delete_parser.set_defaults(func=lambda args: habit_manager.delete_habit(args.id))

    # Unmark complete command
    unmark_parser = subparsers.add_parser("unmark", help="Unmark a habit as complete for a date")
    unmark_parser.add_argument("id", type=str, help="ID of the habit to unmark complete")
    unmark_parser.add_argument("date", type=str, default=format_date_to_string(datetime.date.today()),
                                 help="Date to unmark complete (YYYY-MM-DD, defaults to today)")
    unmark_parser.set_defaults(func=lambda args: habit_manager.unmark_habit_complete(args.id, args.date))


    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

