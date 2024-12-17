# Exercise 9
def main():
    user_string = input("Enter a string to count the number of vowels and consonants: ")
    print("In the given string:")
    print(f"Vowels:     {get_count_vowel(user_string)}")
    print(f"Consonants: {get_count_consonant(user_string)}")

def get_count_vowel(user_string):
    vowels_tuple = get_vowel_tuple()
    count_vowels = 0
    for ch in user_string:
        if ch.upper() in vowels_tuple:
            count_vowels += 1
    return count_vowels

def get_count_consonant(user_string):
    consonants_tuple = get_consonant_tuple()
    count_consonants = 0
    for ch in user_string:
        if ch.upper() in consonants_tuple:
            count_consonants += 1
    return count_consonants

def get_vowel_tuple():
    vowel_file = None
    vowel_list = []
    try:
        vowel_file = open('vowels.txt', 'r', encoding='UTF-8')
        vowel_list = vowel_file.read().splitlines()
    except Exception as error:
        print(error)
    finally:
        if vowel_file is not None:
            vowel_file.close()
        return tuple(vowel_list)

def get_consonant_tuple():
    consonant_file = None
    consonant_list = []
    try:
        consonant_file = open('consonants.txt', 'r', encoding='UTF-8')
        consonant_list = consonant_file.read().splitlines()
    except Exception as error:
        print(error)
    finally:
        if consonant_file is not None:
            consonant_file.close()
        return tuple(consonant_list)

main()

