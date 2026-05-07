from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
all_sqr = []
pos = [(0, 0), (-20, 0), (-40, 0)]

for position in pos:
    new_sqr = Turtle(shape="square")
    new_sqr.penup()
    new_sqr.color("white")
    new_sqr.goto(position)
    all_sqr.append(new_sqr)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for new_sqr in range(len(all_sqr) - 1, 0,-1):
        new_x = all_sqr[new_sqr - 1].xcor()
        new_y = all_sqr[new_sqr - 1].ycor()
        all_sqr[new_sqr].goto(new_x, new_y)
    all_sqr[0].forward(20)
    all_sqr[0].left(90)
screen.exitonclick()
