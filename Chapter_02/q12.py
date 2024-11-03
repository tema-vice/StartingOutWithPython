# Exercise 12
SHARE = 2000
PRICE_SHARE = 40
TAX = 0.03

# Calculate and display
print(f"Total amount paid for the shares: {SHARE * PRICE_SHARE:,.2f}")
print(f"Commission paid to the broker for purchasing shares: {(SHARE * PRICE_SHARE) * TAX:,.2f}")
print(f"Total amount from sold shares: {(2.75 + PRICE_SHARE) * SHARE:,.2f}")
print(f"Commission paid to the broker for selling shares: {((2.75 + PRICE_SHARE) * SHARE) * TAX:,.2f}")
print(f"Total money received as a result: {((2.75 + PRICE_SHARE) * SHARE) - 
                                              (((2.75 + PRICE_SHARE) * SHARE) * TAX) - 
                                              ((SHARE * PRICE_SHARE) * TAX) - 
                                              (SHARE * PRICE_SHARE):,.2f}")
