# Create database phonebook.db
import sqlite3
def main():
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Entries (PhoneID INTEGER PRIMARY KEY NOT NULL,
                                                            Name TEXT,
                                                            Phone TEXT)''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as error:
        print("Database error: ", error)
    except Exception as error:
        print("Error:", error)
    finally:
        if conn != None:
            conn.close()

main()