# Exercise 6
def main():
    result_list = get_set_text()
    set_text_1 = result_list[0]
    set_text_2 = result_list[1]
    print("List of all unique words in text #1: ", end='')
    for word in set_text_1:
        print(word, '| ', end='')
    print("\nList of all unique words in text #2: ", end='')
    for word in set_text_2:
        print(word, '| ', end='')
    print("\nList of words included in both texts: ", end='')
    for word in set_text_1.intersection(set_text_2):
        print(word, '| ', end='')
    print("\nUnique words, first text: ", end='')
    for word in set_text_1.difference(set_text_2):
        print(word, '| ', end='')
    print("\nUnique words, second text: ", end='')
    for word in set_text_2.difference(set_text_1):
        print(word, '| ', end='')
    print("\nUnique words that appear only in one text: ", end='')
    for word in set_text_1.symmetric_difference(set_text_2):
        print(word, '| ', end='')

def get_set_text():
    file_text_1 = open('python_text_1.txt', 'r')
    file_text_2 = open('python_text_2.txt', 'r')
    text_1 = file_text_1.read()
    text_2 = file_text_2.read()
    file_text_1.close()
    file_text_2.close()
    text_list = [text_1.split(), text_2.split()]
    exception_list = [',', '.', '!', '?', ':', ';', '/']
    result_list = []
    for list in text_list:
        index = 0
        while index < len(list):
            if list[index][-1] in exception_list:
                list[index] = list[index].rstrip(list[index][-1])
            index += 1
        result_list.append(set(list))
    return result_list

main()
