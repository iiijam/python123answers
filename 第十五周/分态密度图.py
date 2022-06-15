import matplotlib.pyplot as plt

m, n = map(int, input().split())

ls = []
cl = ['b', 'g', 'r', 'c']

with open('DOSofBaTiO3PDOS.csv', 'r', encoding='utf-8') as f:
    for lines in f:
        ls.append(lines.strip().split(','))

for i in range(4):
    lsx = [float(x[2*i]) for x in ls if x[2*i] != '' and m < float(x[2*i]) < n]
    lsy = [float(x[2*i+1])
           for x in ls if x[2*i+1] != '' and m < float(x[2*i]) < n]
    plt.plot(lsx, lsy, color=cl[i])

plt.axvline(0, linestyle='--', c='black')
plt.xlabel('E-Ev(eV)')
plt.ylabel('DOS')
plt.savefig('pdos.png')
plt.show()
