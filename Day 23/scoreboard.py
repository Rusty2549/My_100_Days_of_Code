from turtle import Screen, Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_level = 1
    def level(self):
        self.penup()
        self.goto(-280, 240)
        self.setheading(90)
        self.write(f"Level: {self.current_level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", font=FONT, align="center")
    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.goto(-280, 240)
        self.write(f"Level: {self.current_level}", font=FONT)

    def you_win(self):
        self.goto(0,0)
        self.write("You Won!", font=FONT, align="center")
