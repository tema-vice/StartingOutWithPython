# Exercise 3
class Person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Address: {self.__address}\n'
                f'Number: {self.__number}')

class Customer(Person):
    def __init__(self, name, address, number, message):
        Person.__init__(self, name, address, number)
        if message:
            self.__message = 'Newsletter is enabled'
        else:
            self.__message = 'Newsletter is disabled'

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def __str__(self):
        return (f'Name: {self.get_name()}\n'
                f'Address: {self.get_address()}\n'
                f'Number: {self.get_number()}\n'
                f'Message: {self.__message}')

def main():
    print("Person.")
    person = Customer("Vladimir", 'Moscow City', '+79*********', True)
    print(person)

main()