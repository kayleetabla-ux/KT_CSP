#KT, nesting

number = 0

while number <= 20:
    print(number)
    number += 2




for number in range(0,21,2):
    print(number)





csp = ["Remy", "Alex", "Gabe", "elsie", "ivan", "caydon", "Kaylee", "levi", "Masen", "william", "Carerra", "Jacob", "Selena", "Ainsley", "Kristian"]
if len(csp)>0:
    for student in csp:
        print(f"checking in {student}")
else:
    print("there is no one in this class.")



while True:
    username = input("what is your username: ").strip()
    password = input("what is your password: ").strip()

    if username == "LaRose" and password == "password":
        print("welcome to the program!")
        break
    else:
        print("Those credentials were incorrect.")