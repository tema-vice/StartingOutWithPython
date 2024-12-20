# Exercise 3
def main():
    codes = choice_codes()
    user_string = input("Enter the string to convert: ")
    new_string = ""
    for ch in user_string:
        if ch in codes:
            new_string += codes[ch]
        else:
            new_string += ch
    print(f"Original line: {user_string}\nTransformed string: {new_string}")
    new_codes = {value: key for key, value in codes.items()}
    string = ""
    for ch in new_string:
        if ch in new_codes:
            string += new_codes[ch]
        else:
            string += ch
    print(f"Decrypted line: {string}")

def choice_codes():
    ru_codes = {'А': "+", "а": "=", "Б": "_", "б": "-", "В": ")", "в": "0", "Г": "(", "г": "9", "Д": "*", "д": "8",
                "Е": "w", "е": "7", "Ё": "W", "ё": "h", "Ж": "&", "ж": "'", "З": ":", "з": "6", "И": "^", "и": "\"",
                "Й": "%", "й": "5", "К": ";", "к": "4", "Л": "$", "л": "]", "М": "№", "м": "3", "Н": "#", "н": "[",
                "О": "2", "о": "@", "П": "H", "п": "1", "Р": "{", "р": "}", "С": "\\", "с": "/", "Т": "|", "т": "`",
                "У": "~", "у": "j", "Ф": "J", "ф": ">", "Х": "<", "х": "F", "Ц": "f", "ц": "D", "Ч": "d", "ч": "U",
                "Ш": "u", "ш": "L", "Щ": "l", "щ": "T", "Ъ": "t", "ъ": "P", "Ы": "p", "ы": "B", "Ь": "b", "ь": "Q",
                "Э": "q", "э": "R", "Ю": "r", "ю": "K", "Я": "k", "я": "v", "0": "z", "1": "Z", "2": "m", "3": "M",
                "4": "s", "5": "S", "6": "o", "7": "O", "8": "i", "9": "I", ".": "x", ",": "X", " ": "Q"}
    eng_codes = {"A": "+", "a": "=", "B": "_", "b": "-", "C": ")", "c": "0", "D": "*", "d": "8", "E": "е", "e": "7",
                 "F": "Ё", "f": "ё", "G": "&", "g": "'", "H": ":", "h": "6", "I": "^", "i": "\"", "J": "%", "j": "5",
                 "K": ";", "k": "4", "L": "$", "l": "]", "M": "№", "m": "3", "N": "#", "n": "[", "O": "2", "o": "@",
                 "P": "П", "p": "1", "Q": "{", "q": "}", "R": "\\", "r": "/", "S": "|", "s": "`", "T": "~", "t": "у",
                 "U": "Ф", "u": "ф", "V": ">", "v": "<", "W": "Х", "w": "х", "X": "Ц", "x": "ц", "Y": "ч", "y": "Ч",
                 "Z": "ь", "z": "Ь", "1": "Я", "2": "я", "3": "Ы", "4": "ы", "5": "ю", "6": "Ю", "7": "й",
                 "8": "Й", "9": "з", ".": "з", ",": "З", " ": "э"}
    choice = input("Select language: Russian = ru / English = eng: ")
    if choice.lower() == "ru":
        return ru_codes
    else:
        return eng_codes

main()
