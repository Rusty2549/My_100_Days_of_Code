import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car = None
        self.hideturtle()
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        self.car = Turtle()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.penup()
        self.car.setheading(180)
        self.car.goto(280, random.randint(-250, 250))
        self.car.color(random.choice(COLORS))
        self.all_cars.append(self.car)
    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
