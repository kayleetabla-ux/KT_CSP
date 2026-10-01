#KT, reading and writing to files

with open('practice.txt', "r") as file:
    content = file.read()
    print(content)
    word = content.find("LaRose")
    length = len("LaRose")
    content+= " Treyson!"
    file.write(content)

with open('practice.txt',"a") as file:
    file.write("another line")