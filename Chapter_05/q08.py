# Exercise 8
PRICE_FOR_WORK = 2000
SQUARE_METERS = 10
WORKING_HOURS = 8


def main():
    area = float(input("Enter the area to be painted in square meters: "))
    while area < 0:
        area = float(input("Area cannot be negative: "))

    if area != 0:
        price_five_liters_paint = float(input("Enter the price of a 5-liter can of paint: "))
        while price_five_liters_paint < 0:
            price_five_liters_paint = float(input("Price cannot be negative: "))

        # Calculate the number of cans needed
        paint_number = calculate_paint_number(area)
        print(f"A total of {paint_number:.0f} can(s) of paint is required.")

        # Calculate working hours and minutes needed for the area
        working_hours, working_minutes = calculate_working_hours(area)
        print(f"For {area} square meters, {int(working_hours)} hours and {working_minutes:.0f} minutes of work are needed.")

        # Calculate paint cost
        price_paint = paint_number * price_five_liters_paint
        print(f"The cost of paint is: {price_paint:,.2f} rubles.")

        # Calculate work cost
        price_work = (int(working_hours) + (working_minutes / 60)) * PRICE_FOR_WORK
        print(f"The cost of labor is: {price_work:,.2f} rubles.")

        # Calculate total cost
        print(f"The total cost of the project is: {price_work + price_paint:,.2f} rubles.")
    else:
        print("The area is zero, so further calculations are unnecessary.")


def calculate_paint_number(area):
    # Calculate the number of paint cans required based on area
    paint_number = (area // SQUARE_METERS)
    if area % SQUARE_METERS > 0:
        return paint_number + 1
    else:
        return paint_number


def calculate_working_hours(area):
    # Calculate the full hours required to cover the given area
    working_hours = (area // SQUARE_METERS) * WORKING_HOURS
    remnant = area % SQUARE_METERS
    if remnant > 0:
        # Calculate the remaining fractional hours needed
        remnant_hours = (remnant / SQUARE_METERS) * WORKING_HOURS
        # Calculate the minutes part of the remaining time
        working_minutes = (remnant_hours % 1) * 60
        return working_hours + remnant_hours, working_minutes
    else:
        return working_hours, remnant


main()
