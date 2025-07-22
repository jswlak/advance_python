def add(a, b):
    print(a+b)


def answer():
    print("Answer is:")


answer()
add(5, 7)


answer()
add(6, 9)


answer()
add(8, 11)


answer()
add(11, 13)

answer()
add(13, 17)


# ❌ problem statement —

# "It's boring to call answer() every time"


# ✅ Solution - 

# Used a decorator to automatically print "Answer is:" before function output, making code cleaner and DRY.




