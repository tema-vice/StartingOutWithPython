# Exercise 11
KILOGRAM = 1.5

weight = float(input("Enter your current weight: "))
while weight <= 0:
    weight = float(input("Weight cannot be less than zero: "))

weight -= KILOGRAM

# Iterate over 6 months
for month in range(6):
    print(f"Month {month + 1}: {weight:.3f} kg")
    weight -= KILOGRAM