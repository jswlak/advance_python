# Pickle file handling in Python
import pickle

# Example object (dictionary)
person = {"name": "Bob", "age": 30, "city": "London"}

# Saving object with pickle
with open("File_handling/file/person.pkl", "wb") as f:
    pickle.dump(person, f)

# Loading object with pickle
with open("File_handling/file/person.pkl", "rb") as f:
    loaded_person = pickle.load(f)
    print("Loaded object:", loaded_person)
