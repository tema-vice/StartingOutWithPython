# Exercise 9
FEDERAL_TAX = 0.05
REGION_TAX = 0.025


def main():
    total_sales = float(input("Enter the total sales for the month: "))
    while total_sales < 0:
        total_sales = float(input("Sales volume cannot be negative: "))

    # Calculate regional sales tax
    region_tax = total_sales * REGION_TAX
    print(f"Regional sales tax amount: {region_tax:,.2f} rubles.")

    # Calculate federal sales tax
    federal_tax = total_sales * FEDERAL_TAX
    print(f"Federal sales tax amount: {federal_tax:,.2f} rubles.")

    # Calculate total tax
    total_tax = region_tax + federal_tax
    print(f"Total tax amount: {total_tax:,.2f} rubles.")


main()
