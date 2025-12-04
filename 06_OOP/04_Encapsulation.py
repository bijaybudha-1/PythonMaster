# Encapsulation
# Problem: Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        return f'{self.__brand}, {self.model}'

#     Encapsulation
    def get_brand(self):    # getter method
        return self.__brand


# my_car = Car("TATA", "Safari")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.fullname())

class ElectricCar:
    def __init__(self):
        self.brand = "Electric Car"

    def _set_car(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def _get_car(self):
        return f'Brand: {self.brand}, Model: {self.model}, Color:  {self.color}'


my_car = ElectricCar()
my_car._set_car("TATA", "Safari", "Black")
print(my_car._get_car())

