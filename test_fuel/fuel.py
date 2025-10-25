def main():
    fuel_str = input("Fuel: ")
    fuel_fraction = convert(fuel_str)
    print(gauge(fuel_fraction))


def convert(fuel_str):
    part_str, whole_str = fuel_str.split("/")
    part = int(part_str)
    whole = int(whole_str)

    if whole == 0:
        raise ZeroDivisionError

    if part < 0 or whole < 0:
        raise ValueError
    
    if part > whole:
        raise ValueError

    return round((part / whole) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    return f"{percentage}%"

if __name__ == "__main__":
    main()
