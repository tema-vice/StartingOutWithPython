# Exercise 10
FEE = 145000
PERCENT = 0.03

end_fee = FEE * (1 + PERCENT)

for year in range(5):
    print(f"Year: {year + 1}")
    print(f"Payment: {end_fee:,.2f}")
    end_fee *= (1 + PERCENT)