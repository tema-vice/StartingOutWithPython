# Exercise 8
import pickle

SEARCH = 1
ADD = 2
UPDATE = 3
DELETE = 4
SHOW = 5
EXIT = 6

def main():
    mail_base = read_file()
    print("Email Address Book.")
    while True:
        choice = show_menu()
        if choice == SEARCH:
            address_search(mail_base)
        elif choice == ADD:
            mail_base = add_address(mail_base)
        elif choice == UPDATE:
            mail_base = update_address(mail_base)
        elif choice == DELETE:
            mail_base = del_address(mail_base)
        elif choice == SHOW:
            show_all_address(mail_base)
        elif choice == EXIT:
            break
    write_file(mail_base)
    print("Program exiting.")

def read_file():
    file = None
    mail_base = {}
    try:
        file = open('email.dat', 'rb')
        mail_base = pickle.load(file)
    except FileNotFoundError:
        print("File not found.")
    finally:
        if file is not None:
            file.close()
    return mail_base

def write_file(mail_base):
    file = open('email.dat', 'wb')
    pickle.dump(mail_base, file)
    file.close()

def show_menu():
    print("1. Search for an address.\n"
          "2. Add a new entry.\n"
          "3. Update an address.\n"
          "4. Delete an address.\n"
          "5. Show all addresses.\n"
          "6. Save file and exit the program.")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if (choice < SEARCH) or (choice > EXIT):
                print("Invalid menu choice.")
            else:
                break
        except Exception:
            print("Input error.")
    return choice

def address_search(mail_base):
    while True:
        key = input("Enter the username: ")
        if key in mail_base:
            print(f"Name: {key}")
            print(f"Email: {mail_base[key]}")
            print()
        else:
            print("Not found.")
        again = input("Do you want to search again? (y/n)\n^: ")
        if again.lower() != "y":
            break

def add_address(mail_base):
    while True:
        key = input("Enter the username: ")
        value = input("Enter the email address: ")
        if key in mail_base:
            print("This name already exists in the database.")
        elif not '@' in value:
            print("\nPlease enter a valid email address (with @).\n")
        elif "@" == value[-1]:
            print("Domain name is missing.")
        elif "@" == value[0]:
            print("Username is missing.")
        else:
            mail_base[key] = value
        again = input("Do you want to add more data? (y/n)\n^: ")
        if again.lower() != "y":
            break
    return mail_base

def update_address(mail_base):
    while True:
        key = input("Enter the username: ")
        if key in mail_base:
            while True:
                value = input("Enter the new email address: ")
                if not '@' in value:
                    print("\nPlease enter a valid email address (with @).\n")
                elif "@" == value[-1]:
                    print("Domain name is missing.")
                elif "@" == value[0]:
                    print("Username is missing.")
                else:
                    mail_base[key] = value
                    print("Entry updated.")
                    break
        else:
            print("Not found.")
        again = input("Do you want to make more updates? (y/n)\n^: ")
        if again.lower() != "y":
            break
    return mail_base

def del_address(mail_base):
    while True:
        key = input("Enter the username: ")
        if key in mail_base:
            del mail_base[key]
            print("Entry deleted.")
            print()
        else:
            print("Not found.")
        again = input("Do you want to delete more entries? (y/n)\n^: ")
        if again.lower() != "y":
            break
    return mail_base

def show_all_address(mail_base):
    print("All email addresses:")
    for key, value in mail_base.items():
        print(f"Name: {key}")
        print(f"Email: {value}")
        print()

main()

