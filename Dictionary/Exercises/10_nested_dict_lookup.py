'''
Nested Dictionary Lookup

    Input: {"student": {"name": "Alice", "marks": {"math": 90, "science": 85}}}

    Task: Access math marks.
'''
my_dict = {"student": {"name": "Alice", "marks": {"math": 90, "science": 85}}}


math_marks = my_dict["student"]["marks"]["math"]

print(math_marks)





