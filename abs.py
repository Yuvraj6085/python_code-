class Car:
    def __init__(self, acc, cal, start_status):
        self.acc = acc
        self.cal = cal
        self.is_started = start_status  # Renamed attribute to avoid conflict

    def start(self):
        self.is_started = True
        self.cal = True
        print("Car started")

# Test the corrected class
c1 = Car(True, True, True)
c1.start()  # Correct call (without print)