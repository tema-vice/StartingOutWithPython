# Exercise 4
class Employee:
    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Id: {self.__id}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}")

def main():
    info_list = []
    info_list.append(Employee("Susan Meyers", "47899", "Accounting", "Vice President"))
    info_list.append(Employee("Mark Jones", "39119", "IT", "Programmer"))
    info_list.append(Employee("Joy Rogers", "81774", "Manufacturing", "Engineer"))
    for info in info_list:
        print("--------------------")
        print(info)

main()
