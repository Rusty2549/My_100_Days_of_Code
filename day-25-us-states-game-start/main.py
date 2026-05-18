import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)
game_is_on = True
while game_is_on:

    all_states = data["state"].tolist()


    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    state_data = data[data["state"] == answer_state]
    if answer_state in all_states:

    answer_state.title()

    if answer_state == "Exit" or "exit":
        game_is_on = False


turtle.mainloop()




