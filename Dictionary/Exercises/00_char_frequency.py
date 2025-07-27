'''
Character Frequency
    Input: "hello world"
    Task: Count how many times each character appears.
'''

text = "hello world"

char_frequency = {}

for char in text:
    if char not in char_frequency:
        char_frequency[char] = 1
    else:
        char_frequency[char] = char_frequency[char] + 1



print(char_frequency)


#delete 'space' count

del char_frequency[" "]
print(char_frequency)
