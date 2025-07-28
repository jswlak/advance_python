'''
Merge Two Dictionaries

    Input: {"a": 1, "b": 2} and {"b": 3, "c": 4}

    Task: Merge and sum values of common keys.

    Output: {"a": 1, "b": 5, "c": 4}
'''




def dict_merger(d1, d2):

   

    merge_dict = d1.copy()                  #Creates a new dictionary

    for key in d2:
        if key in merge_dict:                         #Add values if key exists
            merge_dict[key] += d2[key]
        else:
            merge_dict[key] = d2[key]       #Add new key-value
    print(merge_dict)

#testing--------------------------------------------------------------------------|

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}


dict_merger(d1, d2)
print("---------------------------------------")

x1 = {"a": 1, "b": 2, "x": 10}
x2 = {"b": 3, "c": 4, "x": 5, "z": 1}

dict_merger(x1, x2)
