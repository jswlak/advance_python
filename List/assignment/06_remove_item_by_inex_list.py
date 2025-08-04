# Remove Element by Index List
# Given a list and another list of indices, remove the elements at those indices.


#     # Input: list = [10, 20, 30, 40, 50], indices = [1, 3]
#     # Output: [10, 30, 50]


numbers = [10, 20, 30, 40, 50]

indices = [1, 3]

final_list = []

length = len(numbers)

for i in range(length):
    if i not in indices:
        final_list.append(numbers[i])

print(final_list)
