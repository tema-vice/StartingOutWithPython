# Exercise 3
def main():
    date = get_user_date()
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    day = date[0]
    month = month_list[date[1] - 1]
    year = date[2]
    print(day, month, year, "year.")


def get_user_date():
    while True:
        user_date = input("Enter the date in the format (dd/mm/yyyy): ")
        if len(user_date) > len("dd/mm/yyyy") or len(user_date) < len("d/m/y"):
            print("The length is incorrect.")
        elif user_date.count("/") > 2:
            print("The number of separators exceeds the allowable value.")
        elif user_date[2] != '/' or user_date[5] != '/':
            print("The separator is incorrect.")
        if check_date(user_date):
            date_list = user_date.split("/")
            index = 0
            while index < len(date_list):
                date_list[index] = int(date_list[index])
                index += 1
            return date_list


def check_date(user_date):
    date_list = user_date.split("/")
    if not date_list[0].isdigit() or not date_list[1].isdigit() or not date_list[2].isdigit():
        print("The date contains non-numeric characters.")
        return False
    index = 0
    while index < len(date_list):
        date_list[index] = int(date_list[index])
        index += 1
    if date_list[0] < 1 or date_list[1] < 1 or date_list[2] < 1:
        print("The date cannot be negative or zero.")
    elif date_list[0] > 31:
        print("The number of days exceeds the allowable value.")
    elif date_list[1] > 12:
        print("The number of months exceeds the allowable value.")
    # Check the relationship between days and months
    # Explanation:
    # The first condition is for April and June, as they cannot have more than 30 days
    # The second condition is for September and November, as they cannot have more than 30 days
    # The third condition is for February in leap years, as it cannot have more than 29 days
    # The fourth condition is for February in non-leap years, as it cannot have more than 28 days
    elif (((date_list[1] % 2 == 0) and (date_list[1] < 7)) and date_list[0] > 30) \
        or (((date_list[1] % 2 != 0) and (date_list[1] > 8)) and date_list[0] > 30) \
        or (((date_list[1] == 2) and date_list[2] % 4 == 0) and (date_list[0] > 29)) \
        or (((date_list[1] == 2) and date_list[2] % 4 != 0) and (date_list[0] > 28)):
        print("This month cannot have that many days.")
    else:
        return True, date_list

main()
