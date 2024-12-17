# Exercise 10
def main():
    user_string = input("Enter a string to find the most frequent character: ")
    index = 0
    symbol_list = [user_string[index]]
    count_list = []

    # Collect unique symbols
    while index < len(user_string):
        if user_string[index] not in symbol_list:
            symbol_list.append(user_string[index])
        index += 1

    # Count occurrences for each symbol
    for ch in symbol_list:
        count = 0
        index = 0
        while index < len(user_string):
            if ch == user_string[index]:
                count += 1
            index += 1
        count_list.append(count)

    # Determine the most frequent character
    max_count_index = count_list.index(max(count_list))
    print(f"Most frequent character: {symbol_list[max_count_index]} | {count_list[max_count_index]}")


main()

