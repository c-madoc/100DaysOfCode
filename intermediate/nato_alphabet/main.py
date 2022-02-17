import pandas

# Playing with Pandas dataframes and dictionary comprehensions

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter: row.code for (index, row) in df.iterrows()}
word = input("Enter a word: ").upper()

phonetics = [nato[letter] for letter in word]
print(phonetics)

