# Exercise 1
MILE_KM = 0.6214

def main():
    km = float(input("Enter the distance in kilometers: "))
    while km < 0:
        print("Kilometers cannot be less than zero")
        km = float(input("Enter the distance in kilometers: "))
    print(miles(km))

def miles(km):
    return f"{km * MILE_KM:.2f}"

main()