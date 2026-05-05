from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
keys = {"w": False, "a": False, "d": False, "s": False}
screen.listen()
for key in keys:
    screen.onkeypress(lambda k=key: keys.__setitem__(k, True), key)
    screen.onkeyrelease(lambda k=key: keys.__setitem__(k, False), key)
def clear():
    tim.penup()
    tim.home()
    tim.reset()
def game_loop():
    if keys["w"]:
        tim.forward(18)
    if keys["a"]:
        tim.left(5)
    if keys["d"]:
        tim.right(5)
    if keys["s"]:
        tim.backward(18)
    screen.ontimer(game_loop, 10)
def penup():
    tim.penup()
def pendown():
    tim.pendown()
screen.onkey(key="c", fun=clear)
screen.onkey(key="space", fun=penup)
screen.onkey(key="x", fun=pendown)
game_loop()
screen.mainloop()
screen.exitonclick()
