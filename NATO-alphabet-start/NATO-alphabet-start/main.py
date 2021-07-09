import pandas

#TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
list_of_codes = {}

for index, row in alphabet_df.iterrows():
    list_of_codes[row.letter] = row.code
# print(list_of_codes)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter the word: ")
splited_word = [letter.upper() for letter in user_input]
# print(splited_word)
result = []
for letter in splited_word:
    for key, code in list_of_codes.items():
        if letter == key:
            result.append(code)
print(result)



