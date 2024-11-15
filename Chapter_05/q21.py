# Exercise 21
import random

STONE = 1
SCISSORS = 2
PAPER = 3
START = 1
EXIT = 0


def main():
    print("Rock, Paper, Scissors Game.")
    again = START
    while again != EXIT:
        game()
        print("-----------------------")
        again = int(input("Do you want to play again?\n(Yes = 1 | No = 0): "))
    print("\nProgram terminated.")


def game():
        while True:
            # Core logic of the game
            computer_choice = random.randint(1, 3)
            user_choice = get_user_choice()

            if user_choice == EXIT:
                break

            # Display choices
            print("-----------------------")
            print(f"Computer's choice: {get_choice(computer_choice)}")
            print(f"Your choice: {get_choice(user_choice)}")
            print("-----------------------")

            if (((computer_choice == STONE) and (user_choice == PAPER))
                    or ((computer_choice == PAPER) and (user_choice == SCISSORS))
                    or ((computer_choice == SCISSORS) and (user_choice == STONE))):
                print("Player wins!")
                break
            elif computer_choice == user_choice:
                print("It's a tie! Let's play another round.\n")
            else:
                print("Computer wins!")
                break

def get_user_choice():
    user_choice = int(input("Make your choice:\n0. Exit.\n1. Stone.\n2. Scissors.\n3. Paper.\n>>>  "))

    while user_choice < 0 or user_choice > 3:
        print("Invalid input.")
        user_choice = int(input("Please try again: "))
    return user_choice

def get_choice(choice):
    # Convert numeric choice to string
    if choice == STONE:
        return "Stone"
    elif choice == SCISSORS:
        return "Scissors"
    elif choice == PAPER:
        return "Paper"


main()
