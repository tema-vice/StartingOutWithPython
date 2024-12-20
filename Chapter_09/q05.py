# Exercise 5
def main():
    file = open('8_ball_responses.txt', 'r')
    text = file.read()
    file.close()
    list = text.split()
    exception_list = [',', '.', '!', '?', ':', ';']
    index = 0
    while index < len(list):
        if list[index][-1] in exception_list:
            list[index] = list[index].rstrip(list[index][-1])
        index += 1
    my_set_word = set(list)
    word_count = dict()
    for set_word in my_set_word:
        count = 0
        for list_word in list:
            if list_word == set_word:
                count += 1
        word_count[set_word] = count
    print("List of words and the number of times they occur: ")
    for key, value in word_count.items():
        print(f"Word: {key}\nOccurs once: {value}")

main()
