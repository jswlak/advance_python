
class Student:
    def __init__(self, name, roll):
        self.name = name                #atributes
        self.roll = roll


    def display(self):
        print(f"Name: {self.name}, Roll Number: {self.roll}")



#create object from student class

student_1 = Student("Ankit", 25)
student_2 = Student("Naina", 22)


# call methods

student_1.display()
student_2.display()



        