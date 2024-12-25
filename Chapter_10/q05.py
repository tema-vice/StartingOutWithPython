# Exercise 5
class RetailItem:
    def __init__(self, description, count, cost):
        self.__description = description
        self.__count = count
        self.__cost = cost

    def __str__(self):
        return (f"Description: {self.__description}\n"
                f"Count: {self.__count}\n"
                f"Cost: {self.__cost}")

def main():
    Retail_list = {"Item #1": RetailItem("Jacket", 12, 59.95),
                   "Item #2": RetailItem("Designer Jeans", 40, 34.95),
                   "Item #3": RetailItem("Shirt", 20, 24.95)}
    for item in Retail_list:
        print("--------------------")
        print(f"{item}\n{Retail_list[item]}")

main()
