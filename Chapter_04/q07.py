# Exercise 7
coin = 0.01
total = 0
print("Small Coin Salary Calculation")

day = int(input("Enter the number of days: "))
while day < 0:
    day = int(input("Enter a positive number: "))

print("Day\tSalary in Rubles")

for num in range(day):
    total += coin
    print("~------------------------~")
    print(f"{num + 1}\t\t{coin}")
    coin *= 2

print(f"\nFinal Total: {total:,.2f}")