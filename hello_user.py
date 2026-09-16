#KT, hello user

while True:
    name = input("tell me your name:")
    if name.isnumeric():
        print("that isn't a name")
    else:
        break

print(f"hello {name}!")

