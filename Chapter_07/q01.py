# Exercise 1
def main():
    sales_list = [0] * 7
    # Define the names of the days of the week.
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Enter sales for")

    index = 0
    while index < len(sales_list):
        try:
            # Prompt user for sales data for the current day.
            sales_list[index] = int(input(f"{week_list[index]}: "))
            if sales_list[index] < 0:
                # Ensure sales cannot be negative.
                print("Cannot be less than zero. Please try again.")
            else:
                # Move to the next day if input is valid.
                index += 1
        except ValueError:
            print("Input error")

    # Calculate the total sales for the week.
    total = func_sum_list(sales_list)
    print(f"Total sales for the week: {total}")

def func_sum_list(list):
    total = 0
    for item in list:
        total += item
    return total

main()
