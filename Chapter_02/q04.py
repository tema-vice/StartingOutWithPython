# Exercise 4
TAX = 0.07

product_1 = float(input("Enter the price of product 1: "))
product_2 = float(input("Enter the price of product 2: "))
product_3 = float(input("Enter the price of product 3: "))
product_4 = float(input("Enter the price of product 4: "))
product_5 = float(input("Enter the price of product 5: "))

# Calculate
sum = (product_1 + product_2 + product_3 + product_4 + product_5)
tax = sum * TAX
total_sum = sum + tax

print(f"\nCost of goods: {sum:.2f}")
print(f"\nTax: {tax:.2f}")
print(f'\nThe total amount including sales tax: {total_sum:.2f}')
