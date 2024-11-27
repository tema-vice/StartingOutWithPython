# Exercise 2
# Test file
print('To display the test file, enter: "test_file"\n')

def main():
    user_file = None
    try:
        file_name = input("Enter the name of the file you want to open: ")
        user_file = open(file_name + ".txt", 'r')
        # Read and print the first 5 lines from the file
        line = user_file.readline()
        for count in range(5):
            # Remove the trailing newline character
            line = line.rstrip('\n')
            if line != "":
                # Print non-empty lines
                print(f"{line}")
            line = user_file.readline()

    except Exception as error:
        print(error)
    finally:
        if user_file != None:
            # Close the file
            user_file.close()
            print("\nThe file has been closed")


main()
