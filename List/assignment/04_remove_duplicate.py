# Remove Duplicates
# Remove duplicate elements from a list without using set().


#     # Input: [1, 2, 2, 3, 1]
#     # Output: [1, 2, 3]




numbers = [1, 2, 2, 3, 1]

unique_numbers = []

for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
    

print(unique_numbers)
