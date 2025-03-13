price = 50

#keep looping price, unless < than 0
while price > 0:
    print("Amount Due: ", price, sep="")
#insert coin
    coin = int(input("Insert Coin: "))
#verify if coin is between 5, 10 and 25
    if coin in [25, 10, 5]:
        price = price - coin

print("Change Owed: ", -price, sep="")



