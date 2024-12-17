# Exercise 14
def main():
    date, price = read_file()

    # Calculate the average price per year (Task #1)
    avg_price_year_result = avg_price_year(date, price)
    show_result_avg_price_year(avg_price_year_result)
    print()
    # Calculate the average price per month (Task #2)
    avg_price_month_result = avg_price_month(date, price)
    show_result_avg_price_month(avg_price_month_result)
    print()
    # Find the highest and lowest prices in a year (Task #3)
    max_and_min_price_year_result = max_and_min_price_year(date, price)
    show_result_max_and_min_price_year(max_and_min_price_year_result)
    print()
    # Create files sorted in ascending and descending order (Task #4 and #5)
    create_new_file(date, price)


def read_file():
    file = None
    data = []
    try:
        file = open('GasPrices.txt', 'r')
        data = file.read().splitlines()
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()

    date = []
    price = []
    for d in data:
        d = d.split(':')
        date.append(d[0].split('-'))
        price.append(float(d[1]))
    return date, price


def avg_price_year(date, price):
    avg_price = 0
    avg_count = 0
    avg_price_year_result = []
    index = 0
    while index < len(date):
        # Check year (date[2])
        if date[index][2] == date[index - 1][2] or index == 0:
            avg_price += price[index]
            avg_count += 1
            if index == (len(date) - 1) or date[index][2] != date[index + 1][2]:
                avg_price_year_result.append([date[index][2], round(avg_price / avg_count, 3)])
                avg_price = 0
                avg_count = 0
        else:
            avg_price += price[index]
            avg_count += 1
        index += 1
    return tuple(avg_price_year_result)


def show_result_avg_price_year(avg_price_year_result):
    print("Average price per year:")
    for item in avg_price_year_result:
        print(f"{item[0]} | {item[1]:.2f}$")


def avg_price_month(date, price):
    avg_price = 0
    avg_count = 0
    avg_price_month_result = []
    index = 0
    while index < len(date):
        # Check month (date[0]) and year (date[2])
        if date[index][0] == date[index - 1][0] or index == 0:
            avg_price += price[index]
            avg_count += 1
            if index == (len(date) - 1) or date[index][0] != date[index + 1][0]:
                avg_price_month_result.append([date[index][0] + "-" + date[index][2], round(avg_price / avg_count, 3)])
                avg_price = 0
                avg_count = 0
        else:
            avg_price += price[index]
            avg_count += 1
        index += 1
    return tuple(avg_price_month_result)


def show_result_avg_price_month(avg_price_month_result):
    print("Average price per month:")
    for item in avg_price_month_result:
        print(f"{item[0]} | {item[1]:.2f}$")


def max_and_min_price_year(date, price):
    max_and_min_price_year_result = []
    index = 0
    max_price = 0
    min_price = price[index]
    while index < len(date):
        # Check year (date[2])
        if date[index][2] == date[index - 1][2] or index == 0:
            if price[index] > max_price:
                max_price = price[index]
            if price[index] < min_price:
                min_price = price[index]
            if index == (len(date) - 1) or date[index][2] != date[index + 1][2]:
                max_and_min_price_year_result.append([date[index][2], max_price, min_price])
                max_price = 0
        else:
            min_price = price[index]
            if price[index] > max_price:
                max_price = price[index]
            if price[index] < min_price:
                min_price = price[index]
        index += 1
    return tuple(max_and_min_price_year_result)


def show_result_max_and_min_price_year(max_and_min_price_year):
    print("Highest and lowest prices per year:")
    for item in max_and_min_price_year:
        print(f"{item[0]} | {item[1]:.2f}$ | {item[2]:.2f}$")


def create_new_file(date, price):
    ascending_list = []
    descending_list = []
    index = 0
    for i in range(len(date)):
        min_price_index = price.index(min(price))
        d = f"{date[min_price_index][0]}-{date[min_price_index][1]}-{date[min_price_index][2]}:{price[min_price_index]:.3f}"
        ascending_list.append(d)
        descending_list.insert(0, d)
        date.remove(date[min_price_index])
        price.remove(price[min_price_index])
    # Ascending order (Task #4)
    GasPricesAscending = open('GasPricesAscending.txt', 'w')
    for item in ascending_list:
        GasPricesAscending.write(f"{item}\n")
    GasPricesAscending.close()
    # Descending order (Task #5)
    GasPricesDescending = open('GasPricesDescending.txt', 'w')
    for item in descending_list:
        GasPricesDescending.write(f"{item}\n")
    GasPricesDescending.close()
    print("Data successfully written to files.")


main()
