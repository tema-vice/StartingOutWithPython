# Exercise 4
def main():
    show_tooltip()

    total = 0

    for count in range(1, 7):
        total += outlay(count)

    print(f"Total monthly expenses: {total:,.2f} rubles.")
    print(f"Total yearly expenses: {total * 12:,.2f} rubles.")


def show_tooltip():
    print("This program is designed to calculate car expenses.")
    print("Please enter your expenses for:")
    print("1. Monthly loan")
    print("2. Insurance")
    print("3. Gasoline")
    print("4. Engine oil")
    print("5. Tires")
    print("6. Maintenance")


def outlay(count):
    expense = float(input(f"{count}: "))
    while expense < 0:
        print("Expense cannot be negative. Enter again.")
        expense = float(input(f"{count}: "))

    # Return the validated expense
    return expense


main()