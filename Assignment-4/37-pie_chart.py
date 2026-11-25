# Enrollment No: 92600565001

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

plt.pie([40,30,12], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()