#KT, number guessing game
import random
numbers = random.randint(1,11)
attempts = 0
max_attempts = 6
is_correct = False

print("I'm thinking of a number between 1 and 10. You have 6 tries to guess it!")


while attempts < max_attempts and is_correct == False:
    guess = int(input("enter your guess:"))
    attempts = attempts+1
    if guess == numbers:
        print("you guessed correctly!")
        is_correct = True
    elif guess >= numbers:
        print("To high!")
    else:
        print("To low!")
 
if guess == False:
    print("you lost! the secret number was ", (numbers))

    