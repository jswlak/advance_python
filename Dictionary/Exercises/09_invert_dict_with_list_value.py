'''
Invert a Dictionary with List Values

    Input: {"fruit": ["apple", "banana"], "color": ["red", "yellow"]}

    Output: {"apple": "fruit", "banana": "fruit", "red": "color", "yellow": "color"}
'''


dict_with_list = {"fruit": ["apple", "banana"], "color": ["red", "yellow"]}

inverted_dict = {} #creating an emp dict to store the inverted value

for key in dict_with_list: #loop for each key in dict_with_list
    
    for i in dict_with_list[key]: #loop to iterate every list [value], 
        
        inverted_dict[i] = key  # adding list element as key - inverting 

print(inverted_dict)







