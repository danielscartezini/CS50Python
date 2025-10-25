def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(p):
    #“All vanity plates must start with at least two letters.”
    starts_with_two_letters = p[0:2].isalpha()

    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    between_two_and_six_characters = len(p) >= 2 and len(p) <= 6

    #“No periods, spaces, or punctuation marks are allowed.”
    string_is_alnum = p.isalnum()

    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    has_digit = False
    for char in p:
        if char.isdigit():
            if has_digit == False and char == "0":  #cheking if the first number is 0, if yes return False
                return False
            has_digit = True
        if has_digit == True and char.isalpha():
            return False

    if starts_with_two_letters and between_two_and_six_characters and string_is_alnum:
        return True

if __name__ == '__main__':
    main()
