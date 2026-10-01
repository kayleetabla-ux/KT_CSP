#KT, Your Budget

income = (float(input("what is your monthly income?:")))
print(income)

rent_mortgage = (float(input("what is your monthly rent/mortgage?:")))
print(rent_mortgage)

utilities = (float(input("what is your monthly utilities?:")))
print(utilities)

groceries = (float(input("what is your monthly grocieries?:")))
print(groceries)

transport = (float(input("what is your monthly transportation?:")))
save = income*.10

print(f"your rent is ${rent_mortgage:.2f} and that is {int(round((rent_mortgage/income)*100))}% of your income")

print(f"your utilities is ${utilities:.2f} and that is {int(round((utilities/income)*100))}% of your income")

print(f"your groceries is ${groceries:.2f} and that is {int(round((groceries/income)*100))}% of your income")

print(f"your transport is ${transport:.2f} and that is {int(round((transport/income)*100))}% of your income")

print(f"you should save ${save} a month, that's 10% of your income")

print(f"You have ${income-(rent_mortgage+utilities+groceries+transport):.2f} of spending money each month!")

