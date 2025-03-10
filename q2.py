# Base class Shape
class Shape:
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate total area of different shapes
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Create objects of different shapes
shapes = [Circle(5), Rectangle(4, 6)]

# Calculate total area
print(total_area(shapes))  # Output: 78.5 (Circle area) + 24 (Rectangle area) = 102.5
