import matplotlib.pyplot as plt

x, y = [], []

with open('DosOfBaTiO3.txt', 'r') as f:
    ls = f.readlines()
    for i in ls:
        x.append(float(i.split()[0]))
        y.append(float(i.split()[1]))

plt.plot(x, y,linestyle=':',color='b')

plt.xlabel('Energy(Ha)')
plt.ylabel('Density of States(electrons/Ha)')
plt.savefig('AceTaffy.jpg')
plt.show()