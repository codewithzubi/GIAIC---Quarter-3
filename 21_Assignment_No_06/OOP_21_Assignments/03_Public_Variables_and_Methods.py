class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting...")

my_car = Car("Toyota")
my_car.start()