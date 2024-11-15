# Exercise 5
CENT = 0.72
PERCENT = 0.60

def main():
    cost = float(input("Enter the property value: "))
    while cost < 0:
        print("Invalid value.")
        cost = float(input("Enter the correct property value: "))

    cost_for_taxes = cost * PERCENT

    print(f"Assessed value for taxation: ${cost_for_taxes:,.2f}")
    tax = calculate_tax(cost_for_taxes)
    print(f"Property tax: ${tax:.2f}")


# Calculation function
def calculate_tax(cost_for_taxes):
    tax_units = cost_for_taxes // 100
    tax = tax_units * CENT
    return tax

main()