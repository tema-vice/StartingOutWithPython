# Exercise 3
keep_going = "n"
many = float(input("Enter your monthly budget: "))
total = 0

# Ensure that the budget is not negative
while many < 0:
    print("The budget cannot be negative.")
    many = float(input("Enter your monthly budget: "))

# Collect expenses until the user confirms no more expenses
while keep_going == "N" or keep_going == "n":
    spending = float(input("Enter your expenses: "))
    total += spending
    keep_going = input("Are these all the expenses for the month (y/n): ")

if many < 0:
    print(f"You've overspent the monthly budget, debt = {many - total:,.2f}")
else:
    print(f"You've saved the monthly budget, remaining balance = {many - total:,.2f}")
