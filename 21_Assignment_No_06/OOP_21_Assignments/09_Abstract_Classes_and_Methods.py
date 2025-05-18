from abc import abstractmethod, ABC  # import abstract base class tools

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):  # abstract method
        pass

# Rectangle class inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width        # rectangle width
        self.height = height      # rectangle height

    def area(self):               # implementation of abstract method
        return self.width * self.height

# Create object of Rectangle
rect = Rectangle(4, 5)
print(rect.area())  # prints 20 (area of rectangle)
