# Exercise 16
import random

def main():
    odd = 0
    even = 0
    print("Numbers from 1 to 1000:")

    # Generate 100 random numbers and classify them as odd or even
    for count in range(100):
        num = random.randrange(1000)  # Generate a random number up to 1000
        print(num)

        # Check if the number is odd or even
        if num % 2 == 1:
            odd += 1  # Increment odd counter if number is odd
        else:
            even += 1  # Increment even counter if number is even

    print(f"Even numbers count: {even}")
    print(f"Odd numbers count: {odd}")

main()
