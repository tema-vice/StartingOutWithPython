# Exercise 11
import random

EXIT = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
LEVEL_5 = 5
END_NUM = 10

def main():
    level = show_menu()
    while level != EXIT:
        num_1 = random.randint(0, END_NUM ** (level + 1))
        print(f"  {num_1}")
        num_2 = random.randint(0, END_NUM ** (level + 1))
        print(f"+ {num_2}")
        print("------------")

        user_num = int(input("Answer: "))
        while user_num != (num_1 + num_2):
            print("Incorrect answer.")
            user_num = int(input("Answer: "))

        print("Correct answer!")
        level = show_menu()


def show_menu():

    print("Math Test.")
    print("0. Exit")
    for count in range(5):
        print(f"{count + 1}. Level ({count + 1}): 0 - {END_NUM ** (count + 2)}")

    level = int(input("Select difficulty level: "))
    while level < 0 or level > 5:
        level = int(input("Invalid selection.\nPlease re-enter: "))

    return level


main()
