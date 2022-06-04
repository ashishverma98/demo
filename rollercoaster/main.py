print("welcome to the rollercoaster ride")

height = int(input("enter your height? "))

bill = 0

if height >=120:
    print("you are aligible for the ride")

    age = int(input("enter your age? "))

    if age >18:
        print("you can ride")
        print("plz pay $5")
        bill = 5

    if age >20:
        print("plz pay $10")
        bill = 10

    if age >25:
        print("plz pay $15")
        bill = 25


    wants_photo = input("do you want photo? press Y for yes or N for no ") 

    if wants_photo == "Y":
        print("you have to pay extra $3")
        bill += 3

        print(f"your total bill is {bill}")



else:
    print("wait untill your age or height matches with the riders ")