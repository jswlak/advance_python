'''
Count Vowels in Each Word

    Input: ["apple", "banana", "grape"]

    Output: {'apple': 2, 'banana': 3, 'grape': 2}
'''

word = ["apple", "banana", "grape"]
vowel_count = {}                        #an emp dict to store the count value

for w in word:                          #running loop for each word
    
    count = 0

    for char in w:                      #for each char in word
        if char in 'aeiou':             #checking if there any vowel

            
            count += 1
    vowel_count[w] = count               #adding count as value and word as key in dictionary - vowel_count

print(vowel_count)























