# Exercise 1
def main():
    try:
        while True:
            user_num = int(input("Enter a non-negative integer: "))
            if user_num < 0:
                print("Number cannot be negative.")
            else:
                break
    except Exception as e:
        print("Invalid input.")
    print("Result:")
    recursive_func(user_num)


def recursive_func(user_num):
    if user_num == 1:
        print(user_num, end='')
    else:
        recursive_func(user_num - 1)
        print(user_num, end='')

main()
