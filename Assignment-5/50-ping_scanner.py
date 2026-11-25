# Enrollment No: 92600565001

import subprocess

for i in range(1,11):
    ip = "127.0.0." + str(i)

    result = subprocess.run(
        ["ping", "-c", "l", "-w", "l", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(ip," is UP")
    else:
        print(ip," is DOWN")