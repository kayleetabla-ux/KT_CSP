#KT, caesar cipher

Encript_decript = input("Would you like to (E)ncrypt or (D)ecrypt a message?:")
shift_amount = int(input("enter a shift amount:"))
message = input("Enter your message:")
 
def shift (shift_amount,message):
    words = ""
    for letter in message:
        if letter.isalpha():
            letter = ord(letter)+ shift_amount
            letter = chr(letter)
        words+= letter
    print(words)


shift(shift_amount,message)