# put all names into a list
names = []
with open("Input/Names/invited_names.txt", "r") as input:
    for name in input.readlines():
        names.append(name.strip())

# get the starting letter
with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_data = letter.read()

    # loop through each name
    for name in names:

        # write the letter and save to output
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output:

            print("Replace name: " + name)
            # replace the letter information with the correct name
            new_letter = letter_data.replace("[name]", name)
            output.write(new_letter)


