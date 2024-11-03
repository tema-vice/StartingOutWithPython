# Exercise 3
ACRE_METER = 4046.86
meter = float(input("Enter the total number of square meters:\n"))

# Convert square meters to acres
acre = meter / ACRE_METER

print(f"This amount of square meters: {meter:,} "
      f"\nis equivalent to this amount of acres: {acre:,.2f}")
