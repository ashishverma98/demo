from turtle import Turtle, Screen
import turtle
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
postion = [[(380,20), (380,0), (380,-20)],[(-385,20), (-385,0), (-385,-20)]]

turtle.tracer(0)

for  i in range(0,2):
    for item in range(0,3):
        tim = Turtle()
        tim.speed("fastest")
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(postion[i][item])



tim = Turtle("circle")
tim.color("white")
screen.update()
for i in range(0,400):
    tim.penup()
    tim.goto(i,i)

# time.sleep(0.1)





















screen.exitonclick()