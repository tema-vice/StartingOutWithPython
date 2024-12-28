# Exercise 1
import sqlite3
NUMBER_INCREASE = 1
NUMBER_DECREASE = 2
CITY_NAME = 3
TOTAL_POPULATION = 4
AVG_POPULATION = 5
MAX_POPULATION = 6
MIN_POPULATION = 7
EXIT = 8
def main():
    while True:
        show_menu()
        choice = get_choice()
        if choice == EXIT:
            break
        else:
            sql_select(choice)
    print("Program terminated.")


def show_menu():
    print("----------------------------------------------------------------")
    print("Display:")
    print("1. A list of cities sorted by population in ascending order")
    print("2. A list of cities sorted by population in descending order")
    print("3. A list of cities sort by titles")
    print("4. Display total population")
    print("5. Display average population")
    print("6. Display max population")
    print("7. Display min population")
    print("8. Exit")
    print("----------------------------------------------------------------")

def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < NUMBER_INCREASE or choice > EXIT:
                print("Invalid choice")
            else:
                break
        except Exception as e:
            print("Invalid choice")
    return choice


def sql_select(choice):
    conn = None
    try:
        conn = sqlite3.connect('cities.db')
        c = conn.cursor()
        if choice == NUMBER_INCREASE or choice == MAX_POPULATION:
            c.execute('''SELECT CityName, Population FROM Cities ORDER BY Population DESC''')
        elif choice == NUMBER_DECREASE or choice == MIN_POPULATION:
            c.execute('''SELECT CityName, Population FROM Cities ORDER BY Population ASC''')
        elif choice == CITY_NAME:
            c.execute('''SELECT CityName, Population FROM Cities ORDER BY CityName''')
        elif choice == TOTAL_POPULATION:
            c.execute('''SELECT SUM(Population) FROM Cities''')
        elif choice == AVG_POPULATION:
            c.execute('''SELECT AVG(Population) FROM Cities''')
        show_result(choice, result=c.fetchall())
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if conn is not None:
            conn.close()


def show_result(choice, result):
    if choice == TOTAL_POPULATION:
        print(f"Total population: {result[0][0]}")
    elif choice == AVG_POPULATION:
        print(f"Average population: {result[0][0]}")
    elif choice == MAX_POPULATION:
        print(f"Max population in the city: {result[0][0]}")
    elif choice == MIN_POPULATION:
        print(f"Min population in the city: {result[0][0]}")
    elif choice == NUMBER_INCREASE or choice == NUMBER_DECREASE or choice == CITY_NAME:
        print(f"{'City':17}{'Population':10}")
        print("----------------------------")
        for row in result:
            print(f"{row[0]:17}{row[1]:10}")

main()
