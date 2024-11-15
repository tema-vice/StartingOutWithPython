# Exercise 10
FEET_INCHES = 12

def main():
    print("This program converts feet to inches.")
    feet = float(input("Enter the number of feet: "))
    while feet < 0:
        feet = float(input("Number of feet cannot be negative: "))

    print(f"In {feet:.2f} feet, there are {feet_to_inches(feet):.2f} inches.")


def feet_to_inches(feet):
    return feet * FEET_INCHES


main()
