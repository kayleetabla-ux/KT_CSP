#KT, number guessing game
import random
numbers = random.randint(1,11)

print("I'm thinking of a number between 1 and 10. You have 6 tries to guess it!")

Guess1 = int(input("Guess1:"))

while True:
    if numbers == Guess1:
        break
        print("Correct")
