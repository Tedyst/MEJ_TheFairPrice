import numpy as np
import matplotlib.pyplot as plt

savetofile = False

f = open("samples.txt", "r")
v = []

for line in f:
    v.append(float(line))

plt.figure(dpi=100)
plt.plot(v)
plt.ylim(0, 50)
plt.xlabel("Number of samples taken")
plt.ylabel("Percent of winning games")
if savetofile:
    plt.savefig('filename.png', dpi=300)   
else:
    plt.show()

