import matplotlib.pyplot as plt

labels = ['C语言',  'Python', 'Java', 'C++语言',
          'C#', 'VB.net', 'Javascript', 'PHP', 'Other']
sizes = [16.2, 12.1, 11.7, 7.6, 4.7, 4.0, 2.0, 1.8, 39.9]
explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.axes(aspect=1)
plt.pie(sizes,
        explode=explode,
        labels=labels,
        labeldistance=1.1,
        autopct='%.1f%%',
        shadow=True,
        startangle=90,
        pctdistance=0.7,)
plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1.1))

plt.savefig('program.png')
plt.show()
