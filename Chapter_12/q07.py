# Exercise 7
def main():
    try:
        while True:
            x = int(input("Enter a integer 'x': "))
            y = int(input("Enter a non-negative integer 'y': "))
            if y < 0:
                print("Number cannot be negative.")
            elif y == 0:
                print("Number cannot be 0.")
            else:
                break
    except Exception:
        print("Invalid input.")
    print(f"Result:")
    print(f"{x}^{y} = {recursive_func(x, y)}")

def recursive_func(x, y):
    if y == 1:
        return x
    else:
        result = recursive_func(x, y - 1)
        result *= x
        return result

main()
