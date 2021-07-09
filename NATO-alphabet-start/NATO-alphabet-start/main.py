import pandas

# TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
list_of_codes = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word: ")
splited_word = [letter.upper() for letter in user_input]
result = [list_of_codes[letter] for letter in splited_word]
print(result)
