# Engine class with a start method
class Engine:
    def start(self):
        print("Engine Start...")  # prints when engine starts

# Car class uses Engine (composition)
class Car:
    def __init__(self, engine):
        self.engine = engine  # assign engine to the car

    def start_car(self):
        self.engine.start()  # call engine's start method

# Create Engine object
eng = Engine()

# Pass engine to Car object
cr = Car(eng)

# Start the car (which starts the engine)
cr.start_car()  # Output: Engine Start...
