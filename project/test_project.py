import datetime
import project

def main():
    test_add_habit()
    test_complete_habit()
    test_get_stats()
    print("All tests passed!")

def test_add_habit():
    data = {}
    project.add_habit(data, "Read a book")
    assert "Read a book" in data
    assert data["Read a book"]["created"] == str(datetime.date.today())

def test_complete_habit():
    data = {"Meditate": {"created": "2025-10-21", "completed": []}}
    project.complete_habit(data, "Meditate")
    today = str(datetime.date.today())
    assert today in data["Meditate"]["completed"]

def test_get_stats():
    habit_details = {"created": "2025-10-21", "completed": []}
    total, current, longest = project.get_stats(habit_details)
    assert total == 0
    assert current == 0
    assert longest == 0

if __name__ == "__main__":
    main()
