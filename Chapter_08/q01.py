# Exercise 1
def main():
    user_name = input("Enter your full name to get your initials: ")
    print(get_initials(user_name))

def get_initials(name):
    initials = ''
    list_name = name.split(" ")
    for i in list_name:
        initials = initials + i[0] + '.'
    return initials

main()
