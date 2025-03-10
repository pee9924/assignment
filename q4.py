# Base class for objects that can make sound
class Animal:
    def make_sound(self):
        pass

# Subclass Dog
class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Subclass Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Function that processes sound from any object that can make a sound
def process_sound(sound_object):
    print(sound_object.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Process sound from both objects
process_sound(dog)  # Output: Bark
process_sound(cat)  # Output: Meow
