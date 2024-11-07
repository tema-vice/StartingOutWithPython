# Exercise 9
num = int(input("Enter the pocket number (0-36): "))
if num >= 0 and num <= 36:
    # Determine the color for pockets 1-10 and 19-28
    if (num > 0 and num <= 10) or (num >= 19 and num <= 28):
        # Odd numbers in these ranges are red, even numbers are black
        if (num % 2) == 1:
            print(f"Red - {num}.")
        else:
            print(f"Black - {num}.")

    # Determine the color for pockets 11-18 and 29-36
    elif (num >= 11 and num <= 18) or (num >= 29 and num <= 36):
        # Odd numbers in these ranges are black, even numbers are red
        if (num % 2) == 1:
            print(f"Black - {num}.")
        else:
            print(f"Red - {num}.")

    # Pocket number 0 is green
    else:
        print(f"Green - {num}.")
else:
    print(f"Invalid number: {num}")
