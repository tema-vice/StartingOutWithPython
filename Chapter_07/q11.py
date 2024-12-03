# Exercise 11
def main():
    print("This program determines whether a square is magic or not.")
    while True:
        try:
            value = int(input("Enter the length of any side of the square: "))
            if value < 0:
                print("The number cannot be negative.")
            else:
                break
        except ValueError:
            print("Input error.")

    user_list = []
    for r in range(value):
        user_list.append([])
        for c in range(value):
            while True:
                try:
                    number = int(input(f"Enter the value for positions |{r}|{c}|: "))
                    break
                except ValueError:
                    print("Input error.")
            user_list[r].append(number)
    magic_function(user_list)


def magic_function(user_list):
    checklist = []
    # 'checklist' - list where verification values will be saved after summation, where:
    # indices from 0 to n(rows - 1) are the sums of rows
    # indices from n(rows - 1) to (n(rows - 1) + n(columns)) are the sums of columns
    # indices from (n(rows - 1) + n(columns)) to ((n(rows - 1) + n(columns)) + 2) are the sums of two diagonals
    # Summing rows
    horizontal_sum(user_list, checklist)
    # Summing columns
    vertical_sum(user_list, checklist)
    # Summing diagonals
    diagonal_sum(user_list, checklist)
    # Checking
    flag = True
    index = 0
    while index < len(checklist):
        if index != (len(checklist) - 1):
            if checklist[index] != checklist[index + 1]:
                flag = False
        else:
            if checklist[index] != checklist[index - 1]:
                flag = False
        #print(f"Cycle iteration: {index}\nFlag state: {flag}")
        index += 1
    if flag:
        print("This square is magic, the sums are equal.")
    else:
        print("This square is not magic, the sums are not equal.")


def horizontal_sum(user_list, checklist):
    total = 0
    for row in user_list:
        for item in row:
            total += item
        checklist.append(total)
        total = 0

def vertical_sum(user_list, checklist):
    total = 0
    for col in range(len(user_list)):
        for item in range(len(user_list)):
            total += user_list[item][col]
        checklist.append(total)
        total = 0

def diagonal_sum(user_list, checklist):
    total_1_diagonal = 0
    total_2_diagonal = 0
    for item in range(len(user_list)):
        total_1_diagonal += user_list[item][item]
        total_2_diagonal += (user_list[item][len(user_list) - 1 - item])
    checklist.append(total_1_diagonal)
    checklist.append(total_2_diagonal)

main()
