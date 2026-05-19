import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)
game_is_on = True
all_states = data["state"].tolist()
score = 0
guessed_states = []
last_result = ""
while game_is_on:
    answer_state = screen.textinput(
        title="Guess the State",
        prompt=f"{last_result}\nWhat's another state's name? {len(guessed_states)}/50"
    ).title()
    state_data = data[data["state"] == answer_state]
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        last_result = f"{answer_state} is correct!"
        print(f"Found {answer_state}")
        x = int(state_data["x"].values[0])
        y = int(state_data["y"].values[0])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.write(answer_state)
        guessed_states.append(answer_state)
        score += 1
    else:
        last_result = f"{answer_state} is wrong!"
    if len(guessed_states) == 50:
        game_is_on = False




