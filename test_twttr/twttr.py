def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    vowels = "aeiou"
    new_word = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()
