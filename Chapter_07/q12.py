# Exercise 12
def main():
    while True:
        try:
            user_number = int(input("Enter a number to determine which numbers up to it are prime: "))
            if user_number < 0:
                print("Negative numbers are not considered.")
            else:
                break
        except ValueError:
            print("Input error.")
    test_list = []
    for list_number in range(0, user_number + 1):
        test_list.append(list_number)
    print("List of prime numbers:")
    for number in test_list:
        if calculated(number):
            print(f"The number {number} is prime.")
        else:
            print(f"The number {number} is composite.")

def calculated(number):
    flag = True
    for num in range(2, number):
        if (number % num == 0):
            flag = False
            break
        else:
            flag = True
    return flag

main()

