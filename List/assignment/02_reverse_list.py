# Reverse a List
# Print a list in reverse order (without using [::-1]).

#     # Input: [1, 2, 3]
#     # Output: [3, 2, 1]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_length = len(num)


last_index = num_length - 1



for i in range(num_length):
    print(num[last_index - i])
    
