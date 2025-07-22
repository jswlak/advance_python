def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):   # Accept any arguments
        print("Answer is:")                   # Extra work
        return original_function(*args, **kwargs)  # Call with arguments
    return wrapper_function


@decorator_function
def add(a, b):
    print(a + b)


add(5, 7)
add(6, 9)
add(8, 11)
add(11, 13)
add(13, 17)



@decorator_function
def multiply(a, b):
    print(a*b)


multiply(5,7)
multiply(4, 4)
