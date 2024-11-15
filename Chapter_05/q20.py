# Exercise 20
import random

START = 1
EXIT = 0

def main():
    print("Random Number Guessing Game.")
    again = START
    while again != EXIT:
        game()  # Play the game
        again = int(input("Do you want to play again?\n(Yes = 1 | No = 0): "))
    print("Program terminated.")

def game():
    # Core logic of the guessing game
    num = random.randint(1, 100)
    user_num = int(input("Guess a number between 1 and 100.\nEnter '0' to exit.\nYour guess: "))
    count = 1

    while (user_num != num) and (user_num != 0):
        if user_num > num:
            print("Too high, try again!")
        elif user_num < num:
            print("Too low, try again!")
        user_num = int(input("Your guess: "))
        count += 1


    if user_num == 0:
        print()  # Exiting the game
    else:
        print("Congratulations, you won!")
        print(f"Number of attempts: {count}")

main()
