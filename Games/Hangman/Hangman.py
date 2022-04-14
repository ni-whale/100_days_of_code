# Step 1

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# TODO-3: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


# TODO-4: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


# TODO-5: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# TODO-6: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# TODO-7: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# TODO-8: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."

import random
import Hangman_art
import Hangman_words

print(Hangman_art.logo)

word_list = Hangman_words.word_list
display = []
end_of_game = False
lives = 6

chosen_word = random.choice(word_list)

for char in range(len(chosen_word)):
    display.append("_")

print(chosen_word)
print(display)
print(Hangman_art.stages[lives])

# while not end_of_game:
#     guess = input("Guess the letter: ").lower()
#
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if guess == letter:
#             display[position] = letter
#         else:
#             # print(stages[lives-1])
#             lives -= 1
#             print(lives)
#     print(display)

while not end_of_game:

    if "_" not in display:
        print("You win!")
        end_of_game = True
        break

    guess = input("Guess the letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
            end_of_game = True

    print(Hangman_art.stages[lives])
    print(f"{' '.join(display)}")


