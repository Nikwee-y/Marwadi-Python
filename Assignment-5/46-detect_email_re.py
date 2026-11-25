# Enrollment No: 92600565001
import re

text = "contact abc@gmail.com"

print(re.findall(r'[\w.-]+@[\w.-]+\.\w+', text))