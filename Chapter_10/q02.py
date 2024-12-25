# Exercise 2
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    car = Car('Camry', 'Toyota')
    print("Speed avto: ")
    for n in range(5):
        print(car.get_speed(), 'km/h')
        car.accelerate()
    print(car.get_speed(), 'km/h')
    for n in range(5):
        car.brake()
        print(car.get_speed(), 'km/h')

main()
