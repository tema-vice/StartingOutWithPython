# Exercise 8
class RetailItem:
    def __init__(self, description, count, price):
        self.__description = description
        self.__count = count
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_count(self, count):
        self.__count = count

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_count(self):
        return self.__count

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"Description: {self.__description}\n"
                f"Count: {self.__count}\n"
                f"Price: {self.__price}")

#-------------------------------------------------

class CashRegister:
    def __init__(self, item):
        self.__item_list = [item]
        self.__total_sum = item.get_price()
        item.set_count(item.get_count() - 1)

    def purchase_item(self, item):
        if item.get_count() > 0:
            self.__item_list.append(item)
            self.__total_sum += item.get_price()
            item.set_count(item.get_count() - 1)
            print("Product added.")
        else:
            print("The product is out of stock.")

    def get_total_sum(self):
        return f"Total sum: {self.__total_sum}"

    def show_item_list(self):
        return self.__item_list

    def show_items(self):
        print("\nList of products: ")
        try:
            number = 1
            for item in self.__item_list:
                print(f"Product №{number}: {item.get_description()}")
                number += 1
        except Exception:
            print("List clear.")

    def clear_all(self):
        try:
            for item in self.__item_list:
                item.set_count(item.get_count() + 1)
            self.__total_sum = 0
            self.__item_list.clear()
            print("List clear.")
        except Exception:
            print("Error clear.")

    def clear_item(self, index_item):
        try:
            index_item -= 1
            if self.__item_list[index_item] in self.__item_list:
                item = self.__item_list[index_item]
                item.set_count(item.get_count() + 1)
                self.__total_sum -= item.get_price()
                self.__item_list.remove(item)
                print("Product clear.")
            else:
                print("Product not found.")
        except Exception:
            print("Error.")

#-------------------------------------------------
ADD = 1
SHOW_LIST = 2
SHOW_AMOUNT = 3
DELETE_ITEM = 4
DELETE_ALL = 5
EXIT = 6

def main():
    warehouse_contents = {1: RetailItem("Pen", 6, 0.99),
                            2: RetailItem("Notebook", 3, 1.49),
                            3: RetailItem("Pencil", 4, 0.40)}
    print("Cash Register")
    show_warehouse_contents(warehouse_contents)
    cash_register = CashRegister(warehouse_contents[get_number_product(warehouse_contents)])
    while True:
        choice = show_menu()
        if choice == ADD:
            cash_register.purchase_item(warehouse_contents[get_number_product(warehouse_contents)])
        elif choice == SHOW_LIST:
            cash_register.show_items()
        elif choice == SHOW_AMOUNT:
            print(cash_register.get_total_sum())
        elif choice == DELETE_ITEM:
            cash_register.show_items()
            while True:
                try:
                    delete_item = int(input("Enter the item number to delete: "))
                    cash_register.clear_item(delete_item)
                    break
                except Exception:
                    print("Invalid input.")
        elif choice == DELETE_ALL:
            cash_register.clear_all()
        elif choice == EXIT:
            break
    print("Exiting the program.")

def show_menu():
    print("\n1. Add product\n2. Show product list\n3. Show final amount\n4. Delete product\n5. Delete all product\n6. Exit")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > EXIT or choice < ADD:
                print("Invalid choice. Please try again.")
            else:
                break
        except Exception:
            print("Invalid choice. Please try again.")
    return choice

def show_warehouse_contents(warehouse):
    for item in warehouse:
        print("--------------------")
        print(f"Product №{item}:\n{warehouse[item]}")

def get_number_product(warehouse_contents):
    while True:
        try:
            product_number = int(input("\nSelect which product to add: "))
            if product_number not in warehouse_contents:
                print("Please select a valid product.")
            else:
                break
        except Exception:
            print("Invalid input.")
    return product_number

main()
