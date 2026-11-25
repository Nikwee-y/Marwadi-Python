# Enrollment No: 92600565001

import whois

w = whois.whois("google.com")
print("Creation Date: ",w.creation_date)