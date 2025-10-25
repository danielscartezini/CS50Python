class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"* self.size

    def deposit(self, n):
        n = int(n)
        self._size += n

    def withdraw(self, n):
        n = int(n)
        if n < 0:
            raise ValueError("Cannot withdraw a neganive integer")

        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Capacity must be an integer")
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative number")
        self._capacity = capacity

    @property
    def size(self):
        if self._size > self.capacity:
            raise ValueError("Not enough capacity for deposit")
        return self._size

global_jar = Jar(capacity=10)

def main():
    while True:
        print("\n---- Menu ----")
        print("1- capacity")
        print("2- deposit")
        print("3- withdraw")
        print("4- exit")
        print("--------------\n")

        answer = input("")

        if answer == "1":
            capacity()
        elif answer == "2":
            deposit()
        elif answer == "3":
            withdraw()
        elif answer == "4":
            break


def capacity():
    print(f"Jar capacity: {global_jar.capacity}")
    print(f"Current Cookies: {global_jar}")

def deposit():
    deposit = input("Deposit: ")
    print("\n...\n")
    global_jar.deposit(deposit)
    print(f"You have deposited {deposit} cookies")
    print(f"Current cookies: {global_jar}")

def withdraw():
    withdraw = input("Withdraw: ")
    global_jar.withdraw(withdraw)
    print("\nNom nom nom\n")
    print(f"You had Withdraw {withdraw} cookies")
    print(f"Current cookies: {global_jar}")

if __name__ == "__main__":
    main()
