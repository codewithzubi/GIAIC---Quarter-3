# Dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name          # dog's name
        self.breed = breed        # dog's breed (corrected the typo)

    def bark(self):
        print(f"{self.name} says woof")  # bark method

# Create object with arguments
d = Dog("Bruno", "Labrador")
d.bark()  # prints: Bruno says woof
