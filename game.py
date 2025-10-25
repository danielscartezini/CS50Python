import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        print(f'"{level}" is invalid. Put a positive integer.')
        continue
    except ValueError:
        print(f'level must be a number!')
        continue

random_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0 and guess > level:
            print(f'"{guess}" must be between 1 and {level}')
            continue

        if guess < random_num:
            print("Too small!")
        elif guess > random_num:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        print('guess must be a integer')
        continue
