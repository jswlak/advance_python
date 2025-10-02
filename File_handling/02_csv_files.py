# CSV file handling in Python
import csv

# Writing to CSV
with open("File_handling/file/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ankit", 25, "Patna"])
    writer.writerow(["Bablu", 30, "Delhi"])
    writer.writerow(["Chiku", 22, "Pune"])

# Reading from CSV
with open("File_handling/file/data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
