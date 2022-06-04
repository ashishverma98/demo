from turtle import Turtle, Screen, color
import random

is_race_on = False

screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="user bet", prompt="whic color you want to bet on? ")

color = ["red", "blue", "yellow", "pink", "black", "green", "neon"]
y_postion = [-180, -120, -60, 0, 60, 120, 180]
all_turtles = []

for i in range(6):
    new_turtle=Turtle("turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(-350, y_postion[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 360:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you win!")
            else:
                print("you lose!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)






















screen.exitonclick()