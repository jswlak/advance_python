class Student:
    def __init__(self, name, roll):
        self.__name = name               # private variable  
        self.roll = roll


    def display(self):
        print(f"Name: {self.__name}, Roll Number: {self.roll}")  # controlled access


s1 = Student("Rapunzal", 21)

# print(s1.name)
# print(s1.roll)

# s1.display()

s1.display()

print(s1.__name)





