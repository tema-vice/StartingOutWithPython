# Exercise 6
REGION_TAX = 0.025
FEDERAL_TAX = 0.05

product = float(input("Enter the price of the product: "))

print(f'Product price: {product:,.2f}')
print(f"Federal sales tax: {product * FEDERAL_TAX}")
print(f"Regional sales tax: {product * REGION_TAX}")
print(f"Total sales tax: {(product * FEDERAL_TAX) + (product * REGION_TAX)}")
print(f"Final price including taxes: {product + (product * FEDERAL_TAX) + (product * REGION_TAX)}")
