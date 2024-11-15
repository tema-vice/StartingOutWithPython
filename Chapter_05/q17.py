# Exercise 17

def main():
    print("Enter 0 to exit.")
    num = int(input("Enter an integer: "))
    while num != 0:
        if num > 0:
            if is_prime(num):
                print("The number is prime.")
            else:
                print("The number is not prime.")
        else:
            print("The number is negative.")

        num = int(input("\nEnter an integer: "))

    print("Program terminated.")

def is_prime(num):
    for num_0 in range(2, num):  # Check divisors from 2 to (num - 1)
        if num % num_0 == 0:
            return False  # Return False if divisible
    return True  # Return True if no divisors found

main()

