# Exercise 1
print("Error collector.")

total = 0
for day in range(5):
    print("Enter how many errors occurred during the day.")
    print(f"Day {day + 1}: ", end="")
    bug = int(input(""))
    if bug < 0:
        bug = 0
        print("Cannot enter negative number")
    total += bug

print("Total errors:", total)
