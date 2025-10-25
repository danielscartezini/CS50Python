import csv
import datetime
import os


DATA_FILE = "habits.csv"
HEADER = ["habit_name", "event_type", "date"]

def load_data():
    """Loads habit data from the CSV file."""
    if not os.path.exists(DATA_FILE):
        return {}
    data = {}
    try:
        with open(DATA_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            try:
                next(reader)
            except StopIteration:
                return {}
            for row in reader:
                if not row:
                    continue
                habit_name, event_type, date = row
                if habit_name not in data:
                    data[habit_name] = {
                        "created": "",
                        "completed": []
                    }
                if event_type == "created":
                    data[habit_name]["created"] = date
                elif event_type == "completed":
                    data[habit_name]["completed"].append(date)
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

    return data

def save_data(data):
    """Saves the habit data to the CSV file."""
    with open("habits", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        for name, details in data.items():
            writer.writerow([name, "created", details["created"]])
            for comp_date in details["completed"]:
                writer.writerow([name, "completed", comp_date])

def add_habit(data, name):
    """Adds a new habit to the data."""
    if name in data:
        print(f"❌ Habit '{name}' already exists.")
    else:
        data[name] = {
            "created": str(datetime.date.today()),
            "completed": [] 
        }
        print(f"✅ Added new habit: '{name}'")

def complete_habit(data, name):
    """Marks a habit as complete for today."""
    if name not in data:
        print(f"❌ Habit '{name}' not found.")
        return
    today = str(datetime.date.today())
    if today in data[name]["completed"]:
        print(f"👍 Habit '{name}' was already completed today.")
    else:
        data[name]["completed"].append(today)
        print(f"🎉 Great job! Completed '{name}' for today.")

def get_stats(habit_data):
    """Calculates and returns stats (total, streaks) for a habit."""
    completed_dates = habit_data["completed"]
    if not completed_dates:
        return 0, 0, 0
    dates = sorted([datetime.date.fromisoformat(d) for d in set(completed_dates)])
    total_completions = len(dates)
    longest_streak = 0
    current_streak = 0
    if not dates:
        return total_completions, 0,
    streak = 1
    longest_streak = 1
    for i in range(1, len(dates)):
        if dates[i] == dates[i-1] + datetime.timedelta(days=1):
            streak += 1
        else:
            longest_streak = max(longest_streak, streak)
            streak = 1
    longest_streak = max(longest_streak, streak)
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    if dates[-1] == today or dates[-1] == yesterday:
        current_streak = 1
        for i in range(len(dates) - 1, 0, -1):
            if dates[i] == dates[i-1] + datetime.timedelta(days=1):
                current_streak += 1
            else:
                break
    else:
        current_streak = 0

    return total_completions, current_streak, longest_streak

def display_all_stats(data):
    """Displays statistics for all habits."""
    if not data:
        print("No habits added yet. Add one first!")
        return

    print("\n--- 📊 Your Habit Stats ---")
    for habit, details in data.items():
        total, current_s, longest_s = get_stats(details)
        print(f"\nHabit: {habit}")
        print(f"  Total Completions: {total}")
        print(f"  Current Streak:    {current_s} days 🔥")
        print(f"  Longest Streak:    {longest_s} days 🏆")
    print("----------------------------")

def display_habits(data):
    """Lists all currently tracked habits."""
    if not data:
        print("You are not tracking any habits yet.")
        return
    print("\n--- 📝 Your Habits ---")
    for habit in data:
        print(f"- {habit}")
    print("------------------------")

def main_menu():
    """Displays the main menu and gets user choice."""
    print("\n======= Habit Tracker ========")
    print("1. Add a new habit")
    print("2. Complete a habit for today")
    print("3. View all habits")
    print("4. View stats")
    print("5. Exit")
    print("==============================")
    return input("Choose an option (1-5): ")

def main():
    """Main application loop."""
    data = load_data()
    while True:
        choice = main_menu()
        if choice == '1':
            name = input("Enter the name of the new habit: ").strip()
            if name:
                add_habit(data, name)
                save_data(data)
            else:
                print("❌ Habit name cannot be empty.")
        elif choice == '2':
            name = input("Which habit did you complete? ").strip()
            if name in data:
                complete_habit(data, name)
                save_data(data)
            else:
                print(f"❌ Habit '{name}' not found.")
        elif choice == '3':
            display_habits(data)

        elif choice == '4':
            display_all_stats(data)

        elif choice == '5':
            print("👋 Goodbye! Keep up the good work.")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
