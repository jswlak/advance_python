# JSON file handling in Python
import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Machine Learning", "Kivy"]
}

# Writing JSON
with open("File_handling/file/data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON
with open("File_handling/file/data.json", "r") as f:
    loaded_data = json.load(f)
    print("Loaded JSON:", loaded_data)
