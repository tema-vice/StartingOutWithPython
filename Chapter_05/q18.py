# Exercise 18
def main():
    # Display all prime numbers in the range from 1 to 100
    print("All prime numbers in the range from 1 to 100:")
    for i in range(1, 101):
        if is_prime(i):
            print(i)

def is_prime(num):
    for num_0 in range(2, num):
        if num % num_0 == 0:
            return False  # Not a prime number
    return True  # Prime number

main()