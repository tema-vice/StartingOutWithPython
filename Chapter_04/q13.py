# Exercise 13
print("Population Growth")
start_count = -1

while (start_count < 0) or (day < 0):
    start_count = int(input("Starting count: "))
    increase = float(input("Enter daily increase (in percent): "))
    day = int(input("Number of days to multiply: "))
    if (start_count < 0) or (day < 0):
        print("Error in input data.")

population = start_count

print("Day\t\tPopulation")

for day_population in range(day):
    print(f"{day_population + 1}\t\t{population:.2f}")
    population *= (1 + (increase / 100))