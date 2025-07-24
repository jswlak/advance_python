

# ---------------------------------------Creating 1st class Anmimal-------------------------------------------------------------




class Animal:
    def __init__(self):
        print("Animal object created") #print each time when object is created due to contructor ----> "def __init__(self)" 
    

    def speak(self):
        print("Animal Speak")


# -------------------------------------------Now 2nd class Dog-----------------------------------------------------------------


class Dog(Animal):    #inherating from 1st class Animal
    def bark(self):
        print("Dog barks")



a = Animal() # print --> Animal object created

print("-------------------------")

b = Dog()

b.speak()      #inheritate from, parents class: Animal"
b.bark()                         #own method
