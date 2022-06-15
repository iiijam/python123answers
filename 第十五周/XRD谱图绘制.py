import matplotlib.pyplot as plt

x, y = [], []

with open('XRD_AFO.csv', 'r') as f:
    ls = f.readlines()
    for i in ls[1:]:
        x.append(float(i.split(',')[0]))
        y.append(float(i.split(',')[1]))

plt.plot(x, y,linestyle='--',linewidth=2)
plt.title('X射线衍射图谱',fontproperties='SimHei')
plt.xlabel('Position(2-Theta)')
plt.ylabel('Intensity')
plt.savefig('xrd.png')
plt.show()