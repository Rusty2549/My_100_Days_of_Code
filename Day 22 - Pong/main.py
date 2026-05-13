from turtle import Screen
import paddle
from ball import Ball
import time
import scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.title("Pong")

screen.tracer(0)
game_is_on = True


lpaddle = paddle.Paddle((-350, 0))
rpaddle = paddle.Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down, "s")

screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down, "Down")

while game_is_on:
    scoreboard.Scoreboard()
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
