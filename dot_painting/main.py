from turtle import Turtle, Screen, color
import random
import turtle

tim = Turtle()
screen = Screen()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.penup()
tim.goto(-300,-300)

def pattern():
    for i in range(14):
        tim.color(random_color())
        tim.pendown()
        tim.pensize(18)
        tim.forward(3)
        tim.penup()
        tim.forward(40)
        tim.pendown()
        
## not complete





screen.exitonclick()


