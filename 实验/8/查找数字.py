'''
输入以空格分隔的一系列数字，要求其中只有一个数字出现奇数次，其他的数都出现偶数次。找到并输出这个出现次数为奇数的数字。
'''

import collections

counterItems = collections.Counter(input().split())

for i in counterItems:
    if counterItems[i] % 2 == 1:
        print(i)
        break