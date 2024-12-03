# Exercise 7
COUNT_RIGHT_ANSWERS = 15
def main():
    try:
        # Correct answers for the test
        right_answers = (
            'A', 'C', 'A', 'A', 'D',
            'B', 'C', 'A', 'C', 'B',
            'A', 'D', 'C', 'A', 'D',
            'C', 'B', 'B', 'D', 'A'
        )

        # Get student's answers from the file
        student_list = get_student_list()

        error_list = []
        error_counter = 0
        index = 0

        while index < len(right_answers):
            if right_answers[index] != student_list[index]:
                error_counter += 1
                error_list.append(index)
            index += 1

        # Display results
        print("Result...")
        if error_counter > (len(right_answers) - COUNT_RIGHT_ANSWERS):
            print("Exam failed, too many incorrect answers.")
        else:
            print("Exam successfully passed.")
        print(f"Correct answers: {len(right_answers) - error_counter}")
        print(f"Incorrect answers: {error_counter}")

        if error_counter != 0:
            print("Question numbers with incorrect answers:")
            for item in error_list:
                print(item + 1)
    except Exception as error:
        print(error)


def get_student_list():
    test_file = None
    student_answers = []
    try:
        test_file = open('student_solution.txt', 'r')
        for item in test_file:
            student_answers.append(item.rstrip('\n'))
    except Exception as error:
        print(error)
    finally:
        if test_file != None:
            test_file.close()
        return student_answers


main()

