# Exercise 3
class Information:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Address: {self.__address}\n"
                f"Age: {self.__age}\n"
                f"Phone: {self.__phone}\n")

def main():
    print("Enter information about you and two of your friends: ")
    info = []
    for n in range(3):
        print("--------------------")
        name = input("Enter name: ")
        address = input("Enter address: ")
        age = input("Enter age: ")
        phone = input("Enter phone: ")
        info.append(Information(name, address, age, phone))
    for info in info:
        print("--------------------")
        print(info)

main()
