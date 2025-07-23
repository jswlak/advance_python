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