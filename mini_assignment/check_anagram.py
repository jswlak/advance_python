#Check if two strings are anagrams (same letters in different order).
#eg - save-vase, silent-listen

def is_anargrams(a,b):
   
   a1 = sorted(a)
   b1 = sorted(b)

   if a1 == b1:
      print(f"Yes, {a}, and {b} are anagrams!")


# testing----

a = "listen"
b = "silent"

is_anargrams(a, b)