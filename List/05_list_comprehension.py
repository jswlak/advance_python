# List comprehension is one of the most powerful and concise features in Python.
# It lets you create lists in a single line of code—more readable and often faster than using loops.

#Basic syntax:
    # [expression for item in iterable if condition]
# -------------------------------------------------------------------------------------------------------------------

squares = [x**2 for x in range(11)]
print(squares)

#With Condition (if)

even = [x for x in range(11) if x % 2 == 0]

print(even)


#With if–else

labels = ["even" if x % 2 == 0 else "odd" for x in range(12)]
print(labels)

#Filtering a List

fruits = ["apple", "banana", "kiwi", "pear"]
long_fruit = [fruit for fruit in fruits if len(fruit) > 4]

print(long_fruit)





#Flattening a 2D List

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]

print(flat)

# Nested List Comprehension

nested = [[x*y for y in range(1, 4)] for x in range(1, 4)]
print(nested)

#With Strings

word = "Hello"

char = [i for i in word]

print(char)
