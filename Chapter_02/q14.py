# Exercise 14
print("Program to calculate compound interest income.")

P = float(input("Enter the principal amount you invested at the beginning: "))
r = float(input("Enter the annual interest rate: "))

r = r / 100

n = float(input("Enter the frequency of interest compounding: "))
t = float(input("How many years do you want to earn income: "))

print(f"After {t} years, you will have: {P * ((1 + r / n) ** (n * t)):,.2f}")
