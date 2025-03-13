def main():
    answer = input("What time it it? ")
    time = convert(answer)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
# convert (e.g., 7:30 -> 7.5)
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)

if __name__ == "__main__":
    main()
