# TXT file handling in Python

# Writing to a text file
with open("File_handling/file/example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a text file example.\n")

# Reading the entire file
with open("File_handling/file/example.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Reading line by line
with open("File_handling/file/example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())