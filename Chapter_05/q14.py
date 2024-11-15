# Exercise 14
def main():
    m = float(input("Enter the mass of the object in kilograms: "))
    while m < 0:
        m = float(input("Mass cannot be negative. Please enter again: "))

    v = float(input("Enter the velocity of the object in meters per second: "))
    while v < 0:
        v = float(input("Velocity cannot be negative. Please enter again: "))

    print(kinetic_energy(m, v))


def kinetic_energy(m, v):
    print("K(E) = 1/2mv^2")
    # Calculate kinetic energy using the formula: K = 1/2 * m * v^2
    K = (1 / 2) * m * v ** 2
    return f"Kinetic energy = {K:.2f} Joules."

main()

