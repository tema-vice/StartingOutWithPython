# Exercise 7
import pickle

FILE_NAME = 'employee.dat'
FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW = 5
EXIT = 6

class Employee:
    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Id: {self.__id}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}")
#------------------------------------------------------------------
def main():
    try:
        employee_dict = read_file()
        while True:
            choice = show_menu()
            if choice == FIND:
                find_employee(employee_dict)
            elif choice == ADD:
                add_employee(employee_dict)
            elif choice == CHANGE:
                change_settings(employee_dict)
            elif choice == DELETE:
                delete_employee(employee_dict)
            elif choice == SHOW:
                show_employee(employee_dict)
            elif choice == EXIT:
                break
    except Exception as error:
        print(error)
    finally:
        save_data(employee_dict)
        print("Exiting the program")

def show_menu():
    print("Personal management system")
    print("1. Find an employee\n2. Add a new employee\n3. Change settings\n4. Delete an employee\n5. Show employees\n6. Exit")
    while_flag = True
    while while_flag:
        try:
            choice = int(input("Enter your choice: "))
            if choice > EXIT or choice < FIND:
                print("Invalid choice.")
            else:
                break
        except Exception:
            print("Invalid choice.")
    return choice

# Reading and writing data

def read_file():
    file = None
    employee_dict = dict()
    try:
        file = open(FILE_NAME, 'rb')
        employee_dict = pickle.load(file)
    except Exception as error:
        print(error)
    finally:
        if file != None:
            file.close()
        return employee_dict

def save_data(employee_dict):
    file = open(FILE_NAME, 'wb')
    pickle.dump(employee_dict, file)
    file.close()

# Functions from the menu

def find_employee(employee_dict):
    again = 'y'
    while again.lower() == 'y':
        id = input("Enter employee id: ")
        if id in employee_dict:
            print(employee_dict[id])
        else:
            print("Invalid employee id.")
        again = input("Continue searching? (y/n): ")

def add_employee(employee_dict):
    again = 'y'
    while again.lower() == 'y':
        id = input("Enter employee id: ")
        if id in employee_dict:
            print(f"An employee with this id: {id} - already exists.")
        else:
            name = input("Enter name: ")
            department = input("Enter department: ")
            job_title = input("Enter job title: ")
            employee_dict[id] = Employee(name, id, department, job_title)
        again = input("Continue adding employee? (y/n): ")

def change_settings(employee_dict):
    again = 'y'
    while again.lower() == 'y':
        id = input("Enter employee id: ")
        if id in employee_dict:
            employee_dict[id].set_name(input("Enter new name: "))
            employee_dict[id].set_department(input("Enter new department: "))
            employee_dict[id].set_job_title(input("Enter new job title: "))
        else:
            print("Invalid employee id.")
        again = input("Continue change settings? (y/n): ")

def delete_employee(employee_dict):
    again = 'y'
    while again.lower() == 'y':
        id = input("Enter employee id: ")
        if id not in employee_dict:
            print(f"Invalid employee id.")
        else:
            exactly = input("Delete? (y/n): ")
            if exactly.lower() == 'y':
                del employee_dict[id]
            else:
                print("Not removed.")
        again = input("Continue to remove employees? (y/n): ")

def show_employee(employee_dict):
    print("-----------------------------")
    for i in employee_dict:
        print(employee_dict[i])
        print("-----------------------------")

main()
