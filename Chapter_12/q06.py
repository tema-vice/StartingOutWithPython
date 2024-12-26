# Exercise 6
def main():
    try:
        while True:
            x = int(input("Enter a non-negative integer 'x': "))
            if x < 0:
                print("Number cannot be negative.")
            elif x == 0:
                print("Number cannot be 0.")
            else:
                break
    except Exception:
        print("Invalid input.")
    print(f"Result: {recursive_func(x)}")

def recursive_func(x):
    if x == 0:
        return 0
    else:
        sum = recursive_func(x - 1)
        sum += x
        return sum

main()
