# Exercise 12
print("Factorial Calculation")

factorial = int(input("Enter a number to calculate its factorial.\n"))

while factorial <= 0:
    print("Factorial cannot be negative or zero.")
    factorial = int(input("Re-enter the factorial number: "))

print(f"{factorial}! =", end="")
total = 1

for x in range(factorial):
    print(f" {x + 1}", end="")
    if (x + 1) < factorial:
        print(" *", end="")
    total *= (x + 1)

print(f" = {total}", end="")