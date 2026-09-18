#KT, string notes

name = 'ms. larose'

print("you can't drive my car.")
      
print('ms. larose told the class "you can\'t drive my car."')
#escape char lets  the program ignore the next character 

#concatenation => add 2 strings together
last_name = 'LaRose'

first_name = "vienna"

name = first_name + " " + last_name

user = input("please tell me your name:\n").strip().title()

print(f"new user recognized\nWelcome {user}")

sentence = "the quick brown fox jumped over the lazy dog"
print(f"the sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", name))