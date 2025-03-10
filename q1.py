# Base class Vehicle
class Vehicle:
    def description(self):
        return "This is a vehicle."

# Subclass Car
class Car(Vehicle):
    def description(self):
        return "This is a car."

# Subclass Bike
class Bike(Vehicle):
    def description(self):
        return "This is a bike."

# Creating instances and showing method overriding
vehicle = Vehicle()
car = Car()
bike = Bike()

print(vehicle.description())  # Output: This is a vehicle.
print(car.description())      # Output: This is a car.
print(bike.description())     # Output: This is a bike.
