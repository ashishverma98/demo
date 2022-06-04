from multiprocessing import RLock
from random import random


import random

print("WELCOME TO THE ROCK PAPER SCISSOR GAME")

list1= ["rock" , "paper", "scissor" ]

user_input = input("enter user choice rock paper or scissor? ")
print(user_input)
computer_input = random.choice(list1)
print(computer_input)

user_score = 0
computer_score = 0

if user_input == "rock"  and computer_input == "paper":
    computer_score +=1
    print("you lose!")

if user_input == "rock"  and computer_input == "scissor":
    user_score +=1
    print("you win!")

if user_input == "paper"  and computer_input == "scissor":
    computer_score +=1
    print("you lose!")

if user_input == "paper"  and computer_input == "rock":
    user_score +=1
    print("you win!")

if user_input == "scissor"  and computer_input == "rock":
    computer_score +=1
    print("you lose!")

if user_input == "scissor"  and computer_input == "paper":
    user_score +=1
    print("you win!")

if user_input == computer_input:
    print("draw")




