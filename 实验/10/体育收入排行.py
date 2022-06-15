command = input()

with open('2012-19sport.csv', 'r', encoding='utf-8') as f:
    ls = [i.strip().split(',') for i in f.readlines()[1:]]

if command.isdigit() and int(command) in range(2012, 2020):
    # 某年的收入排名前若干名选手

    # 如果输入n是2012-19之间的年份，则可以输入整数k，输出n年的前k名排名信息。
    year = int(command)
    lsOfInputedYear = [i for i in ls if i[-1] == str(year)]

    # 如果k大于当年排名运动员人数，则输出当年所有的信息。
    topK = int(input())
    if topK > len(lsOfInputedYear):
        topK = len(lsOfInputedYear)

    # 每行一名运动员信息，以' | '间隔该行各项信息。
    for item in lsOfInputedYear[:topK]:
        item[0] = item[0].replace('#', '')
        print(' | '.join(item))

elif command.upper() == 'SPORT':
    # 某年属于某个运动项目的所有运动员信息，和收入总和

    # 如果输入的是'sport'（不区分大小写），则可以继续输入一个年份，输出一个当年排行中的运动项目菜单，按照字符串升序排列，格式见示例，
    year = int(input())
    lsOfInputedYear = [i for i in ls if i[-1] == str(year)]
    events = list(set([i[5] for i in lsOfInputedYear]))
    events.sort()
    for num, item in enumerate(events):
        print(f'{num+1}: {item}')

    # 再输入运动项目对应的数字来输出该项运动当年的运动员数据，每行一名运动员信息，以' | '间隔该行各项信息。
    eventNum = int(input())
    event = events[eventNum-1]
    lsOfSpecifiedEvent = [i for i in lsOfInputedYear if i[5] == event]
    for item in lsOfSpecifiedEvent:
        item[0] = item[0].replace('#', '')
        print(' | '.join(item))

    # 最后输出该项运动n年的表中收入总和，格式为'TOTAL: ${:.2f} M'
    for item in lsOfSpecifiedEvent:
        item[2] = item[2].replace('$', '')
        item[2] = item[2].replace(' M', '')
    total = sum([float(i[2]) for i in lsOfSpecifiedEvent])
    print(f'TOTAL: ${total:.2f} M')

else:
    print('Wrong Input')
