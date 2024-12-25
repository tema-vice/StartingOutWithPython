# Exercise 2
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

class ShiftSupervisor(Employee):
    def __init__(self, name, id, annual_salary, award):
        Employee.__init__(self, name, id)
        self.__annual_salary = annual_salary
        self.__award = award

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_award(self, award):
        self.__award = award

    def get_annual_salary(self):
        return self.__annual_salary

    def get_award(self):
        return self.__award

    def __str__(self):
        return (f"Name: {self.get_name()}\n"
                f"Id: {self.get_id()}\n"
                f"Shift Number: {self.__annual_salary}\n"
                f"Hourly Pay: {self.__award}")


def main():
    name = input("Enter your name: ")
    while True:
        try:
            id = int(input("Enter your id: "))
            annual_salary = int(input("Enter your annual salary: "))
            award = int(input("Enter your award: "))
            if (id < 0) or (annual_salary < 0) or (award < 0):
                print("Invalid input.")
            else:
                break
        except Exception:
            print("Invalid data.")
    supervisor = ShiftSupervisor(name, id, annual_salary, award)
    print()
    print(supervisor)

main()
