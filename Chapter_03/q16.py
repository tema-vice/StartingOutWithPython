# Exercise 16
age = int(input("Enter the year: "))

# Check if the year is a leap year.
if (((age % 100) == 0) and ((age % 400) == 0)) or (((age % 100) != 0) and ((age % 4) == 0)):
    print(f"In the year {age}, February has 29 days.")
else:
    print(f"In the year {age}, February has 28 days.")
