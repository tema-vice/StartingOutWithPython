# create database student_info
import sqlite3
def create_database_student_info():
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY NOT NULL, Name TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY NOT NULL, Name TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY NOT NULL, Name TEXT,
                        MajorID INTEGER, DeptID INTEGER,
                        FOREIGN KEY (MajorID) REFERENCES Majors (MajorID),
                        FOREIGN KEY (DeptID) REFERENCES Departments (DeptID))''')
        conn.commit()
        print("Created tables")
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn != None:
            conn.close()

create_database_student_info()

main()