#Goal - to count the character in string

text = "banana"


char_count = {}
for char in text:
    print(char)
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1


print(char_count)