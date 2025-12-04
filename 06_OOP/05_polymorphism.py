class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Fuel Type: Petrol / Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f'Fuel Type: Battery Charging'
        

safari = Car("TATA", "Safari")
print(safari.brand)
print(safari.model)
print(safari.fuel_type())

tesla = ElectricCar("tesla", "Safari", "85KWH")
print(tesla.brand)
print(tesla.fuel_type())