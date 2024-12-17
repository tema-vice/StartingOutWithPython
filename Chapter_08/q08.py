# Exercise 8
# A test sentence: contains periods? yes! and question marks and exclamation points.

def main():
    user_string = input("Enter a string for correction: ")
    word_list, flag_list = redactor_function(user_string)
    show_function(word_list, flag_list)

def redactor_function(string):
    word_list = string.split()
    flag_list = []
    index_word = 0
    while index_word < len(word_list):
        if word_list[index_word][-1] in ('.', '?', '!'):
            flag_list.append(True)
        else:
            flag_list.append(False)
        index_word += 1
    return word_list, flag_list

def show_function(word_list, flag_list):
    index = 0
    word_list[index] = word_list[index].replace(word_list[index], word_list[index].capitalize())
    while index < len(word_list):
        try:
            if flag_list[index]:
                word_list[index + 1] = word_list[index + 1].replace(word_list[index + 1], word_list[index + 1].capitalize())
        except Exception:
            pass
        index += 1
    for word in word_list:
        print(word + ' ', end='')

main()

