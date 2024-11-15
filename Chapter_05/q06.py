# Exercise 6
CARBOHYDRATES = 4
FATS = 9


def main():

    carbohydrates = float(input("Enter how many grams of carbohydrates you consume per day: "))
    while carbohydrates < 0:
        carbohydrates = float(input("Carbohydrates cannot be less than zero: "))

    fats = float(input("Enter how many grams of fat you consume per day: "))
    while fats < 0:
        fats = float(input("Fats cannot be less than zero: "))

    print(f"Calories from carbohydrates: {carbohydrates * CARBOHYDRATES:.2f}")
    print(f"Calories from fats: {fats * FATS:.2f}")

main()