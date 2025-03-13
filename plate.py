def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    if s[0:2].isalpha():
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        if len(s) >= 2 and len(s) <= 6:
    #“No periods, spaces, or punctuation marks are allowed.”#
            if s.isalnum:
                return True
    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    have_num = False
    for char in s:
        if char.isdigit():
            have_num == True
            if char.isalpha and have_num:
                return False

    return True


main()



