def main():
    user_input = input("Greeting: ").strip()
    print(f"${value(user_input)}")

def value(greeting):
 
    normalized_input = greeting.lower()

    if normalized_input.startswith("hello"):
        return 0
    elif normalized_input.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
