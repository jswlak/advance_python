from learning_class import Student

# create object

s1 = Student("Radhey", 19)


s1.display()


#Problem - 
#all 3 student is showing because-
# Python runs the whole learning_class.py file — not just imports the class — which creates all the objects inside it too.

#solution -


# This block runs only if you directly run this file
# if __name__ == "__main__":
#     student_1 = Student("Ankit", 25)
#     student_2 = Student("Naina", 22)
#     student_1.display()
#     student_2.display()