# Exercise 8
# Constants for menu choices
BOYS = 1
GIRLS = 2
BOYS_AND_GIRLS = 3
EXIT = 4

def main():
    # Create lists of popular boy and girl names
    boy_names_list = create_boy_names_list()
    girl_names_list = create_girl_names_list()

    print("Search among the most popular names.")
    print("Choose whose name you want to find.")
    choice = 0
    while choice != EXIT:
        try:
            choice = int(input("1. Boy\n2. Girl\n3. Boy or Girl\n4. Exit\n^: "))
            if choice < BOYS or choice > EXIT:
                print("This menu option does not exist.")

            if choice == EXIT:
                print("Exiting the program.")
            else:
                # Search for the name based on the user's choice
                find_name(choice, boy_names_list, girl_names_list)

        except ValueError:
            print("Input error.")

def create_boy_names_list():
    # Load boy names from a file into a list
    file = None
    boy_names_list = []
    try:
        file = open('BoyNames.txt', 'r')
        for item in file:
            boy_names_list.append(item.rstrip("\n"))
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()
        return boy_names_list

def create_girl_names_list():
    # Load girl names from a file into a list
    file = None
    girl_names_list = []
    try:
        file = open('GirlNames.txt', 'r')
        for item in file:
            girl_names_list.append(item.rstrip("\n"))
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()
        return girl_names_list

def find_name(choice, boy_names_list, girl_name_list):
    user_name = input("Enter the name you are searching for: ")

    # Determine if the search should include both boys' and girls' names
    choice_3_flag = choice == BOYS_AND_GIRLS

    # Search for the name in the relevant list(s)
    name_flag = False
    if (choice == BOYS) or choice_3_flag:
        for name_in_list in boy_names_list:
            if name_in_list == user_name:
                name_flag = True
    if (choice == GIRLS) or choice_3_flag:
        for name_in_list in girl_name_list:
            if name_in_list == user_name:
                name_flag = True


    if name_flag:
        print("The name was found in the list!\n")
    else:
        print("The name does not exist in the list.\n")

main()
