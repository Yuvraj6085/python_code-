class Car :
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.brand} {self.model}"
car= Car("Toyota", "Corolla")
print(car.full_name())
print(f"Total Cars: {Car.total_cars}")

    