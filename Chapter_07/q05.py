# Exercise 5
NUMBER_LENGTH = 7

def main():
    # Load account numbers from file into a list.
    accounts_list = open_file()

    while True:
        number_user = input("Enter a 7-digit account number: ")
        if len(number_user) != NUMBER_LENGTH:
            print("Invalid account number length. Please try again.")
        else:
            break

    if number_user in accounts_list:
        print(f"The account number '{number_user}' exists.")
    else:
        print("The account number does not exist.")


def open_file():
    accounts_file = None
    accounts_list = []
    try:
        accounts_file = open('charge_accounts.txt', 'r')
        for item in accounts_file:
            accounts_list.append(item.rstrip('\n'))
    except Exception as error:
        print(error)
    finally:
        if accounts_file != None:
            accounts_file.close()
        return accounts_list


main()
