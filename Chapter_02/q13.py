# Exercise 13
R = float(input("Enter the length of the row in meters: "))
E = float(input("How much space do the end supports occupy in meters: "))
S = float(input("What is the distance between the grapevines in meters: "))

print(f"Number of grapevines that can fit in the row = {(R - 2 * E) / S:.0f}")
