from turtle import Screen
import paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.title("Pong")

screen.tracer(0)
game_is_on = True

scoreboard = Scoreboard()
lpaddle = paddle.Paddle((-350, 0))
rpaddle = paddle.Paddle((350, 0))
ball = Ball()
screen.listen()
keys = {"w": False, "s": False, "Up": False, "Down": False}
for key in keys:
    screen.onkeypress(lambda k=key: keys.__setitem__(k, True), key)
    screen.onkeyrelease(lambda k=key: keys.__setitem__(k, False), key)
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if keys["w"]:
        lpaddle.go_up()
    if keys["s"]:
        lpaddle.go_down()
    if keys["Up"]:
        rpaddle.go_up()
    if keys["Down"]:
        rpaddle.go_down()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
