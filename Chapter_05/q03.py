# Exercise 3
def main():
    cost = float(input("Enter the property value: "))
    while cost < 0:
        cost = float(input("Cost cannot be negative: "))
    print(insurance(cost))


def insurance(cost):
    return f"Minimum insurance cost: ${cost * 0.8:,.2f}"


main()
