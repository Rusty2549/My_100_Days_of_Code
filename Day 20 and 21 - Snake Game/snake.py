from turtle import Turtle

STARTING_POS =[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_sqr = []
        self.create_snake()
        self.head = self.all_sqr[0]

    def create_snake(self):
        for position in STARTING_POS:
            new_sqr = Turtle(shape="square")
            new_sqr.penup()
            new_sqr.color("white")
            new_sqr.goto(position)
            self.all_sqr.append(new_sqr)

    def move(self):
        for new_sqr in range(len(self.all_sqr) - 1, 0, -1):
            new_x = self.all_sqr[new_sqr - 1].xcor()
            new_y = self.all_sqr[new_sqr - 1].ycor()
            self.all_sqr[new_sqr].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

