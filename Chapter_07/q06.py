# Exercise 6
import random
def main():
    random_list = create_list()

    while True:
        try:
            test_user_number = int(input("Enter a number between 1 and 100: "))
            if test_user_number < 1 or test_user_number > 100:
                print("The number is out of range.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"Length of random list: {len(random_list)}")
    print(f"Here are all numbers greater than {test_user_number}:")
    filter_and_print(random_list, test_user_number)


def create_list():
    # Create a list of random integers of random length (1 to 100 elements).
    random_list = [0] * random.randint(1, 100)
    index = 0
    while index < len(random_list):
        random_list[index] = random.randint(1, 100)
        index += 1
    return random_list


def filter_and_print(list, number):
    # Create a new list containing only numbers greater than the given number.
    filtered_list = [item for item in list if item > number]

    index = 0
    while index < len(filtered_list):
        print(filtered_list[index])
        index += 1


main()

