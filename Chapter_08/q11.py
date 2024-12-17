# Exercise 11
def main():
    test_string = 'StopAnd SmellTheRoses.LikeLilacsAreBlooming?Yes!'
    print("Test string:", test_string)
    choice = input("Would you like to use the test sentence (y/n)?\n^: ")
    if choice.lower() == 'y':
        user_string = test_string
    else:
        user_string = input("Enter a sentence: ")
    print(f"Transformed sentence: {get_string(user_string)}")

def get_string(user_string):
    user_string = user_string.strip()
    result_string = ""
    index = 0
    while index < len(user_string):

        if user_string[index].isupper() and index != 0:
            if user_string[index - 1].isspace():
                result_string += user_string[index].lower()
            elif user_string[index - 1] in ('.', ',', '!', '?'):
                result_string += ' ' + user_string[index]
            else:
                result_string += ' ' + user_string[index].lower()
        elif user_string[index].isspace():
            result_string += user_string[index]
        elif user_string[index] in ('.', ',', '!', '?'):
            result_string += user_string[index]
        else:
            result_string += user_string[index]
        index += 1
    return result_string

main()



