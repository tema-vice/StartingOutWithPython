# Exercise 2
def main():
    user_number = input("Enter a series of numbers without separators (e.g., 3413) to calculate their sum: ")
    # Validate the entered values
    user_number = check_user_number(user_number)
    # Summation
    print(f"Sum of numbers in the string: {get_num_sum(user_number)}")

def check_user_number(user_num):
    check_num_flag = False
    while True:
        for n in user_num:
            if n.isdigit():
                check_num_flag = True
            else:
                check_num_flag = False
                break
        if not check_num_flag:
            user_num = input("The entered string contains a non-digit character. Please try again: ")
        else:
            break
    return user_num

def get_num_sum(user_num):
    total = 0
    for num in user_num:
        total += int(num)
    return total

main()
