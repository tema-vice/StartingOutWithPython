# Exercise 3
age = float(input("Enter the age: "))

if age < 0:
    print("Age cannot be negative")
elif age <= 1:
    print(f"{age:.1f} - Infant")
elif age < 13:
    print(f"{age:.0f} - Child")
elif age <= 20:
    print(f"{age:.0f} - Teenager")
else:
    print(f"{age:.0f} - Adult")
