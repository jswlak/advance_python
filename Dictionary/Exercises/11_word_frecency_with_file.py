'''
Create Frequency Dictionary from a File

    Task: Read a .txt file and create a word frequency dictionary.
'''

with open('Text_data/War_and_Peace.txt', 'r') as file: 
    text = file.read()

word_list = text.split()

# print(word_list)

total_length = len(word_list)


print(total_length)

word_frequency = {} #creating an emp dict to store count value of each word

#adding and counting

for w in word_list:
    if w not in word_frequency:
        word_frequency[w] = 1
    else:
        word_frequency[w] += 1

# print(word_frequency)



#---------------------------------------------Improved and most general ---------------------------------------------------|

# import re
# from collections import Counter

# # Step 1: Read File
# with open('Text_data/War_and_Peace.txt', 'r') as file:
#     text = file.read()

# # Step 2: Clean and Normalize Text
# # Remove punctuation and convert to lowercase
# clean_text = re.sub(r'[^\w\s]', '', text.lower())

# # Step 3: Split into words
# word_list = clean_text.split()
# print("Total words:", len(word_list))

# # Step 4: Count word frequencies
# word_frequency = Counter(word_list)

# # Step 5: Print top 10 most common words
# print(word_frequency.most_common(10))
