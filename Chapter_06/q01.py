# Exercise 1
def main():
    try:
        number_file = open('numbers.txt','r')
        for line in number_file:
            amount = int(line)
            print(f"{amount}")
    except Exception as error:
        print(error)
    finally:
        number_file.close()
main()
