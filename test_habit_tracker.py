
import pytest
import os
import datetime
from unittest.mock import MagicMock, patch

from data_store import DataStore
from habit_manager import Habit, HabitManager
from calendar_view import CalendarView
from utils import get_weekday_name, parse_date_string, format_date_to_string

# --- Fixtures ---

@pytest.fixture
def temp_data_file(tmp_path):
    """Provides a temporary data file path for DataStore tests."""
    return tmp_path / "test_habits.json"

@pytest.fixture
def data_store(temp_data_file):
    """Provides a DataStore instance with a temporary file."""
    ds = DataStore(str(temp_data_file))
    ds.data = {"habits": [], "completion_records": {}} # Ensure clean state
    ds._save_data() # Save initial empty state
    return ds

@pytest.fixture
def habit_manager(data_store):
    """Provides a HabitManager instance with a mocked DataStore."""
    return HabitManager(data_store)

@pytest.fixture
def sample_habits(habit_manager):
    """Adds sample habits to the habit manager."""
    h1 = habit_manager.add_habit("Read Book", "Read for 30 mins", "daily")
    h2 = habit_manager.add_habit("Exercise", "Go to the gym", "weekdays")
    h3 = habit_manager.add_habit("Meditate", "10 mins mindfulness", ["Saturday", "Sunday"])
    h4 = habit_manager.add_habit("Code Project", "Work on personal project", ["Monday", "Wednesday", "Friday"])
    return [h1, h2, h3, h4]

# --- Test DataStore ---

def test_data_store_init_empty(temp_data_file):
    """Test DataStore initializes with empty data if file doesn't exist."""
    ds = DataStore(str(temp_data_file))
    assert ds.data == {"habits": [], "completion_records": {}}

def test_data_store_save_load(data_store):
    """Test saving and loading data."""
    test_habit = Habit("Test Habit", frequency="daily")
    data_store.add_habit(test_habit)
    data_store.add_completion_record(test_habit.id, "2023-01-01")

    # Create a new DataStore instance to load from the same file
    new_ds = DataStore(data_store.data_file)
    assert len(new_ds.get_habits()) == 1
    assert new_ds.get_habits()[0].name == "Test Habit"
    assert new_ds.is_habit_completed_on_date(test_habit.id, "2023-01-01") is True

def test_data_store_add_habit(data_store):
    """Test adding a habit to the data store."""
    habit = Habit("New Habit")
    data_store.add_habit(habit)
    assert len(data_store.get_habits()) == 1
    assert data_store.get_habits()[0].name == "New Habit"

def test_data_store_update_habit(data_store):
    """Test updating an existing habit."""
    habit = Habit("Original Name")
    data_store.add_habit(habit)
    habit.name = "Updated Name"
    data_store.update_habit(habit)
    assert data_store.get_habits()[0].name == "Updated Name"

def test_data_store_delete_habit(data_store):
    """Test deleting a habit and its completion records."""
    habit = Habit("Habit to Delete")
    data_store.add_habit(habit)
    data_store.add_completion_record(habit.id, "2023-01-01")
    data_store.delete_habit(habit.id)
    assert len(data_store.get_habits()) == 0
    assert habit.id not in data_store.get_completion_records()

def test_data_store_add_completion_record(data_store):
    """Test adding a completion record."""
    habit = Habit("Daily Task")
    data_store.add_habit(habit)
    data_store.add_completion_record(habit.id, "2023-01-01")
    assert data_store.is_habit_completed_on_date(habit.id, "2023-01-01") is True
    # Test adding same record twice doesn't duplicate
    data_store.add_completion_record(habit.id, "2023-01-01")
    assert len(data_store.get_completion_records()[habit.id]) == 1

def test_data_store_remove_completion_record(data_store):
    """Test removing a completion record."""
    habit = Habit("Daily Task")
    data_store.add_habit(habit)
    data_store.add_completion_record(habit.id, "2023-01-01")
    data_store.remove_completion_record(habit.id, "2023-01-01")
    assert data_store.is_habit_completed_on_date(habit.id, "2023-01-01") is False

# --- Test Habit Class ---

def test_habit_init():
    """Test Habit initialization."""
    habit = Habit("Test Habit", "Description", "daily")
    assert habit.name == "Test Habit"
    assert habit.description == "Description"
    assert habit.frequency == "daily"
    assert isinstance(habit.id, str)
    assert isinstance(habit.created_at, datetime.datetime)

def test_habit_is_due_on_date_daily():
    """Test daily frequency."""
    habit = Habit("Daily", frequency="daily")
    assert habit.is_due_on_date(datetime.date(2023, 10, 21)) is True # Saturday
    assert habit.is_due_on_date(datetime.date(2023, 10, 23)) is True # Monday

def test_habit_is_due_on_date_weekdays():
    """Test weekdays frequency."""
    habit = Habit("Weekdays", frequency="weekdays")
    assert habit.is_due_on_date(datetime.date(2023, 10, 21)) is False # Saturday
    assert habit.is_due_on_date(datetime.date(2023, 10, 23)) is True # Monday

