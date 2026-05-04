import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.hideturtle()
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = r,g,b
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(211, 154, 97), (52, 108, 132), (236, 245, 241), (177, 78, 33), (198, 143, 35),
              (117, 154, 170), (124, 79, 98), (122, 175, 158), (234, 239, 243), (229, 196, 128),
              (192, 86, 107), (55, 39, 20), (11, 51, 64), (193, 123, 142), (54, 121, 116),
              (41, 168, 127), (167, 21, 30), (225, 94, 79), (38, 31, 33), (5, 28, 26), (243, 164, 160),
              (80, 149, 171), (163, 26, 22), (235, 166, 171), (105, 124, 159), (23, 79, 90),
              (171, 207, 189), (158, 205, 214)]

for row in range(10):
    tim.penup()
    tim.goto(-300, row * 50)
    for dot in range(10):
        tim.pencolor(random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()
        tim.dot(20)
        tim.penup()


Screen().exitonclick()

