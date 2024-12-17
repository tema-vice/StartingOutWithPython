# Exercise 4
def main():
    print("The program converts text encoding using Morse code.")
    user_string = input("Enter string value: ")
    Morse_code_tuple = get_Morse_code_tuple()
    string_in_Morse_code = create_Morse_code_string(Morse_code_tuple, user_string)
    print(string_in_Morse_code)


def get_Morse_code_tuple():
    Morse_code_file = open("Morse_code.txt", 'r', encoding= 'utf-8')
    list = Morse_code_file.readlines()
    index = 0
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    list = tuple(list)
    return list

def create_Morse_code_string(Morse_code_tuple, user_string):
    string_in_Morse_code = ''
    for ch in user_string:
        if ch.upper() in Morse_code_tuple:
            ch_code_index = Morse_code_tuple.index(ch.upper()) + 1
            string_in_Morse_code += Morse_code_tuple[ch_code_index]
        elif ch == ' ':
            string_in_Morse_code += '   '
        else:
            string_in_Morse_code += ch
        string_in_Morse_code += " "
    return string_in_Morse_code

main()