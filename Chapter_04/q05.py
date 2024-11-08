# Exercise 5
print("Average Rainfall Thickness")

year = int(input("Enter the number of years: "))
# Validate that the entered value is positive
while year <= 0:
    print("The number of years cannot be negative.")
    year = int(input("Enter the number of years: "))

total = 0

for num in range(year):
    print(f"Year {num + 1}\n\\~~~~~~~/")
    for month in range(12):
        print("Enter the amount of rainfall for this month.")
        print(f"Month {month + 1}: ", end="")
        rain = float(input())
        # Validate that the entered value is non-negative
        while rain < 0:
            rain = float(input("The amount of rainfall cannot be negative. Please try again: "))
        total += rain

print(f"Total number of months: {year * 12}")
print(f"Total amount of rainfall: {total}")
print(f"Average rainfall thickness: {total / (year * 12):.2f}")

