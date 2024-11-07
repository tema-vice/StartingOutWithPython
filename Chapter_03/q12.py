# Exercise 12
SALES_10 = 0.1
SALES_20 = 0.2
SALES_30 = 0.3
SALES_40 = 0.4
PACK_SALES = 99     # Price per package

pack = int(input("Enter the number of packages purchased: "))
# If a negative number is entered, show the debt owed for negative packages
if pack < 0:
    print(f"You owe us: {(pack * (-1)) * PACK_SALES}$")

elif pack < 10:
    print(f"Purchase amount: {pack * PACK_SALES:,.2f}$")

# Apply a 10% discount for 10 to 19 packages
elif 10 <= pack <= 19:
    print(f"Purchase amount: {pack * PACK_SALES:,.2f}$")
    print(f"Discount amount: {(pack * PACK_SALES) * SALES_10:,.2f}$")
    print(f"Final amount: {(pack * PACK_SALES) - ((pack * PACK_SALES) * SALES_10):,.2f}$")

# Apply a 20% discount for 20 to 49 packages
elif 20 <= pack <= 49:
    print(f"Purchase amount: {pack * PACK_SALES:,.2f}$")
    print(f"Discount amount: {(pack * PACK_SALES) * SALES_20:,.2f}$")
    print(f"Final amount: {(pack * PACK_SALES) - ((pack * PACK_SALES) * SALES_20):,.2f}$")

# Apply a 30% discount for 50 to 99 packages
elif 50 <= pack <= 99:
    print(f"Purchase amount: {pack * PACK_SALES:,.2f}$")
    print(f"Discount amount: {(pack * PACK_SALES) * SALES_30:,.2f}$")
    print(f"Final amount: {(pack * PACK_SALES) - ((pack * PACK_SALES) * SALES_30):,.2f}$")

# Apply a 40% discount for 100 or more packages
else:
    print(f"Purchase amount: {pack * PACK_SALES:,.2f}$")
    print(f"Discount amount: {(pack * PACK_SALES) * SALES_40:,.2f}$")
    print(f"Final amount: {(pack * PACK_SALES) - ((pack * PACK_SALES) * SALES_40):,.2f}$")
