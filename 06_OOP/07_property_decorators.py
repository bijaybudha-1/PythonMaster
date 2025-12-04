# Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only

class EngineCar:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f'Brand Name: {self.__brand}, Model: {self.__model}'

    @property
    def model(self):
        return self.__model

my_engine_car = EngineCar("TATA", "Safari")
my_engine_car.__model = "Nexon"
print(my_engine_car.full_name())
print(my_engine_car.model)
