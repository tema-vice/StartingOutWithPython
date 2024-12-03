# Exercise 9
START_YEAR = 1950
END_YEAR = 1990
def main():
    year_list = []
    for year in range(START_YEAR, END_YEAR + 1):
        year_list.append(year)

    population_list = get_list()
    change_population_list = []

    index = 0
    while index < len(population_list):
        if index == (len(population_list) - 1):
            break
        else:
            change_population = population_list[index + 1] - population_list[index]
            change_population_list.append(change_population)
            # Data in each iteration of the loop
            #print(f"{year_list[index]}-{year_list[index + 1]}: {change_population} | index = {index}")

            index += 1

    # Find total sum
    total_sum_population = func_sum_items_in_list(change_population_list)
    # Find index max and min value in list
    index_max_change_population = change_population_list.index(max(change_population_list))
    index_min_change_population = change_population_list.index(min(change_population_list))

    # Show results
    print(f"Average annual change in population: "
          f"{year_list[0]}-{year_list[len(year_list) - 1]} | "
          f"{total_sum_population / len(change_population_list):.1f} |")
    print("Year with largest increase in population: "
          f"{year_list[index_max_change_population]}-{year_list[index_max_change_population + 1]} | "
          f"{max(change_population_list)} |")
    print("Year with the least imprisonment: "
          f"{year_list[index_min_change_population]}-{year_list[index_min_change_population + 1]} | "
          f"{min(change_population_list)} |")

def get_list():
    file = None
    list = []
    try:
        file = open('USPopulation.txt', 'r')
        list = file.readlines()

        index = 0
        while index < len(list):
            list[index] = list[index].rstrip('\n')
            list[index] = int(list[index])
            index += 1
    except Exception as error:
        print(error)
    finally:
        if file is not None:
            file.close()
        return list



def func_sum_items_in_list(change_population_list):
    total = 0
    for item in change_population_list:
        total += item
    return total

main()
