# Exercise 9
# Constant representing millimeters per year
MM_PER_YEAR = 1.6

print("Water Level Rise Over Years")

for year in range(25):
    water_level_rise = MM_PER_YEAR * (year + 1)
    print(f"{year + 1}: {water_level_rise:.1f} mm")