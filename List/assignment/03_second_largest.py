# Second Largest Element
# Write a program to find the second largest number in a list.


#     # Input: [5, 2, 9, 1]
#     # Output: 5



numbers = [5, 2, 9, 1]

numbers.sort() #sort in acendeniding order

# now for 2nd laregst we have to print last second index of sorted list


print(numbers[-2])

#but this will not work if there is duplicate

# numbers = [5, 9, 9, 1]
# This will still print 9, which is not the second unique largest.

numbers = [5, 9, 9, 1]

unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print(unique_numbers[-2])
else:
    print("No second largest number")


