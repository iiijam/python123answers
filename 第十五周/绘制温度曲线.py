import matplotlib.pyplot as plt
import numpy as np

x, y, z = [], [], []

with open('9.1 某月温度.txt', 'r') as f:
    ls = f.readlines()
    for i in ls:
        x.append(float(i.split()[0]))
        y.append(float(i.split()[1]))
        z.append(float(i.split()[2]))

plt.ylim(-10, 25)

plt.plot(x, y, linestyle='-', color='r', marker='o')
plt.plot(x, z, linestyle='-', color='b', marker='*')
plt.axhline(y=0, color='b', linestyle='--')
plt.xticks(np.arange(1, 32, 1))
plt.savefig('temp_curve.png')
plt.show()