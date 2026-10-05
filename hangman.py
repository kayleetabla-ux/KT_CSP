#KT, hangman

import random
with open("hangman.txt","r") as file:
    content = file.read()
    words = content.split(",")
    answer = random.choice(words)


wrong_guesses = 0
guess = 1

def display_man(wrong_guesses):
    if wrong_guesses == 0
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |
        |
        |_____
            """)
    elif wrong_guesses == 1:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |
        |_____
            """)
    elif wrong_guesses == 2:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |    |
        |_____
            """)
    elif wrong_guesses == 3:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |   /|
        |_____
            """)
    elif wrong_guesses == 4:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |   /|\\
        |_____
            """)
    elif wrong_guesses == 5:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |   /|\\
        |___/_
            """)
    elif wrong_guesses == 6:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
        |    |      
        |    O
        |   /|\\
        |___/_\\
            """)
        
for answer



















letter = ""
for letter in word:

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
                word = content.find("win:")
                content+= 1
                win_loss(content)
                print("you won!")
        

                #reference file noes to see how to add to a specific part of the line of hangman_win_loss.txt.
                #add 1 each time.
                #then go back to the video to see how to continue this code. time to continue: 20:53
                
                