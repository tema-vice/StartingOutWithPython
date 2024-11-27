# Exercise 6
def main():
    try:
        count_number = 0
        total_sum = 0
        numbers_file = open('numbers.txt','r')
        for line in numbers_file:
            amount = int(line)
            total_sum += amount
            count_number += 1
        arithmetic_mean = total_sum / count_number
        print(f"The arithmetic mean of numbers in the file is: {arithmetic_mean:.2f}")
    except Exception as error:
        print(error)
    finally:
        numbers_file.close()

main()
