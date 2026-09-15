#KT, fixing inputs

#when you want a specific input
while True:
    color = input("tell me a color that is only 1 word").lower().strip
    ()
    if color.isneumeric():
        print(f"I painted your walls {color}!")
    elif " " in color:
        print("I said 1 word")
    else:
        break

# when you want a number
while True:
    try:
        age = int(input("how old are you:"))
        break
    except:
        print("that isn't a number")

print(f"wow you are {age} that is really old!")