'''
Build a Simple Address Book

    Task: Add, search, delete contacts using a dictionary.
'''

address_book = {}

def add(name, contact):
    address_book[name] = contact


def search(name):
    if name in address_book:
        print(f"Name : {name} --> Contact: {address_book[name]}")

def delete(name):
    del address_book[name]


#testing 

#adding contact
add("Ankit", 7675446389)
add("Naina", 3458699459)

print(address_book)

#search
search("Naina")

#delete
delete("Ankit")
print(address_book)