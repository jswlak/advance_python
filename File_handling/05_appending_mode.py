# Writing & Appending

# overwrite file
with open("File_handling/file/notes.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# append to file
with open("File_handling/file/notes.txt", "a") as f:
    f.write("Appended line\n")
    f.write("2nd Appended line")
