print("welcome to the number guessing game")

print("I'm thinking of a number between 1 to 100")

import random


number = random.randint(1,100)
print(number)

lives = 5

game_on = True

while game_on:
    user_guess = int(input("guess a number: "))

    if number==user_guess:
        print(f"you guess the right number: {number}")

    elif number>user_guess:
        print("lower than the number")
        lives-=1
        print(f"you have {lives} left")

    elif number<user_guess:
        print("higher than the number")
        lives-=1
        print(f"you have {lives} left")

    if lives==0:
        game_on=False





