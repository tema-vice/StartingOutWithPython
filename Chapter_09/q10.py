# Exercise 10
def main():
    text, word_list = get_text_and_word()
    word_and_value = get_word_and_value(text, word_list)
    file_create(word_and_value)

def get_text_and_word():
    file_text = open('8_ball_responses.txt', 'r')
    text = file_text.read().splitlines()
    file_text.close()

    index = 0
    word_list = ''
    while index < len(text):
        word_list += text[index] + ' '
        index += 1
    word_list = word_list.split()

    exception_list = [',', '.', '!', '?', ':', ';', '/']
    index = 0
    while index < len(word_list):
        if word_list[index][-1] in exception_list:
            word_list[index] = word_list[index].rstrip(word_list[index][-1])
        index += 1

    index = 0
    while index < len(text):
        for ch in text[index]:
            if ch in exception_list:
                text[index] = text[index].replace(ch, '')
        index += 1
    return text, word_list


def get_word_and_value(text, word_list):
    set_word_list = set(word_list)
    text_split = []
    index = 0
    while index < len(text):
        text_split.append(text[index].split())
        index += 1
    word_and_value = {}
    for word in set_word_list:
        key = word
        num_string = []
        index_offer = 0
        while index_offer < len(text_split):
            index_word = 0
            while index_word < len(text_split[index_offer]):
                text_word = (text_split[index_offer][index_word])
                if word == text_word:
                    num_string.append(index_offer + 1)
                index_word += 1
            index_offer += 1
        word_and_value[key] = num_string
    return word_and_value

def file_create(word_and_value):
    file = open('q10_8_ball_responses.txt', 'w')
    for k, v in sorted(word_and_value.items()):
        file.write(k + ': ')
        for num_string in v:
            file.write(str(num_string) + ' ')
        file.write('\n')
    file.close()

main()