# Exercise 4
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
    my_set = set(list)
    print(f"List of all unique words: ", end='')
    for word in my_set:
        print(word, '| ', end='')

main()
