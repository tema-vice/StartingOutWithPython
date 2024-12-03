# Exercise 2
import random
# Constants defining the range of numbers and the size of the lottery ticket.
START_NUM = 0
END_NUM = 9
VALUE_LIST = 7

def main():
    # Create a list to store the lottery numbers, initialized with zeros.
    lot_list = [0] * VALUE_LIST
    index = 0
    while index < len(lot_list):
        # Generate a random digit.
        lot_list[index] = random.randint(START_NUM, END_NUM)
        index += 1

    print("Your lottery ticket number: ", end='')
    for item in lot_list:
        print(item, end='')

main()
