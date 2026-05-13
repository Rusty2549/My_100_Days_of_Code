from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    def go_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)
    def go_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)
