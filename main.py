import turtle
import pandas as pd
from state import State


screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states = states_data["state"].tolist()

guessed_states = []
missing_states = []

count = 0

while count < 50:
    if count == 0:
        answer = screen.textinput(title="Guess The State", prompt="Whats another states name?").title()
    else:
        answer = screen.textinput(title=f"{count}/50 States Correct", prompt="Whats another states name?").title()

    #Exiting The Loop
    if answer == "Exit":
        break

    #Checking The State and Placing it on a map
    if answer in states:
        guessed_states.append(answer)
        coordinate = states_data[states_data.state == answer]
        print(coordinate)
        x_cord = int(coordinate["x"])
        y_cord = int(coordinate["y"])
        state_ = State(x_cord, y_cord, answer)
        count += 1
    else:
        pass

for state in states:
    if state not in guessed_states:
        missing_states.append(state)
df = pd.DataFrame(missing_states)
df.to_csv("Missing_state.csv")

