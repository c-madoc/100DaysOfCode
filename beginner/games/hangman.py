import random

# list of potential words for hangman
words = ['hello', 'world', 'testing']

# randomly choose a word to use for the game
word = random.choice(words)

# the users correct guesses
correct = []

# the users incorrect guesses
incorrect = []

# the maximum fails you can have before losing the game
fails = 5


# ask the user to guess a letter
def ask_for_letter():
    return input("Please enter a letter.\n").lower()


# check the users correct guesses against the answer
def check_answer(guess: str):
    guess = guess.lower()

    # if the guess is correct
    if guess in word:
        if guess not in correct:
            correct.append(guess)
            print(f"{guess.upper()} is correct! ")
            return

        print(f"You've already guessed the letter {guess.upper()}! ")
        return

    # if the guess is wrong
    if guess not in incorrect:
        incorrect.append(guess)
        tries = fails - len(incorrect)
        print(f"{guess.upper()} was incorrect. You have {tries} tries remaining.")
        return


# checks if the game should still be continued or not
def continue_game() -> bool:
    tries_remaining = fails - len(incorrect)

    if tries_remaining == 0:
        print("You have 0 remaining tries. You lose!")
        return False

    for letter in word:
        if letter not in correct:
            return True

    print(f"You win! The answer was {word.upper()}.")
    return False


# shows the current progress of the game, showing what you have uncovered.
def show_game():
    reveal_word = ""
    for letter in word:
        if letter not in correct:
            reveal_word += "_"
            continue
        reveal_word += letter.upper()

    print(reveal_word)


# runs the game
def run_game():
    while continue_game():
        show_game()
        guess = ask_for_letter()
        check_answer(guess)


# runs the program
if __name__ == "__main__":
    run_game()
