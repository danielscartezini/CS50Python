import random

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    choices = [1,2,3]
    print(random.choice(choices))


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    if not s[0:2].isalpha():
        return False

    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not (2 <= len(s) <= 6):
        return False

    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    have_num = False
    for char in s:
        if char.isdigit():
            if char == '0':
                return False
            have_num = True
            if char.isalpha() and have_num == True:
                return False

    #“No periods, spaces, or punctuation marks are allowed.”
    if not s.isalnum():
        return False

    return True

main()
