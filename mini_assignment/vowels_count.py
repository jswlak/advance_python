#Goal - to find number of vowels in a string




def count_vowels(text):
    vowel = ["a", "e", "i", "o", "u", "A", "E","I", "O", "U"]
    count = 0
    for x in text:
        for v in vowel:
            if x == v:
                count += 1
    print(f"Total number of vowels in '{text}', is {count}")



# testing ---------------------

text = "I love NLP"

count_vowels(text)

