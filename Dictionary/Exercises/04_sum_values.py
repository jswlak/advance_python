'''
Sum of All Values

    Input: {"a": 5, "b": 10, "c": 3}

    Output: 18
'''

my_dict = {"a": 5, "b": 10, "c": 3}

total = 0

for key in my_dict:
    total += my_dict[key]
    
print(total)