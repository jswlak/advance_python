# Find Maximum Element
# Find the largest number in a list without using max().


#     # Input: [5, 1, 7, 3]
#     # Output: 7

numbers = [5, 1, 7, 3]

max_num = 0

for i in numbers:
    if i > max_num:
        max_num = i

print(max_num)

#but this will fail if there is -ve number 
# e.g 
    # numbers = [-10, -3, -50, -2]
    # # Correct output: -2
    # but above logic give 0, which we set , since 0 will be always greater than all -ve numbers

#----------------So, let's fix it-------------------------------------------------------------------|

#To fix this, initialize max_num to the first element of the list:

numbers = [-10, -3, -50, -2]

max_num = numbers[0]  # Start with the first element

for i in numbers:
    if i > max_num:
        max_num = i

print(max_num)

