'''
Top N Frequent Elements

    Input: "apple banana apple orange banana apple"

    Task: Return the top 2 most frequent words.
'''

text = "apple banana apple orange banana apple"

text_list = text.split() #converting input-text into list 


word_count = {} # emp dictionay to store the value/word_count

for i in text_list:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1

print(word_count)


sorted_by_freq = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


top_n = 2
for word, freq in sorted_by_freq[:top_n]:
    print(word, freq)
   

