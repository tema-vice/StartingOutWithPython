# Exercise 10
SUGAR = 1.5
OIL = 1
FLOUR = 2.75
ROLL = 48

int_input = int(input("Enter how many rolls you want to bake: "))
percent = int_input / ROLL

print("You will need:")
print(f"{percent * SUGAR:.2f} cups of sugar.")
print(f"{percent * OIL:.2f} cups of oil.")
print(f"{percent * FLOUR:.2f} cups of flour.")
