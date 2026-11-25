# Enrollment No: 92600565001

import subprocess

d = input("Enter the domain: ")

subprocess.run(["dig", d])
subprocess.run(["dig", d, "MX"])
subprocess.run(["dig", d, "NS"])
