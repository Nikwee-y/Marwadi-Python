# Enrollment No: 92600565001

import re 

s = input("Enter a string: ")

if re.search(r'\d',s):
    print("Digits Found.")
else:
    print("No digit found.")