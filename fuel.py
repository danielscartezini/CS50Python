def main():
    while True:
        try:
            f = input("Fraction: ")

            #split str in two numbers by the '/'
            numerator, denominator = f.split('/', 1)

            numerator = int(numerator)
            denominator = int(denominator)

            #operates the percentage and round two numbers splited
            def percentage(part, whole):
                Percentage = 100* float(part)/float(whole)
                return Percentage

            #raise error in case unsuported input
            if denominator < numerator:
                raise ValueError
            elif denominator == 0:
                raise ZeroDivisionError

            #get porcentage and round it
            percent = round(percentage(numerator, denominator))

            #contitionals and error handling
            if percent <= 10:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")

            #exit the loop if user's input is valid
            break

        except (ZeroDivisionError, ValueError):
            print(f'"{f}" is not a valid fraction.')

main()
