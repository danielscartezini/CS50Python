import datetime
import sys
import inflect

p = inflect.engine()

def main():
    date_of_birth = input("Date of Birth: ")
    year, month, day = validate_date_of_birth(date_of_birth)

    date_of_birth = datetime.date(int(year), int(month), int(day))
    diff = datetime.date.today() - date_of_birth
    diff_minutes = diff.days * 24 * 60
    print(p.number_to_words(diff_minutes, andword = "").capitalize() + " minutes")

def validate_date_of_birth(birth):
    try:
        if datetime.datetime.strptime(birth, '%Y-%m-%d'):
            year, month, day = birth.split("-")
            return year, month, day
    except:
        sys.exit("Invalid date.")

if __name__ == "__main__":
    main()
