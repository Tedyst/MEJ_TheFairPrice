import numpy as np
import matplotlib.pyplot as plt

savetofile = False

f = open("samples.txt", "r")
v = []

for line in f:
    v.append(float(line))

plt.figure(dpi=300)
plt.plot(v)
line1 = plt.axhline(np.e-2, label="e-2", color="red")
plt.legend([line1], ["e-2"])
plt.xlabel("Number of samples taken")
plt.ylabel("Median Money taken")
if savetofile:
    plt.savefig('filename.png', dpi=300)   
else:
    plt.show()

