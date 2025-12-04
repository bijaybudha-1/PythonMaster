# Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f'{self.brand}, {self.model}'

class ElecttricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car('toyota', 'toto')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

electric_car = ElecttricCar("Tesla", "S", "85KWH")
print(electric_car.brand)
print(electric_car.fullname())
print(electric_car.battery_size)