#KT, password strength checker

password = input("what is your password:")

uppercase = False
lowercase = False
number = False
symbol = False
length = False
increment = 0
feedback = "to make it strong:"
if len(password)>=8:
    length = True
    print(f"at least 8 characters long: {length}")
else:
    print(f"at least 8 characters long : {length}")

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in"$#!?@^%*&":
        symbol = True

print(f"Has a lowercase letter: {lowercase}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
if password==True:
    increment = increment+1
else:
    feedback = feedback+" make your password 8 characters long" 
if uppercase==True:
    increment = increment+1
else:
    feedback = feedback+" add an upercase letter"
if lowercase==True:
    increment = increment+1
else:
    feedback = feedback+" add a lowercase letter"
if number==True:
    increment = increment+1
else:
    feedback = feedback+" add a number"
if symbol==True:
   increment = increment+1
else:
    feedback = feedback+" add a symbol"
if increment==5:
    print("your password strength is: medium")
if increment==1 or increment==2:
    print("your password strength is: weak")
if increment==3 or increment==4:
    print("your password stregth is: strong")
print(feedback)
