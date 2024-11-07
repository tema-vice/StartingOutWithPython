# Exercise 6
# Max days
DAY = 30

print("Magic Date Checker")
day = int(input("Enter the day: "))
month = int(input("Enter the month (as a number): "))
age = int(input("Enter the two-digit year: "))

if day < 1 or month < 1 or age < 0:
    print("Day, month or year cannot be negative.")
elif month > 12:
    print("There can't be more than 12 months!")
elif age > 99:
    print("The year must be two digits!")
else:
    if ((month % 2 == 1) and month < 8) or ((month > 7) and (month % 2 == 0)):
        DAY += 1
    else:
        # Leap year
        if age % 4 == 0:
            DAY -= 1
        else:
            DAY -= 2

    if day > DAY:
        print("There can't be that many days in this month!")
    else:
        if (day * month) == age:
            print(f"{day}.{month}.{age} - Magic date (^~^)")
        else:
            print(f"{day}.{month}.{age} - Not a magic date (*-*)")
