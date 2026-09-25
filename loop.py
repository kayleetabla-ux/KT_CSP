#KT, loop notes
import random
#code that repeats over and over agin
count=1

while count <= 10:
    print(count)
    count +=1


goose = random.randint(1,11)
ducks=1

while True:
    print("duck")
    if ducks==goose:
        break
    ducks+=1
print("GOOSE!!!")


#list

sibling = ["Tara", "Alaiah", "Maiah"]

print(sibling[2])
print(sibling)
sibling.append("jayshree")
print(sibling)

#add to the list
sibling.insert(3,"vienna")
print(sibling)

#remove item from list
print(sibling)
sibling.pop(3)
print(sibling)

#for loops
for number in range(1,11,2):
    print(number)

for sibling in sibling:
    print (sibling + " Tabla")