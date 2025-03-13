months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def month_is_alpha(MM, DD, YYYY):
    if MM in months:
        MM_index = months.index(MM) + 1    # MM_index count the position of the month ("+1" because the count starts with zero)
        print(f"{YYYY}-{MM_index}-{DD}")    # print in date in "YYYY-MM-DD" format
    else:
        print(f'Invalid format: "{MM}" is not a month')

def month_is_digit(MM, DD, YYYY):
    if MM.isdigit() and DD.isdigit and YYYY.isdigit():
        print(f"{YYYY}-{MM}-{DD}")
    else:
        print("Invalid format.")

def main():
    while True:
        date_input = input("Date: ").title()

        #check if the input contains slash (as e.g., MM/DD/YYYY)
        if '/' in date_input:
            month, day, year = date_input.split('/')
            month_is_digit(month, day, year)
            break

        #check if the input contain a space and comma (e.g., Month Day, Year)
        elif ',' in date_input and " " in date_input:
            month, day, year = date_input.replace(',','').split()
            month_is_alpha(month, day, year)
            break

        else:
            print('Please "MM/DD/YYYY" or "Month Day, Year" format.')

main()
