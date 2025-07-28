'''
Sort Dictionary by Value

    Input: {"apple": 5, "banana": 2, "grape": 7}

    Output: Sorted by values in descending order.
'''

my_dict = {"apple": 5, "banana": 2, "grape": 7}

sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

print(sorted_dict)
