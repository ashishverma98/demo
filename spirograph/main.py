from turtle import Turtle, Screen, color
import random
import turtle
tim= Turtle()
screen = Screen()
tim.speed("fastest")

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size):
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size)

draw_spirograph(2)
    






screen.exitonclick()