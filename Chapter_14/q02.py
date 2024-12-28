# Exercise 2
MIN_CHOICE = 1
MAX_CHOICE = 6
SHOW_DATABASE = 1
CREATE = 2
READ = 3
UPDATE = 4
DELETE = 5
EXIT = 6
import sqlite3
def main():
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == SHOW_DATABASE:
            show_database()
        elif choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
           update()
        elif choice == DELETE:
            delete()
        elif choice == EXIT:
            break
    print('Thank you for using Phonebook-program')

def display_menu():
    print("----------------------------------------")
    print("MENU")
    print("1. Show database.")
    print("2. Create new position")
    print("3. Read position")
    print("4. Update position")
    print("5. Delete position")
    print("6. Exit")
    print("-----------------------------------------")

def get_menu_choice():
    try:
        while True:
            choice = int(input("Enter your choice: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print("Invalid choice. Please try again.")
            else:
               break
        return choice
    except Exception:
        print("Invalid choice. Please try again.")

def show_database():
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Entries''')
        results = c.fetchall()
        for row in results:
            print("----------------------------------------")
            print(f"Id: {row[0]}\nName: {row[1]}\nPhone: {row[2]}")
            print("----------------------------------------")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

def create():
    print("Creating position.")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_row(name, phone)
    print("Position created successfully.")
    print()

def read():
    print("Reading position.")
    name = input("Enter item name: ")
    num_found = display_item(name)
    print(f"Found {num_found} items.")
    print()
    return num_found

def update():
    num_found = read()
    if num_found != 0:
       try:
            print("Updating position.")
            while True:
                id = int(input("Enter id: "))
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                if id < 0:
                    print("Invalid input value. Please try again.")
                else:
                    break
            results = update_row(id, name, phone)
            if results != 0:
                print("Position updated successfully.")
            else:
                print("Position could not be updated.")
            print()
       except Exception:
            print("Invalid input.")
    else:
        print("No items found.")

def delete():
    num_found = read()
    if num_found != 0:
        try:
            print("Deleting position.")
            while True:
                id = int(input("Enter item id: "))
                if id < 0:
                    print("Invalid input value. Please try again.")
                else:
                    break
            sure = input("Are you sure to delete this number? (y/n): ")
            if sure.lower() == 'y':
                results = delete_row(id)
                if results != 0:
                    print("Position deleted successfully.")
                else:
                    print("Position could not be deleted.")
                print()
            else:
                print("Position not deleted.")
                print()
        except Exception:
            print("Invalid input.")
    else:
        print("No items found.")

def insert_row(name, phone):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''INSERT INTO Entries (Name, Phone)
                            VALUES (?, ?)''', (name, phone))
        conn.commit()
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()

def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Entries WHERE Name == ?''', (name,))
        results = c.fetchall()
        for row in results:
           print(f"Id: {row[0]}\nName: {row[1]}\nPhone: {row[2]}")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()
            return len(results)

def update_row(id, name, phone):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''UPDATE Entries
                        SET Name = ?,
                            Phone = ?
                       WHERE PhoneId == ?''', (name, phone, id))

        results = c.rowcount
        conn.commit()
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()
            return results

def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''DELETE FROM Entries WHERE PhoneId == ?''', (id,))
        results = c.rowcount
        conn.commit()
    except sqlite3.Error as error:
       print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()
            return results

main()
