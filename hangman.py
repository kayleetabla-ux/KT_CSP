#KT, hangman

import random

wrong_guesses = 0
correct_guesses
word =""

with open("hangman.txt","r") as file:
    content = file.read()
    words = content.split(",")
    word = random .choice(word)



