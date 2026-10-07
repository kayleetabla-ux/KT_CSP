#KT, hangman

import random
win = ""
loss = ""
wrong_guesses = 0
guess = 1
guessed_letters = ""
guesses = 6
win = 0
loss = 0




with open("hangman.txt","r") as file:
    content = file.read()
    words = content.split(",")
    answer = random.choice(words)


with open("hangman_win_loss.txt", "r") as win_loss:
	for line in win_loss:
		if win in win_loss:
			win = line.split(",")[0]
		elif loss in win_loss:
			loss = line.split(",")[1]


def display_man(wrong_guesses):
    if wrong_guesses == 0:
        print(f"""_____
                        wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|
|
|_____
     """)
    elif wrong_guesses == 1:
        print(f"""_____
                        wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|    O
|
|_____
    """)
    elif wrong_guesses == 2:
        print(f"""_____
                        wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|    O
|    |
|_____
    """)
    elif wrong_guesses == 3:
        print(f"""_____
                        wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|    O
|   /|
|_____
    """)
    elif wrong_guesses == 4:
        print(f"""_____
                    wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|    O
|   /|\\
|_____
    """)
    elif wrong_guesses == 5:
        print(f"""_____
                        wrong_guesses = {wrong_guesses}
|    |                  letters guessed: {guessed_letters}
|    O
|   /|\\
|___/_
    """)
    elif wrong_guesses == 6:
        print(f"""_____
                        wrong_guesses = {wrong_guesses} 
|    |                  letters guessed: {guessed_letters}
|    O
|   /|\\
|___/_\\
    """)
       


def hint(answer, guessed_letters):
    display_word = []
    for letter in answer:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")
    return " ".join(display_word)
    

while guesses <= 6:
    display_man(wrong_guesses)
    print(f"{hint(answer, guessed_letters)}")
    play = input(f"guess #{guess}: ").lower()
    if not play.isalpha() or len(play) != 1:
        print("please enter a single letter")
        continue
    if play in guessed_letters:
        print("you have already guessed that")
        continue
    guess += 1
    guessed_letters += play
    if play not in answer:
        wrong_guesses += 1 
    elif "_" not in hint(answer, guessed_letters):
        print("you won the game!")
        win += 1
        print(f"win:{win}")
        play = input("do you want to play again?:")
    elif wrong_guesses == 6:
        print(f"you lost the game! the secret word was {answer}")
        loss += 1
        print(f"loss:{loss}")
        play = input("do you want to play again?:")
    if play=="yes" or play=="y" or play=="Yes" or play=="Y":
        answer = random.choice(words)
        guessed_letters = ""
        wrong_guesses = 0
        guess = 1
    if play=="no" or play=="n" or play=="No" or play=="N":
        print("thank you for playing!")
        break