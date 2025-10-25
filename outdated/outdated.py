import sys

def main():
    """
    Continuously prompts the user for a date until a valid format is entered
    and successfully converted to YYYY-MM-DD.
    """
    while True:
        # Use .strip() here to handle leading/trailing whitespace (e.g., " 9/8/1636 ")
        date_str = input("Date: ").strip()

        result = None
        if "/" in date_str:
            result = format1(date_str)

        elif "," in date_str:
            result = format2(date_str)

        if result is not None:
            # FIX: Print ONLY the result string, without any prefix text.
            print(result)
            break

        # Reprompt if no valid format was matched or if the format function returned None
        print("Error: Invalid date format or value. Please try again.")


""" expect September 8, 1636 """
def format2(date):
    months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
            ]

    try:
        # Split the string into three parts (Month, Day with comma, Year)
        month_str, day_with_comma, year_str = date.split()

        # --- Type Conversion and Cleaning ---
        day = int(day_with_comma.strip(","))
        year = int(year_str)
        month_string = month_str.title() # Normalize the case for comparison

    except ValueError:
        # Returns None if the split fails (e.g., 'Sep 8, 1636 extra')
        # or if the int() conversion fails (e.g., 'September eight, 1636')
        return None

    # --- Validation ---
    # Check if the month name is valid AND the day is within a standard range
    if (month_string not in months) or (day < 1 or day > 31):
        return None

    # --- Finding Month Number (Corrected Loop Logic) ---
    month = 0
    # The comparison now uses the normalized month_string.
    for i, m in enumerate(months):
        if m == month_string:
            month = i + 1
            break

    # Should not happen due to the check above, but good practice
    if month == 0:
        return None

    # Final format: YYYY-MM-DD with zero padding
    return f"{year}-{month:02d}-{day:02d}"


""" expect 9/8/1636 format"""
def format1(date):
    try:
        # Split the string by '/'
        month_str, day_str, year_str = date.split("/")

        # --- Type Conversion ---
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)

    except ValueError:
        # Returns None if the split fails (not 3 parts) or int conversion fails
        return None

    # --- Validation (Corrected Logic) ---
    # It must be 'or' to check if the value is outside the valid range (1-12 or 1-31).
    if (day < 1 or day > 31) or (month < 1 or month > 12):
        return None

    # Final format: YYYY-MM-DD with zero padding
    return f"{year}-{month:02d}-{day:02d}"


if __name__ == "__main__":
    main()
