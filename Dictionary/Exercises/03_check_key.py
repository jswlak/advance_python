'''
Check Key Exists

    Task: Write a function that checks if a given key exists in a dictionary.
'''

my_dict = {
    "name": "Ankit",
    "country": "India",
    "city": "Delhi"
}

def key_check(key):
    if key in my_dict:
        print(f"✅ Key '{key}' exists.")

    else:
        print(f"❌ Key '{key}' does not exist.")


#testing----------|

key_check("name")
key_check("pincode")


