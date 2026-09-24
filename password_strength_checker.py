#KT, password strength checker

password = input("what is your password:")

uppercase = False
lowercase = False
number = False
symbol = False
length = False
increment = 0
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
if {password}==True:
    ({increment}+1)
if {uppercase}==True:
    ({increment}+1)
if {lowercase}==True:
    ({increment}+1)
if {number}==True:
    ({increment}+1)
if {symbol}==True:
    ({increment}+1)
if {increment}==5:
    print("your password strength is: medium")
if {increment}<=2:
    print("your password strength is: weak")
if {increment}==3 or 4:
    print("your password stregth is: strong")
    