def test_habit_is_due_on_date_weekends():
    """Test weekends frequency."""
    habit = Habit("Weekends", frequency="weekends")
    assert habit.is_due_on_date(datetime.date(2023, 10, 21)) is True # Saturday
    assert habit.is_due_on_date(datetime.date(2023, 10, 23)) is False # Monday

def test_habit_is_due_on_date_specific_days():
    """Test specific days frequency."""
    habit = Habit("Specific Days", frequency=["Monday", "Wednesday"])
    assert habit.is_due_on_date(datetime.date(2023, 10, 23)) is True # Monday
    assert habit.is_due_on_date(datetime.date(2023, 10, 24)) is False # Tuesday
    assert habit.is_due_on_date(datetime.date(2023, 10, 21)) is False # Saturday

# --- Test HabitManager ---

def test_habit_manager_add_habit(habit_manager):
    """Test adding a habit via HabitManager."""
    habit = habit_manager.add_habit("New Habit")
    assert habit.name == "New Habit"
    assert len(habit_manager.get_all_habits()) == 1

def test_habit_manager_mark_complete(habit_manager, sample_habits):
    """Test marking a habit complete."""
    habit_id = sample_habits[0].id # Daily habit
    date_str = "2023-10-21"
    assert habit_manager.mark_habit_complete(habit_id, date_str) is True
    assert habit_manager.data_store.is_habit_completed_on_date(habit_id, date_str) is True

def test_habit_manager_mark_complete_not_due(habit_manager, sample_habits, capsys):
    """Test marking a habit complete when not due (should still mark, but warn)."""
    habit_id = sample_habits[1].id # Weekdays habit
    date_str = "2023-10-21" # Saturday
    assert habit_manager.mark_habit_complete(habit_id, date_str) is True
    assert habit_manager.data_store.is_habit_completed_on_date(habit_id, date_str) is True
    captured = capsys.readouterr()
    assert "Warning: Habit" in captured.out

def test_habit_manager_unmark_complete(habit_manager, sample_habits):
    """Test unmarking a habit complete."""
    habit_id = sample_habits[0].id
    date_str = "2023-10-21"
    habit_manager.mark_habit_complete(habit_id, date_str)
    assert habit_manager.data_store.is_habit_completed_on_date(habit_id, date_str) is True
    assert habit_manager.unmark_habit_complete(habit_id, date_str) is True
    assert habit_manager.data_store.is_habit_completed_on_date(habit_id, date_str) is False

def test_habit_manager_get_habits_for_date(habit_manager, sample_habits):
    """Test retrieving habits for a specific date."""
    today = datetime.date(2023, 10, 21) # Saturday
    habits_for_today = habit_manager.get_habits_for_date(today)
    # h1 (daily), h3 (weekends)
    assert len(habits_for_today) == 2
    assert any(item["habit"].name == "Read Book" for item in habits_for_today)
    assert any(item["habit"].name == "Meditate" for item in habits_for_today)

    # Mark one complete and check status
    habit_manager.mark_habit_complete(sample_habits[0].id, format_date_to_string(today))
    habits_for_today_updated = habit_manager.get_habits_for_date(today)
    for item in habits_for_today_updated:
        if item["habit"].id == sample_habits[0].id:
            assert item["completed"] is True
        else:
            assert item["completed"] is False

# --- Test CalendarView ---

def test_calendar_view_display_weekend_calendar(habit_manager, sample_habits, capsys):
    """Test displaying the weekend calendar view."""
    calendar_view = CalendarView(habit_manager)
    start_date = datetime.date(2023, 10, 20) # Friday

    # Mark a weekend habit complete
    weekend_habit_id = sample_habits[2].id # Meditate (weekends)
    habit_manager.mark_habit_complete(weekend_habit_id, "2023-10-21") # Saturday

    calendar_view.display_weekend_calendar(start_date, num_weeks=1)
    captured = capsys.readouterr()

    assert "--- Weekend Habit Calendar ---" in captured.out
    assert "### Saturday, 2023-10-21 ###" in captured.out
    assert "### Sunday, 2023-10-22 ###" in captured.out
    assert "[X] Meditate" in captured.out # Marked complete
    assert "[ ] Read Book" in captured.out # Daily, not marked
    assert "No habits scheduled." not in captured.out # Should have habits


def test_calendar_view_no_habits(habit_manager, capsys):
    """Test displaying calendar with no habits defined."""
    calendar_view = CalendarView(habit_manager)
    start_date = datetime.date(2023, 10, 20)
    calendar_view.display_weekend_calendar(start_date, num_weeks=1)
    captured = capsys.readouterr()
    assert "No habits scheduled." in captured.out

# --- Test Utils ---

def test_get_weekday_name():
    assert get_weekday_name(datetime.date(2023, 10, 23)) == "Monday"
    assert get_weekday_name(datetime.date(2023, 10, 21)) == "Saturday"

def test_parse_date_string():
    assert parse_date_string("2023-10-21") == datetime.date(2023, 10, 21)
    with pytest.raises(ValueError):
        parse_date_string("invalid-date")

def test_format_date_to_string():
    assert format_date_to_string(datetime.date(2023, 10, 21)) == "2023-10-21"


