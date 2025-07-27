
my_dict = {
    "Bihar": "Patna", 
    "Maharashtra" : "Bombay", 
    "Goa" : "Panji",
    "Telangana": "Hyderabad"
}

print(my_dict)
print("\n")

#add 

my_dict["Karnatka"] = "Bengaluru"

print(my_dict)
print("\n")

#----------------------Update--------------------------------|

my_dict["Maharashtra"] = "Mumbai"
print(my_dict)
print("\n")

#----------------------Delete--------------------------------|

del my_dict["Telangana"]
print(my_dict)

#Clear all data

my_dict.clear()
print(my_dict)