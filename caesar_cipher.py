#KT, caesar cipher

Encript_decript = input("Would you like to (E)ncrypt or (D)ecrypt a message?:")
shift_amount = int(input("enter a shift amount:"))
message = input("Enter your message:")
 
def shift (shift_amount,message):
    words = ""
    for letter in message:
        print(letter)
        if Encript_decript == "e" or Encript_decript == "E":
            if letter.isalpha():
                capitalized = letter.isupper()
                letter = ord(letter)+ shift_amount
                if not capitalized and letter>ord('z'):
                    letter-=26
                letter = chr(letter)
            words+= letter   
            print(letter)
    
        if Encript_decript == "d" or Encript_decript == "D":
            if letter.isalpha():
                capitalized = letter.isupper()
                letter = ord(letter)-shift_amount
                if capitalized and letter>132:
                    letter+=26
                letter = chr(letter)
            words+=letter
            print(letter)
    print(words)



    


  




shift(shift_amount,message)