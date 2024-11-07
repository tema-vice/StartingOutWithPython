# Exercise 1
num = int(input("Enter a number from 1 to 7, and the program will show what day of the week it is:\n"))

if num >= 1 and num <= 7:
    if num == 1:
        print("Monday.")
    elif num == 2:
        print("Tuesday.")
    elif num == 3:
        print("Wednesday.")
    elif num == 4:
        print("Thursday.")
    elif num == 5:
        print("Friday.")
    elif num == 6:
        print("Saturday.")
    else:
        print("Sunday.")
else:
    print("Invalid range.")
