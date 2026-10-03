#KT, hangman

import random

win_total = 0
loss_total = 0
wrong_guesses = 0
guessed_letters = ""
word =""


with open("hangman.txt","r") as file:
    content = file.read()
    words = content.split(",")
    word = random .choice(word)

"""  _____
    |    |
    |    0
    |   /|\\
    |   / \\
    |_____
"""
def letters_spaces(word,letters):

for word in hangman.txt:
    guess = input("guess a letter:")
    display_word = ""
    if guess in guessed_letters:
        display_word.append(guess)
        print("you already guessed that letter.")
    elif guess not in guessed_letters:
        display_word.append("_")
return display_word

while True:
    def hangman()
