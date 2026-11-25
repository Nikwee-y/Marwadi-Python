# Enrollment No: 92600565001

import socket

host = input("Enter the ip: ")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.7)

    result = s.connect_ex((host,port))

    if result == 0:
        print("Port: ",port, "is open")
    else:
        print("Port: ",port, "is close")

    s.close()