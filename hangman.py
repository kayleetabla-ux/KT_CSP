#KT, hangman

import random

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" O ",
                  "   ",
                  "   "),
               2:(" O ",
                  " | ",
                  "   "),
               3:(" O ",
                  "/|",
                  "   "),
               4:(" O ",
                  "/|\\",
                  "  "),
               5:(" O ",
                  "/|\\",
                  "/  "),
               6:(" O ",
                  "/|\\",
                  "/ \\"),}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

with open("hangman.txt","r") as file:
    content = file.read()
    words = content.split(",")
    answer = random.choice(words)
   
    hint = ("_") * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running == True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
        if guess in guessed_letters:
            print(f"you have already guessed {guess}")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            with open("hangman_win_loss.txt", "r") as win_loss:
                content = win_loss.read()
                rate = content.split(",")
                value =
                #reference file noes to see how to add to a specific part of the line of hangman_win_loss.txt.
                #add 1 each time.
                #then go back to the video to see how to continue this code. time to continue: 20:53
                
                