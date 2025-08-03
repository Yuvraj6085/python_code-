class Car:
    def __init__(self,barnd,model):
        self.barnd = barnd
        self.model = model
    def ge__brand(self):
        return self.barnd +"!"
    def full_name(self):
        return f"{self.barnd} {self.model}"
class ElectricCar(Car):
    def __init__(self,barnd,model,battery_size):
        super().__init__(barnd,model)
        self.battery_size = battery_size
tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.full_name())
print(f"Battery Size: {tesla.battery_size} kWh")
