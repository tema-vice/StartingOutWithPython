# Exercise 10
SAVE = 1
READ = 2
EXIT = 3

def main():
    print("Program to save and read golf player data.")
    choice = 0
    while choice != EXIT:
        try:
            choice = int(input('1. Save.\n2. Read.\n3. Exit.\n^: '))
            while choice < SAVE or choice > EXIT:
                print("Invalid value.")
                choice = int(input("Please enter again: "))

            if choice == SAVE:
                save()
            elif choice == READ:
                read()
        except ValueError:
            print("Invalid input.")
    print("Exiting program.")

def save():
    while True:
        try:
            # Input player's name and score
            player_name = input("Enter the player's name: ")
            player_score = float(input("Enter the player's score: "))
            if player_score < 0:
                print("Score cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input.")

    try:
        golf_file = open("golf.txt", 'a')
        golf_file.write(f"{player_name}\n")
        golf_file.write(f"{str(player_score)}\n")
        print("Data successfully saved.")
    except Exception as error:
        print(error)
    finally:
        golf_file.close()

def read():
    golf_file = None
    try:
        golf_file = open('golf.txt', 'r')
        player_name = golf_file.readline()
        while player_name != '':
            player_score = float(golf_file.readline())
            player_name = player_name.rstrip("\n")
            print("--------------------")
            # Display player name
            print(f"Name: {player_name}")
            # Display player score
            print(f"Score: {player_score}")
            # Read next player name
            player_name = golf_file.readline()
        print("--------------------")
        print("Data successfully read.")
    except FileNotFoundError:
        print()
        # If the file doesn't exist, ask the user if they want to create it
        create_file = input('The file "golf.txt" does not exist, create it (y/n): ')
        if create_file.lower() == 'y':
            # Create a new empty file
            file = open('golf.txt', 'w')
            file.close()
        else:
            print("Returning to menu.\n")
    except Exception as error:
        print(error)
    finally:
        if golf_file != None:
            golf_file.close()

main()

