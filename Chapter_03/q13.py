# Exercise 13
weight = float(input("Enter the package weight in grams: "))

# If a negative weight is entered, display an error message
if weight < 0:
    print("Please enter valid data.")

elif weight <= 200:
    print(f"Shipping cost: {(weight / 100) * 150:,.2f} rubles.")
elif weight <= 600:
    print(f"Shipping cost: {(weight / 100) * 300:,.2f} rubles.")
elif weight <= 1000:
    print(f"Shipping cost: {(weight / 100) * 400:,.2f} rubles.")
else:
    print(f"Shipping cost: {(weight / 100) * 475:,.2f} rubles.")
