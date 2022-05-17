'''
输入一系列以逗号分隔的英文人名，其中包含重复的名字，请将其中重复的名字去掉，输出包含不重复人名的列表，名字出现顺序与输入顺序相同。
'''

if __name__ == '__main__':
    s = input()
    l = s.split(',')
    l2 = []
    for i in l:
        if i not in l2:
            l2.append(i)
    print(l2)