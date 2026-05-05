import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)

def random_color():

    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

turtle_moving = True
steps = 0
directions = [0, 90, 180, 270]
tim.speed(0)
while turtle_moving:
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(5)
    tim.tiltangle(10)


screen = Screen()
screen.setup(width=1, height=1)
