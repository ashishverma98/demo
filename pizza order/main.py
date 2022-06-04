##pizza ordering system
bill = 0

print("welcome sir/mam")
size = input("what size pizza do you want to order S M or L? ")
if size == "S":
    print("you have order a small size pizza")
    print("you have to pay 15$.")
    bill = 15

if size == "M":
    print("you have order a medium size pizza")
    print("you have to pay 20$.")
    bill = 20

if size == "L":
    print("you a order a lager size pizza")
    print("you have to pay 25$")
    bill = 25

pepperoni = input("do you want to add Pepperoni? Y for yes/ N for no ")
if pepperoni == "Y":
    print("you have to PAY EXTRA 2$.")
    bill +=2

cheese = input("do you want to add Cheese? Y for yes/ N for no ")
if cheese == "Y":
    print("you have to pay extra 1$.")
    bill +=1

print(f"you total bill is {bill}$")
