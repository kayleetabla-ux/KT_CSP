#KT, password strength checker

password = input("what is your password:")

uppercase = False
lowercase = False
number = False
symbol = False
length = False

if len (password)>=8:
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

