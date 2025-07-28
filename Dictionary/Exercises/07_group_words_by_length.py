'''
Group Words by Length

    Input: ["hi", "hello", "cat", "python", "dog"]

    Output: {2: ['hi'], 3: ['cat', 'dog'], 5: ['hello'], 6: ['python']}
'''

word_list = ["hi", "hello", "cat", "python", "dog"]

char_count = {} #emp dict to store count char in word

#char count 
for word in word_list:
    count = 0

    for char in word:
        
        count += 1
    char_count[word] = count

print(char_count)

# swap key-value

swaped = {}

for key, value in char_count.items():
    if value not in swaped:
        swaped[value] = [key] # create new list with the key
    else:
        swaped[value].append(key)  # append to existing list


print(swaped)

