'''
利用附件中的成绩数据进行成绩统计，根据总分进行升序排序后，输出总分最低分和最高分，按总分升序输出前n名同学和后n名同学成绩信息（n为非负数，当n大于数据行数时，按实际行数输出），输出每题的平均成绩。
'''

data = open('成绩单.csv', 'r', encoding='utf-8')
n = int(input())

ls = []
ls1 = []
ls2 = []

a = s = d = j = g = h = 0

with open('成绩单.csv', 'r', encoding='utf-8') as f:

    for line in f:
        ls.append(line.strip().split(','))

    number = len(ls)

    ls.sort(key=lambda x: int(x[-1]))
    print(f'最低分{ls[0][-1]}分,最高分{ls[-1][-1]}分')

    for i in range(number):
        a += int(ls[i][3])
        s += int(ls[i][4])
        d += int(ls[i][5])
        j += int(ls[i][6])
        g += int(ls[i][7])
        h += int(ls[i][8])

    if n > number:
        print(ls)

    else:
        print(ls[0:n])
        print(ls[-n:])

    ls2.extend([float(f'{(a/(number)):.2f}'),
                float(f'{(s/(number)):.2f}'),
                float(f'{(d/(number)):.2f}'),
                float(f'{(j/(number)):.2f}'),
                float(f'{(g/(number)):.2f}'),
                float(f'{(h/(number)):.2f}'),
                ])

    print(ls2)

data.close()
