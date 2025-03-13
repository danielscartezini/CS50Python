def main():
    plate = input("Plate: ").lower().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    starts_with_two_letters = s[0:2].isalpha()

    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    between_two_and_six = len(s) >= 2 and len(s) <= 6

    #“No periods, spaces, or punctuation marks are allowed.”
    is_string_all_alnum = s.isalnum()

    if starts_with_two_letters and between_two_and_six and is_string_all_alnum:

    #Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
        has_digit = False
        for char in s:
            if char.isdigit():
                if has_digit == False and char == "0":
                    return False
                has_digit = True
            if has_digit and char.isalpha():
                return False

        return True
main()
