# Exercise 3
def main():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    precipitation_list = []

    print("Enter the amount of precipitation for each month:")
    index = 0

    # Loop through each month and collect user input
    while index < len(month_list):
        try:
            # Get precipitation value for the current month
            precipitation = int(input(f"{month_list[index]}: "))
            if precipitation < 0:
                print("The amount of precipitation cannot be negative.")
            else:
                # Store valid input
                precipitation_list.append(precipitation)
                index += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate total, average, maximum, and minimum precipitation
    total = 0
    for item in precipitation_list:
        total += item

    # Average precipitation
    avg = total / len(precipitation_list)
    # Maximum precipitation
    prec_max = max(precipitation_list)
    # Minimum precipitation
    prec_min = min(precipitation_list)

    print(f"Total precipitation for the year: {total}")
    print(f"Average monthly precipitation: {avg}")
    print(f"Month with maximum precipitation: {month_list[precipitation_list.index(prec_max)]} - {prec_max}")
    print(f"Month with minimum precipitation: {month_list[precipitation_list.index(prec_min)]} - {prec_min}")


main()

