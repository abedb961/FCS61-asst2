salary = float(input("Enter the salary for this month: "))
month = input("Enter the name for this month: ")
svngs = input("Enter the percentage of salary allocated for savings: ")
rnt = input("Enter the percentage of salary allocated for rent: ")
elct = input("Enter the percentage of salary allocated for electricity: ")

savings = salary * float(svngs) / 100
rent = salary * float(rnt) / 100
electricity = salary * float(elct) / 100

print("The amount allocated for savings is: $" + str(savings))
print("The amount allocated for rent is: $" + str(rent))
print("The amount allocated for electricity is: $" + str(electricity))

total = savings + rent + electricity
print("Total spent: $" + str(total))

remainder = salary - total
print(str(remainder) + " remains from the salary")

yearlyCost = (rent + electricity) * 12
print("Your estimated yearly cost is: $" + str(yearlyCost))

a = input("Are you feeling adventurous? (input yes or no): ")
if a == "yes":
    print("Doubling your salary would make it: $" + str(salary ** 2))
else:
    print(":(")

x = input("Do you have any additional savings? (input yes or no): ")
if x == "yes":
    y = float(input("Enter the amount you saved: "))
    print("Congrats, your total savings for this month are: $" + str(savings + y))
else:
    print("Better luck next month!")
