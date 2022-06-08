with open('2019Charity.csv', 'r', encoding='utf-8') as f:
    ls = [i.strip().split(',') for i in f.readlines()]

province = []

for i in ls:
    if i[3] not in province:
        province.append(i[3])

command = input()

if command.lower() == 'total':
    num = sum([eval(i[5]) for i in ls[1:]])
    print(f'Total:{num}万元')
elif command in [str(i) for i in range(1, 101)]:
    for i in ls[1:]:
        if eval(i[0]) == eval(command):
            print(' '.join(i))
elif command in province:
    for i in ls:
        if command in i:
            print(' '.join(i[:4]))
else:
    print('No Record')