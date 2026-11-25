# Enrollment No: 92600565001
import hashlib

s = input("Enter the string: ")
h = hashlib.sha256(s.encode())
print("Hash: ",h.hexdigest())