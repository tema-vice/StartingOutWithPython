# Exercise 8
TIP = 0.18
TAX = 0.07

many = float(input("Enter the cost of the ordered dishes: "))

print(f"Tip amount for the waiter: {many * TIP:,.2f}")
print(f"Tax amount: {many * TAX:,.2f}")
print(f"Final cost including tip and tax: {many + (many * TAX) + (many * TIP):,.2f}")
