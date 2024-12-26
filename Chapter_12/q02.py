# Exercise 2
def main():
    try:
        while True:
            x = int(input("Enter a non-negative integer 'x': "))
            y = int(input("Enter a non-negative integer 'y': "))
            if x < 0 or y < 0:
                print("Number cannot be negative.")
            elif x == 0 or y == 0:
                print("Number cannot be 0.")
            else:
                break
    except Exception as e:
        print("Invalid input.")
    print(f"Result:")
    print(x, '*', y, '= ', end='')
    recursive_func(x, y)

def recursive_func(x, y):
    print(y,end='')
    if x == 1:
        return 0
    else:
        print(' + ',end='')
        recursive_func(x-1, y)

main()
