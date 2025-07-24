class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane flies high")



b = Bird()
a = Airplane()

b.fly()
a.fly()



#----------------------------------------------------------------
# Polymorphism means same name, different behavior depending on the object.
# During inheritance - child class overrides (rides over) the parent class method.
#----------------------------------------------------------------

print("------------------------------------------------------------------------------------------------")


class Vehicle:
    def ride(self):
        print("Riding a vehicle...")

class Bike(Vehicle):
    def ride(self):
        print("Riding a bike...")

class Car(Vehicle):
    def ride(self):
        print("Driving a car...")

v0 = Vehicle()
v1 = Bike()  #will overide the parents
v2 = Car()      # "

v0.ride()
v1.ride()
v2.ride()
