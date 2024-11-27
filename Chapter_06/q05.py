# Exercise 5
def main():
    try:
        total_sum = 0
        numbers_file = open('numbers.txt','r')
        for line in numbers_file:
            amount = int(line)
            total_sum += amount
        print(f"Sum of numbers in file: {total_sum}")
    except Exception as error:
        print(error)
    finally:
        numbers_file.close()

main()
