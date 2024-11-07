# Exercise 4
I = "I"
V = "V"
X = "X"

num = int(input("Enter a number from 1 to 10: "))

if num <= 0 or num > 10:
    print("Number out of range")
elif num < 5:
    print(I * (num % 4) + ((I + V) * (num % 1) ** (num % 4)))
elif num < 9:
    print(V + (I * (num % 5)))
else:
    print((I * ((num % 8) % 2)) + X)
