# Exercise 9
import random
class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, number_correct_answer):
        self.__question = question
        self.__answer = {1:answer_1, 2:answer_2, 3:answer_3, 4:answer_4}
        self.__number_correct_answer = number_correct_answer

    def check_answer(self, answer):
        if answer == self.__number_correct_answer:
            print("\n - Correct!")
            return True
        else:
            print("\n - Incorrect!")

    def show_question(self):
        print("----------------------------------------------------------------------\n"
              f"{self.__question}\n"
              f"----------------------------------------------------------------------")
        for key, value in self.__answer.items():
            print(f"{key}) {value}")

def main():
    question_list = get_question_list()
    print("Player number one chooses!")
    count_user_1 = question_func(question_list)
    print("Player number two chooses!")
    count_user_2 = question_func(question_list)
    print(f"Gamer #1: {count_user_1}")
    print(f"Gamer #2: {count_user_2}")
    if count_user_1 > count_user_2:
        print("Player 1 wins!")
    elif count_user_2 < count_user_1:
        print("Player 2 wins!")
    else:
        print("Draw!")

def question_func(question_list):
    count_user = 0
    for num in range(5):
        question = random.choice(question_list)
        question.show_question()
        question_list.remove(question)
        while_flag = True
        while while_flag:
            try:
                user_answer = int(input("Enter your answer: "))
                if user_answer > 4 or user_answer < 1:
                    print("Please enter a number between 1 and 4")
                else:
                    while_flag = False
            except Exception:
                print("Please enter a number between 1 and 4")
        if question.check_answer(user_answer):
            count_user += 1
    return count_user

def get_question_list():
    question_list = [
        Question("What is the capital of Russia?", "Moscow", "Minsk", "Volgograd", "Saint Petersburg", 1),
        Question("25/0.125 = ?", "200", "150", "220", "2000", 1),
        Question("Force is measured in...?", "Truth", "Honor", "Newtons", "Joules", 4),
        Question("Who discovered America?", "Christopher Columbus", "Stalin", "Diego Colon", "Fernando Columbus", 1),
        Question("Who is the president of the world?", "Putin", "Putin V.S.", "Putin Vladimir Vladimirovich", "Vladman P.V.", 3),
        Question("What is the name of the main character in 'Flowers for Algernon' by Daniel Keyes?", "Strauss", "Charlie Gordon", "Algernon", "Joe", 2),
        Question("Who was the first person in space?", "Yuri Gagarin", "Anatoly Ivanov", "Sergey Burunov", "Lyudmila Ezhevskaya", 1),
        Question("How many bits are in a byte?", "1", "8", "4", "16", 2),
        Question("What is the formula for the area of a triangle?", "S = 2 * h/b", "S = a * h/2", "S = (h * 2) / a", "P = a * h/2", 2),
        Question("What type of memory is used for storage in computers?", "SDD/HDD", "HHD/SSD", "SSD/HDD", "HDH/DSD", 3)
    ]
    return question_list


main()
