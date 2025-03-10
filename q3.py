# Base class Shape
class Shape:
    def __init__(self):
        print("Shape initialized.")

    def calculate_area(self):
        pass

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Calling the constructor of the Shape class
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Create a Rectangle object
rectangle = Rectangle(4, 6)  # Output: Shape initialized.
print("Area:", rectangle.calculate_area())  # Output: 24
