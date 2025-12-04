# EngineCar class
class EngineCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# ElectricCar class inheriting EngineCar
class ElectricCar(EngineCar):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# Engine class
class Engine:
    def engine_info(self):
        return "This is the engine info"

# Electric class
class Electric:
    def electric_info(self):
        return "This is the electric info"

# Multiple inheritance class
class CarDescription(Engine, Electric, EngineCar):
    pass

# Create object
my_car = CarDescription("Tesla", "S5")

# Call methods from parent classes
print(my_car.engine_info())    # Engine method
print(my_car.electric_info())  # Electric method
