# Exercise 3
# Test file
print('To display the test file, enter: "test_file"\n')

def main():
    file_name = None

    try:
        file_name = input("Enter the name of the file you want to open: ")
        user_file = open(file_name + ".txt", 'r')
        line_number = 1
        for line in user_file:
            line = line.rstrip('\n')
            print(f"{line_number}: {line}")
            line_number += 1

    except Exception as error:
        print(error)

    finally:
        if file_name != None:
            # Close the file
            user_file.close()
            print("The file has been closed")
main()
