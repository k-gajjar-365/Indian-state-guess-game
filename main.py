import turtle
import pandas
import time


screen = turtle.Screen()
image = "India-map.gif"

screen.title("Indian States Game")
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("states_data.csv")
all_states = state_data.state.to_list()
guessed_states = []

cords = turtle.Turtle()
cords.hideturtle()
cords.penup()

while not len(all_states)==len(guessed_states):
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} are correct.",prompt="What's the state name to be entered?").title()


    if answer in all_states:
        x = state_data[state_data.state == answer].x.item()
        y = state_data[state_data.state == answer].y.item()
        cords.goto(x,y)
        cords.write(f"{answer}")
        guessed_states.append(answer)
        time.sleep(0.3)

    if answer=="Exit":
        states_to_learn = [state for state in all_states if not state in guessed_states]
        pandas.DataFrame(states_to_learn).to_csv("indian_states_to_learn.csv")
        break

if len(guessed_states) == 29:
    cords.goto(0,0)
    cords.write("YOU DID IT!",move=False,align="center",font=("Courier",40,"bold"))

screen.exitonclick()
