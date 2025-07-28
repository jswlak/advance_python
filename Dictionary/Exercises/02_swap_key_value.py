'''
Swap Keys and Values

    Input: {1: "a", 2: "b", 3: "c"}

    Output: {"a": 1, "b": 2, "c": 3}
'''

a = {1: "a", 2: "b", 3: "c"}

b = {}

for key in a:
    # print(a[key])
    b[a[key]] = key 

print(b)



#---------------------------handle non-unique values-----------------------|

#problem

'''
    z  = {1: "x", 2: "y", 3: "x"}
    we want - 
    # Output:
    {'x': [1, 3], 'y': [2]}
'''

z = {1: "x", 2: "y", 3: "x"}

m = {}

for key, value in z.items():
    if value not in m:
        m[value] = [key]         # create new list with the key
    else:
        m[value].append(key)     # append to existing list

print(m)
