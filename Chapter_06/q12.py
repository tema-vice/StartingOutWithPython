# Exercise 12
DAY_31 = 31  # Number of days in a 31-day month
DAY_30 = 30  # Number of days in a 30-day month
DAY_28 = 28  # Number of days in February (non-leap year)

def main():
    month = 1  # Start from January
    total_step = 0  # Initialize the total number of steps
    count_omission = 0  # Tracks lines already read in the file
    print("Average number of steps per month.")

    try:
        # Iterate through all 12 months
        while month != 13:
            if month == 2:
                # Handle February (28 days)
                month_step, count_omission, total_step = read_file(DAY_28, count_omission, total_step)
                show_month_step(month, month_step)
                month += 1
            elif (month > 0 and month < 8) and (month % 2 != 0):
                # Handle months with 31 days in the first half of the year (Jan, Mar, May, Jul)
                month_step, count_omission, total_step = read_file(DAY_31, count_omission, total_step)
                show_month_step(month, month_step)
                month += 1
            elif (month > 0 and month < 8) and (month % 2 == 0):
                # Handle months with 30 days in the first half of the year (Apr, Jun)
                month_step, count_omission, total_step = read_file(DAY_30, count_omission, total_step)
                show_month_step(month, month_step)
                month += 1
            elif (month > 7 and month < 13) and (month % 2 != 0):
                # Handle months with 30 days in the second half of the year (Sep, Nov)
                month_step, count_omission, total_step = read_file(DAY_30, count_omission, total_step)
                show_month_step(month, month_step)
                month += 1
            else:
                # Handle months with 31 days in the second half of the year (Aug, Oct, Dec)
                month_step, count_omission, total_step = read_file(DAY_31, count_omission, total_step)
                show_month_step(month, month_step)
                month += 1
        print(f"Total number of steps for the year: {total_step:,}")  # Display yearly total
        # Verify total step count
        test_data()
    except Exception as error:
        print(error)

def read_file(const_day, count_omission, total_step):
    try:
        steps_file = open('steps.txt', 'r')
        month_step = 0

        # Skip already read lines
        for omission in range(count_omission):
            steps_file.readline()

        # Read steps for the current month
        for day in range(1, const_day + 1):
            day_step = int(steps_file.readline())
            # Add to yearly total
            total_step += day_step
            # Add to monthly total
            month_step += day_step
            # Increment read line count
            count_omission += 1

        # Calculate monthly average
        month_step /= const_day
        return month_step, count_omission, total_step
    except Exception as error:
        print(error)
    finally:
        steps_file.close()

def show_month_step(month, month_step):
    if month == 1:
        print(f"January: {month_step:.0f}")
    elif month == 2:
        print(f"February: {month_step:.0f}")
    elif month == 3:
        print(f"March: {month_step:.0f}")
    elif month == 4:
        print(f"April: {month_step:.0f}")
    elif month == 5:
        print(f"May: {month_step:.0f}")
    elif month == 6:
        print(f"June: {month_step:.0f}")
    elif month == 7:
        print(f"July: {month_step:.0f}")
    elif month == 8:
        print(f"August: {month_step:.0f}")
    elif month == 9:
        print(f"September: {month_step:.0f}")
    elif month == 10:
        print(f"October: {month_step:.0f}")
    elif month == 11:
        print(f"November: {month_step:.0f}")
    else:
        print(f"December: {month_step:.0f}")

# Sum all steps from the file
def test_data():
    step_file = open('steps.txt', 'r')
    count_step = 0
    for amount in step_file:
        step = int(amount)
        count_step += step
    print(f"Verification step count: {count_step:,}")
    step_file.close()

main()