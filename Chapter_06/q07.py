# Exercise 7
import random
MAX_RANGE = 501

def main():
    while True:
        try:
            user_num = int(input("Enter the number of random numbers to write to the file: "))
            if user_num < 0:
                print("The number cannot be negative!")
                user_num = int(input("Try again: "))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    try:
        random_number_file = open('q07_random_number.txt', 'w')
        for count in range(user_num):
            random_number = random.randrange(MAX_RANGE)
            random_number_file.write(f"{str(random_number)}\n")

        print("Data successfully written to the file.")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        random_number_file.close()

main()


