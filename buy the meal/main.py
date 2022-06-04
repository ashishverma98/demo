import random

people = input("enter the names of people? ")
list = people.split()

buyer = random.choice(list)
print(buyer)