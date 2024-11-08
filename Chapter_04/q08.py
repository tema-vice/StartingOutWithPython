# Exercise 8
print("Sum of Numbers")

num = float(input("Enter positive numbers to calculate their sum.\n"
                  "The program will stop when you enter a negative number.\n"))

total = 0

while num >= 0:
    total += num
    num = float(input("Another number: "))

print("Total Sum:", total)