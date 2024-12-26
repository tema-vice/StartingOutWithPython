# Exercise 8
def main():
    try:
        while True:
            m = int(input("Enter a non-negative integer 'm': "))
            n = int(input("Enter a non-negative integer 'n': "))
            if m < 0 or n < 0:
                print("Number cannot be negative.")
            else:
                break
    except Exception:
        print("Invalid input.")
    print(f"Ackerman: {ackerman(m, n)}")

def ackerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return m + 1
    else:
        return ackerman(m - 1, ackerman(m, n - 1))

main()