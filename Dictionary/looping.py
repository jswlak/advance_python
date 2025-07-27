my_di = {
    "name" : "Naina",
    "country" : "India",
    "city" : "Delhi"
}

#loop through key
for key in my_di:
    print(key)



print("--------------------")

for k in my_di:
    print(k, my_di[k])

print("--------------------")

#loop through item


for key, val in my_di.items():
    print(key, val)
   
for key, val in my_di.items():
     print(f"{key} --> {val}")
