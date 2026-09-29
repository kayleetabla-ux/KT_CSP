#KT, function notes

#round()
#len()
#print()
def stupid_proof(money):
    while True:
        try:
            temp = float(input(f'what is your monthly{money}:'))
            return temp
        except:
            print("that is not a number:")


income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
transportation = stupid_proof("transportation")
groceries = stupid_proof("groceries")
save =  income*.1

#functions go second
def calc_percent(bill, income):
    return round(bill/income * 100)

print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of your income")
print(f"your utilities is ${utilities} which is {calc_percent(utilities, income)}% of your income")
print(f"your transportation is ${transportation} which is {calc_percent(transportation, income)}% of your income")
print(f"your groceries is ${groceries} which is {calc_percent(groceries, income)}% of your income")
print(f"you should save is ${round(income*.1,2)} which is 10% of your income")
print(f"that means you have { income-rent-utilities-transportation-groceries-save} left to spend")

