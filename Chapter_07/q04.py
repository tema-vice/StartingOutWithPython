# Exercise 4
def main():
    print("Enter a series of 20 numbers.")
    number_list = []
    i = 0
    while i < 20:
        try:
            number_list.append(float(input(f"#{i+1}: ")))
            i += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"The smallest number in the list: {min(number_list)}")
    print(f"The largest number in the list: {max(number_list)}")
    sum_and_average(number_list)

def sum_and_average(list):
    total = 0
    for num in list:
        total += num
    print(f"The sum of the numbers in the list: {total}")
    print(f"The average of the numbers in the list: {total/len(list):.2f}")

main()

