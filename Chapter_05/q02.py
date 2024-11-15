# Exercise 2
REGION_TAX = 0.025
FEDERAL_TAX = 0.05

def main():
    price = get_price()

    print(f"Original Price: ${price:,.2f}")

    federal_tax = calculate_federal_tax(price)
    region_tax = calculate_region_tax(price)

    print(f"Federal Tax: ${federal_tax:,.2f}")
    print(f"Regional Tax: ${region_tax:,.2f}")
    print(f"Total Taxes: ${federal_tax + region_tax:,.2f}")
    print(f"Grand Total: ${federal_tax + region_tax + price:,.2f}")


def get_price():
    price = float(input("Enter the item's price: "))
    while price < 0:
        print("Price cannot be negative.")
        price = float(input("Enter the correct price: "))
    return price


def calculate_federal_tax(price):
    return price * FEDERAL_TAX


def calculate_region_tax(price):
    return price * REGION_TAX

main()