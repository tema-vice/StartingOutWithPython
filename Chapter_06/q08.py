# Exercise 8
def main():
    try:
        total_sum = 0
        count_num = 0
        random_number_file = open('q07_random_number.txt', 'r')
        for line in random_number_file:
            count_num += 1
            amount = int(line)
            print(f"{count_num}: {amount}")
            total_sum += amount
        print(f"Total numbers: {count_num}")
        print(f"Sum of numbers: {total_sum}")
    except Exception as error:
        print(error)
    finally:
        random_number_file.close()

main()
