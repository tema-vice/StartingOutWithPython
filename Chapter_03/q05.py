# Exercise 5
N = 9.8

mass = float(input("Enter the mass of the object: "))
if mass > 0:
    weight = mass * N
    if weight < 500 and weight > 100:
        print(f"Weight = {weight:.2f}")
    elif weight < 100:
        print(f"The object is too light. {weight:.2f}")
    else:
        print(f"The object is too heavy. {weight:.2f}")
else:
    print("Mass cannot be negative.")