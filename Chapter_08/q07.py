# Exercise 7
def main():
    results = read_text()
    print(f"The text contains the following counts of different characters:\n"
          f"Uppercase letters:          {results[0]}\n"
          f"Lowercase letters:          {results[1]}\n"
          f"Digits:                     {results[2]}\n"
          f"Spaces:                     {results[3]}\n"
          f"Other symbols:              {results[4]}\n")

def read_text():
    text = open_file()

    count_letter_lower = 0
    count_letter_upper = 0
    count_number = 0
    count_space = 0
    count_other_symbols = 0

    for line in text:
        for ch in line:
            if ch.isdigit():
                count_number += 1
            elif ch.islower():
                count_letter_lower += 1
            elif ch.isupper():
                count_letter_upper += 1
            elif ch.isspace():
                count_space += 1
            else:
                count_other_symbols += 1

    results = [count_letter_upper, count_letter_lower, count_number, count_space, count_other_symbols]
    return results


def open_file():
    file = None
    text = []
    try:
        file = open('text.txt', 'r')
        text = file.read().splitlines()
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()
        return text

main()

