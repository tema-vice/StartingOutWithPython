# Exercise 19

def main():
    p = float(input("Enter the current amount in your account: "))
    while p < 0:
        p = float(input("Please enter a positive number: "))

    i = float(input("Enter the monthly interest rate (x%): "))
    while i < 1:
        i = float(input("Interest rate cannot be negative: "))

    i /= 100  # Convert percentage to decimal

    t = int(input("Enter the number of months the money will remain in the account: "))
    while t < 1:
        t = int(input("Number of months cannot be negative or zero: "))
    print(f"Future balance: {calculate_cost(p, i, t):,.2f} rubles.")


def calculate_cost(p, i, t):
    return p * (1 + i) ** t


main()
