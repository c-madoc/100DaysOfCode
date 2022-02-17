import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_guesses = []
incorrect_guesses = []  # do something with this after the user has completed?


# while the player hasnt guessed the correct amount of states, play the game
while len(correct_guesses) < 50:
    # Set the text input for the user to guess
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    # Grab the state the user entered
    state = data[data.state == answer_state]

    # Check if we actually collected the data
    if len(state) > 0:
        # add to correct guesses
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)

        # set the naming and how writing to the image should work
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()

        # go to the location of the state
        name.goto(int(state.x), int(state.y))

        # add the state to the image
        name.write(answer_state)

    # If the state wasn't correct, add to incorrect guesses
    else:

        # if the user enters exit
        if answer_state.lower() == "exit":

            # get all the missed states the user didnt get, put into a list
            missed = [x for x in all_states if x not in correct_guesses]

            # create a dict of the missed data
            missed_data = {
                "missed": missed
            }

            # create a datagrame of the missed data
            df = pandas.DataFrame(missed_data)

            # save the missed data to a new csv
            df.to_csv("missed_states.csv")

            # print the summary of how the user did
            print(f"You missed {len(missed)} states\n"
                  f"You got {len(correct_guesses)} states correct\n"
                  f"You entered {len(incorrect_guesses)} wrong answers")
            break

        # add the guess to the incorrect guess list
        incorrect_guesses.append(answer_state)

    print(f"Correct: {correct_guesses}")
    print(f"Wrong:   {incorrect_guesses}")

