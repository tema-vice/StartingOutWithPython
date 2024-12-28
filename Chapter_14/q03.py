# Exercise 3
# Table name
MAJORS = "Majors"
DEPARTMENTS = "Departments"
STUDENTS = "Students"
# Choice table
MIN_CHOICE_TABLE_MENU = 1
MAX_CHOICE_TABLE_MENU = 5
MAJOR_TABLE = 1
DEPARTMENTS_TABLE = 2
STUDENTS_TABLE = 3
SHOW_ALL_DATABASE = 4
EXIT_TABLE_MENU = 5
# Choice action
MIN_CHOICE_MENU = 1
MAX_CHOICE_MENU = 6
SHOW_DATABASE = 1
CREATE = 2
READ = 3
UPDATE = 4
DELETE = 5
EXIT = 6
import sqlite3
def main():
    while True:
        display_table_menu()
        table_choice = get_choice(MIN_CHOICE_MENU, MAX_CHOICE_TABLE_MENU)

        if table_choice == MAJOR_TABLE:
            table_name = MAJORS
        elif table_choice == DEPARTMENTS_TABLE:
            table_name = DEPARTMENTS
        elif table_choice == STUDENTS_TABLE:
            table_name = STUDENTS
        elif table_choice == SHOW_ALL_DATABASE:
            show_all_database()
        elif table_choice == EXIT_TABLE_MENU:
            break
        if table_choice != SHOW_ALL_DATABASE:
            while True:
                display_menu()
                action_choice = get_choice(MIN_CHOICE_MENU, MAX_CHOICE_MENU)

                if action_choice == SHOW_DATABASE:
                    show_database(table_name)
                elif action_choice == CREATE:
                    create(table_name)
                elif action_choice == READ:
                    read(table_name)
                elif action_choice == UPDATE:
                    update(table_name)
                elif action_choice == DELETE:
                    delete(table_name)
                elif action_choice == EXIT:
                    break

    print('Thank you for using program')


def display_table_menu():
    print("----------------------------------------------")
    print("SELECT TABLE")
    print("1. Major Table")
    print("2. Departments Table")
    print("3. Students Table")
    print("4. Show All Database")
    print("5. Exit")
    print("----------------------------------------------")

def display_menu():
    print("----------------------------------------------")
    print("MENU")
    print("1. Show database.")
    print("2. Create new position")
    print("3. Read position")
    print("4. Update position")
    print("5. Delete position")
    print("6. Exit")
    print("----------------------------------------------")

def get_choice(MIN_CHOICE, MAX_CHOICE):
    try:
        while True:
            choice = int(input("Enter your choice: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print("Choice out of range")
            else:
                return choice
    except Exception:
        print("Invalid choice")


def show_database(table_name):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        c.execute(query)
        result = c.fetchall()
        print("Result:", end='')
        for row in result:
            print("\n----------------------------------------------")
            for item in row:
                print(f"{item:^5}", end="")
        print("\n----------------------------------------------")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

def create(table_name):
    print("Create position.\n")
    if table_name == MAJORS:
        name = input("Enter major name: ")
        insert_row(table_name, name, MajorID = None, DeptID = None)
    elif table_name == DEPARTMENTS:
        name = input("Enter department name: ")
        insert_row(table_name, name, MajorID = None, DeptID = None)
    elif table_name == STUDENTS:
        try:
            while True:
                name = input("Enter student name: ")
                MajorID = int(input("Enter major ID: "))
                DeptID = int(input("Enter department ID: "))
                if MajorID < 0 or DeptID < 0:
                    print("Invalid ID")
                else:
                    break
            insert_row(table_name, name, MajorID, DeptID)
        except Exception:
            print("Invalid input.")

def insert_row(table_name, name, MajorID, DeptID):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        if table_name == MAJORS or table_name == DEPARTMENTS:
            query = f"INSERT INTO {table_name} (Name) VALUES (?)"
            params = (name,)
        elif table_name == STUDENTS:
            query = f"INSERT INTO {table_name} (Name, MajorID, DeptID) VALUES (?, ?, ?)"
            params = (name, MajorID, DeptID)
        c.execute(query, params)
        conn.commit()
        print("Position successfully created")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()


def read(table_name):
    print("Read position.\n")
    name = input("Enter name: ")
    num_found = display_item(table_name, name)
    print(f"Found {num_found} item.")
    return num_found

def display_item(table_name, name):
    conn = None
    try:
        result = []
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE Name = ?"
        params = (name,)
        c.execute(query, params)
        result = c.fetchall()
        print("Result:", end='')
        for row in result:
            print("\n----------------------------------------------")
            for item in row:
                print(f"{item:^5}", end="")
        print("\n----------------------------------------------")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()
            return len(result)

def update(table_name):
    print("Update position.\n")
    num_found = read(table_name)
    if num_found > 0:
        try:
            while True:
                id = int(input("Enter id: "))
                name = input("Enter new name: ")
                if table_name == STUDENTS:
                    MajorID = int(input("Enter major ID: "))
                    DeptID = int(input("Enter department ID: "))
                    if DeptID < 0 or MajorID < 0:
                        print("Invalid ID")
                else:
                    MajorID = None
                    DeptID = None
                if id < 0:
                    print("Invalid ID")
                else:
                    break
            update_row(table_name, id, name, MajorID, DeptID)
        except Exception:
            print("Invalid input.")
    else:
        print("No items found.")

def update_row(table_name, id, name, MajorID, DeptID):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        if table_name == MAJORS:
            query = f"UPDATE {table_name} SET Name = ? WHERE MajorID = ?"
            params = (name, id,)
        elif table_name == DEPARTMENTS:
            query = f"UPDATE {table_name} SET Name = ? WHERE DeptID = ?"
            params = (name, id,)
        elif table_name == STUDENTS:
            query = f"UPDATE {table_name} SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID = ?"
            params = (name, MajorID, DeptID, id)
        c.execute(query, params)
        conn.commit()
        if c.rowcount > 0:
            print(f"Position successfully updated.")
        else:
            print(f"No items found.")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

def delete(table_name):
    print("Delete position.\n")
    num_found = read(table_name)
    if num_found > 0:
        try:
            while True:
                id = int(input("Enter id: "))
                if id < 0:
                    print("Invalid ID")
                else:
                    break
            sure = input("Do you want to delete the item? (y/n): ")
            if sure.lower() == "y":
                delete_row(table_name, id)
        except Exception:
            print("Invalid input.")
    else:
        print("No items found.")

def delete_row(table_name, id):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        if table_name == MAJORS:
            query = f"DELETE FROM {table_name} WHERE MajorID = ?"
            params = (id,)
        elif table_name == DEPARTMENTS:
            query = f"DELETE FROM {table_name} WHERE DeptID = ?"
            params = (id,)
        elif table_name == STUDENTS:
            query = f"DELETE FROM {table_name} WHERE StudentID = ?"
            params = (id,)
        c.execute(query, params)
        conn.commit()
        if c.rowcount > 0:
            print(f"Position successfully deleted.")
        else:
            print(f"No items found.")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

def show_all_database():
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('''SELECT Students.StudentID, Students.Name, Majors.Name, Departments.Name
                        FROM Students, Majors, Departments
                        WHERE Students.MajorID = Majors.MajorID
                        AND Students.DeptID = Departments.DeptID''')
        result = c.fetchall()
        print("Result:")
        for row in result:
            print("----------------------------------------------")
            print(f"Student ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Major: {row[2]}")
            print(f"Department: {row[3]}")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

main()