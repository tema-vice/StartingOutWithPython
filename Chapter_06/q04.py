# Exercise 4
def main():
    try:
        count = 0
        names_file = open('names.txt','r')
        for line in names_file:
            name = line.rstrip("\n")
            count += 1
        print(f"Number of names in file: {count}")
    except Exception as error:
        print(error)
    finally:
        names_file.close()

main()
