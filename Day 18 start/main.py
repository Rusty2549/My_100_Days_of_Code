from turtle import Turtle, Screen
import random
tim = Turtle()
color = (["red", "blue", "green", "yellow", "purple", "orange", "brown", "black", "aquamarine"])
turtle_moving = True
steps = 0
while turtle_moving:

    forward_back = random.randint(1, 101)
    right_left = random.randint(15,90)


    moves_forward = random.choice([tim.forward, tim.back])
    moves_left_right = random.choice([tim.right, tim.left])
    moves_forward(forward_back)
    moves_left_right(right_left)
    tim.pencolor(random.choice(color))
    steps += 1
    if steps == 50:
        turtle_moving = False



screen = Screen()
screen.exitonclick()
