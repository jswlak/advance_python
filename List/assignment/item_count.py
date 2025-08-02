#given list , we have to count item in list


fruits = ["banana", "apple", "banana", "guava", "pineapple", "banana"]

banana_count = 0

for fruit in fruits:
    if fruit == "banana":
        banana_count += 1

print(banana_count)

