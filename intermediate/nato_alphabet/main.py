import pandas

# Playing with Pandas dataframes and dictionary comprehensions

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Only letters in the alphabet are accepted.")
        generate_phonetic()

    else:
        print(output)


generate_phonetic()
