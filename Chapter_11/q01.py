# Exercise 1
class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Id: {self.__id}")

class ProductionWorker(Employee):
    def __init__(self, name, id, shift_number, hourly_pay):
        Employee.__init__(self, name, id)
        self.__hourly_pay = hourly_pay
        if shift_number == 1:
            self.__shift_number = "Day shift"
        elif shift_number == 2:
            self.__shift_number = "Night shift"
        else:
            self.__shift_number = "Incorrect data"

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay(self):
        return self.__hourly_pay

    def __str__(self):
        return (f"Name: {self.get_name()}\n"
                f"Id: {self.get_id()}\n"
                f"Shift Number: {self.__shift_number}\n"
                f"Hourly Pay: {self.__hourly_pay}")


def main():
    name = input("Enter your name: ")
    while True:
        try:
            id = int(input("Enter your id: "))
            shift_number = int(input("Enter '1' if you work in day shift\nOr '2' if you work in night shift: "))
            hourly_pay = float(input("Enter your hourly pay: "))
            if id < 0:
                print("Enter a valid id.")
            elif (shift_number < 1) or (shift_number > 2):
                print("Incorrect shift number.")
            elif hourly_pay < 0:
                print("Hourly pay must be greater than or equal to 0.")
            else:
                break
        except Exception:
            print("Invalid data.")
    worker = ProductionWorker(name, id, shift_number, hourly_pay)
    print(worker)

main()
