# Exercise 13
def main():
    # Read data from the file into a list
    numbers = read_file()
    # Convert the data into a single tuple
    tuple_numbers = convert_to_tuple(numbers)

    # Count how many times each number appears in the lottery
    max_and_min_result_list, max_and_min_count_list = count_numbers(tuple_numbers)

    # Display the top 10 most and least frequent numbers (Task #1 and #2)
    print(f"Top 10 most common numbers:     {ten_maximal(max_and_min_result_list, max_and_min_count_list)}")
    print(f"Top 10 least common numbers:    {ten_minimum(max_and_min_result_list, max_and_min_count_list)}")

    # Separate the regular lottery numbers from PowerBall numbers
    other_numbers, PowerBall_numbers = split_numbers(tuple_numbers)

    # Count occurrences for regular lottery numbers
    other_numbers_result_list, other_numbers_count_list = count_numbers(other_numbers)
    # Count occurrences for PowerBall numbers
    PowerBall_numbers_result_list, PowerBall_numbers_count_list = count_numbers(PowerBall_numbers)

    # Display the 10 most "mature" numbers (Task #3)
    result = [] + other_numbers_result_list
    count = [] + other_numbers_count_list
    print(f"Top 10 most 'mature' numbers:   {ten_minimum(result, count)}")

    # Display the frequency of all numbers (Task #4)
    show_statistics(other_numbers_result_list, other_numbers_count_list, PowerBall_numbers_result_list, PowerBall_numbers_count_list)

def read_file():
    file = None
    numbers = []
    try:
        file = open('pbnumbers.txt', 'r')
        numbers = file.read().splitlines()
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()
        return numbers

def convert_to_tuple(numbers):
    number_list = [item.split() for item in numbers]
    tuple_numbers = []
    index = 0
    while index < len(number_list):
        inside_index = 0
        while inside_index < len(number_list[index]):
            tuple_numbers.append(int(number_list[index][inside_index]))
            inside_index += 1
        index += 1
    return tuple(tuple_numbers)

def count_numbers(tuple_numbers):
    result_list = []
    count_list = []
    index = 0
    while index < len(tuple_numbers):
        if tuple_numbers[index] not in result_list:
            result_list.append(tuple_numbers[index])
            count_index = 0
            count = 0
            while count_index < len(tuple_numbers):
                if tuple_numbers[index] == tuple_numbers[count_index]:
                    count += 1
                count_index += 1
            count_list.append(count)
        index += 1
    return result_list, count_list

def ten_maximal(result_list, count_list):
    maximum = []
    for n in range(10):
        maximum_count_index = count_list.index(max(count_list))
        maximum.append(result_list[maximum_count_index])
        result_list.remove(result_list[maximum_count_index])
        count_list.remove(count_list[maximum_count_index])
    return maximum

def ten_minimum(result_list, count_list):
    minimum = []
    for n in range(10):
        minimum_count_index = count_list.index(min(count_list))
        minimum.append(result_list[minimum_count_index])
        result_list.remove(result_list[minimum_count_index])
        count_list.remove(count_list[minimum_count_index])
    return minimum

def split_numbers(tuple_numbers):
    other_numbers = []
    PowerBall_numbers = []
    index = 0
    count_append = 0
    while index < len(tuple_numbers):
        if count_append == 5:
            PowerBall_numbers.append(tuple_numbers[index])
            count_append = 0
        else:
            other_numbers.append(tuple_numbers[index])
            count_append += 1
        index += 1
    return tuple(other_numbers), tuple(PowerBall_numbers)

def show_statistics(other_numbers_result_list, other_numbers_count_list, PowerBall_numbers_result_list, PowerBall_numbers_count_list):
    print("Statistics for regular numbers:")
    for n in range(len(other_numbers_result_list)):
        minimum_count_index = other_numbers_count_list.index(min(other_numbers_count_list))
        print(f"No.{n+1:^2}| {other_numbers_result_list[minimum_count_index]:^2} - {other_numbers_count_list[minimum_count_index]}")
        other_numbers_result_list.remove(other_numbers_result_list[minimum_count_index])
        other_numbers_count_list.remove(other_numbers_count_list[minimum_count_index])
    print()
    print("Statistics for PowerBall numbers:")
    for n in range(len(PowerBall_numbers_result_list)):
        minimum_count_index = PowerBall_numbers_count_list.index(min(PowerBall_numbers_count_list))
        print(f"No.{n+1:^2}| {PowerBall_numbers_result_list[minimum_count_index]:^2} - {PowerBall_numbers_count_list[minimum_count_index]}")
        PowerBall_numbers_result_list.remove(PowerBall_numbers_result_list[minimum_count_index])
        PowerBall_numbers_count_list.remove(PowerBall_numbers_count_list[minimum_count_index])

main()
