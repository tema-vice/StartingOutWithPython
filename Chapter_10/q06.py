# Exercise 6
class Patient:
    def __init__(self, full_name, address, phone, spare_number):
        self.__full_name = full_name
        self.__address = address
        self.__phone = phone
        self.__spare_number = spare_number

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_spare_number(self, spare_number):
        self.__spare_number = spare_number

    def get_full_name(self):
        return self.__full_name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_spare_number(self):
        return self.__spare_number

    def __str__(self):
        return (f"Name: {self.__full_name}\n"
                f"Address: {self.__address}\n"
                f"Phone: {self.__phone}\n"
                f"Spare number: {self.__spare_number}")

class Procedure:
    def __init__(self, procedure_name, date, doctors_name, price):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__doctors_name = doctors_name
        self.__price = price

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_date(self, date):
        self.__date = date

    def set_doctors_name(self, doctors_name):
        self.__doctors_name = doctors_name

    def set_price(self, price):
        self.__price = price

    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_doctors_name(self):
        return self.__doctors_name

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"Procedure name: {self.__procedure_name}\n"
                f"Date: {self.__date}\n"
                f"Doctors name: {self.__doctors_name}\n"
                f"Price: {self.__price}")

def main():
    full_name = input("Enter your full name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone: ")
    spare_number = input("Enter spare number: ")
    user_patient = Patient(full_name, address, phone, spare_number)
    procedure_list = []
    procedure_list.append(Procedure("Doctor's Examination", "Today", "Irvin", 250))
    procedure_list.append(Procedure("X-Ray", "Today", "Jamison", 500))
    procedure_list.append(Procedure("Blood Test", "Today", "Smith", 200))
    print(f"Patient:\n{user_patient}")
    print("Procedure List:")
    for procedure in procedure_list:
        print("------------")
        print(procedure)

main()
