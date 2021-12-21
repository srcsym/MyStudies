N = input()

shoeListAsString = input().split()

shoeListCounter = Counter(shoeListAsString)
CustomNumber=input()
totalPrice=0
for i in range(int(CustomNumber)):
    customer, price = input().split()

    if customer in shoeListCounter.keys() and shoeListCounter[customer] != 0:
        # shoe exists
        shoeListCounter[customer]-=1
        totalPrice+=int(price)




print(totalPrice)
