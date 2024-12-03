# Exercise 13
import random
def main():
    print("This program simulates a magic ball. Try asking it something!")
    magic_list = []
    create_magic_list(magic_list)
    print("Type 'Stop' to exit.")
    user_choice = input("/: ")
    while user_choice != 'Stop':
        print(f"Magic ball's answer: {random.choice(magic_list)}")
        user_choice = input("/: ")
    print("Thanks for the session!")

def create_magic_list(magic_list):
    answer_file = None
    try:
        answer_file = open('8_ball_responses.txt', 'r')  # , encoding='utf-8')
        for line in answer_file:
            magic_list.append(line.rstrip("\n"))
    except Exception as error:
        print(error)
    finally:
        if answer_file is not None:
            answer_file.close()

main()
