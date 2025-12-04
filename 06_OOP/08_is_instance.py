# Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of EngineCar and ElectricCar.

class EngineCar:
    def __init__(self, model, brand):
        self._model = model
        self._brand = brand

    def fullname(self):
        return f"Brand: {self._brand} Model: {self._model}"

    def engine_type(self):
        return f"Engine: Petrol / Diesel"

class ElectricCar(EngineCar):
    def __init__(self, model, brand, battery_size):
        super().__init__( model, brand)
        self.battery_size = battery_size

    def fullname(self):
        return f"Brand: {self._brand} Model: {self._model}, Battery Capacity: {self.battery_size} "

    def engine_type(self):
        return "Battery Charger"


safari = EngineCar("TATA", "Safari")
print(safari.fullname())
print(safari.engine_type())

tesla = ElectricCar("tesla", "ts2", "85KWH")
print(tesla.fullname())
print(tesla.engine_type())

# Check the isinstance() method
print(isinstance(tesla, ElectricCar))
print(isinstance(safari, EngineCar))