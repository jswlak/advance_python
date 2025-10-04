# read entire file
with open("File_handling/file/data.csv", "r") as f:
    content = f.read()
    print(content)

# read first 10 characters
with open("File_handling/file/data.csv", "r") as f:
    print(f.read(10))

# read line by line
with open("File_handling/file/data.csv", "r") as f:
    print(f.readline())   # first line
    print(f.readline())   # second line

# read all lines in list
with open("File_handling/file/data.csv", "r") as f:
    lines = f.readlines()
    print(lines)
