#Goal - to find print the reverse of string

def reverse_string(text):
  rev_string = ""
  length = len(text)

  for i in range(length):
    rev_string += text[length -1 - i]
  print(rev_string)

# testing

text = "hello"

reverse_string(text)






















