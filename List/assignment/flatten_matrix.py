#problem - we have nested list - matrix , we have to flatten it

matrix = [[1, 2], [3, 4], [5, 6]]


flatten_list = [] #creating an emp list to store the value

for i in matrix:
    for j in i:
        flatten_list.append(j)


print(flatten_list)