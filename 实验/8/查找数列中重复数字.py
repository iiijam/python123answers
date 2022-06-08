'''
在一个无序的整数序列中，存在多个重复的数据（出现次数超过1次），用列表的形式将这些重复的数据从小到大输出。
'''

import collections

numbers = collections.Counter(input().split())
ls = []
for i in numbers:
    if numbers[i] != 1:
        ls.append(int(i))
ls.sort(reverse=False)
print(ls)