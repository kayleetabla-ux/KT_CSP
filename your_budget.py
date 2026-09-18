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

print(f"your rent is ${rent_mortgage:.2f} and that is {int(round((rent_mortgage/income)*100))}% of your income")

print(f"your rent is ${utilities:.2f} and that is {int(round((utilities/income)*100))}% of your income")

print(f"your rent is ${groceries:.2f} and that is {int(round((groceries/income)*100))}% of your income")

print(f"your rent is ${transport:.2f} and that is {int(round((transport/income)*100))}% of your income")

print("you should save $300.00 a month, that's 10% of your income")

