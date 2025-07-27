#Goal -to find the factorial of number

def find_factorial(nums):

    factorial = 1
    for i in range(nums):
        factorial = factorial *(i+1)


    print(factorial)


#testing
nums = 10

find_factorial(nums)
