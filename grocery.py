buy_list = {}

while True:
    try:
        item = input("").strip()
        #counter of the items:
        if item in buy_list:
            buy_list[item]+=1
        else:
            buy_list[item]=1

    except EOFError:
        print()
        #prefixing the counter and the item on every line
        for item in sorted(buy_list):
            print(buy_list[item], item.upper())
        break
