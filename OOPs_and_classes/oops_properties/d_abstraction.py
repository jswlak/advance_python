from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


# Create objects
dog = Dog()
cat = Cat()

# Call methods
print(dog.sound())   # Output: Bark
print(cat.sound())   # Output: Meow


# You can’t create object of Animal, only of Dog or Cat, which implement the method.


#-------------------------------------------------------------------------------------------

print("_________________________")

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start_engine(self):
        pass

# Try to create object
# v = Vehicle()  #❌ Error! Can't instantiate abstract class

class Car(Vehicle):  # Child Class
    def start_engine(self):
        print("Car engine started 🚗")

c = Car()
c.start_engine()









# Abstract class is like a contract or template.
# Child classes are the ones that bring it to life.
