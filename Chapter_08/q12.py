# Exercise 12
def main():
    user_string = input("Enter a string to convert: ").upper()
    word_list = user_string.split()
    for word in word_list:
        print(word[1:], word[0], "KI ", sep='', end='')

main()

