'''
Word Frequency

    Input: "the quick brown fox jumps over the lazy dog"

    Task: Count how many times each word appears.
'''

text = "the quick brown fox jumps over the lazy dog"

word = text.split() #converting into list


word_frequency ={}

for w in word:
    if w not in word_frequency:
        word_frequency[w] = 1
    else:
        word_frequency[w] += 1

print(word_frequency)

