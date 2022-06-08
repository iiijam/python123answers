'''
输入两个整数，在这两个整数组成的闭区间范围内生成100个随机整数，并统计出现数据的次数，出现0次的数字不输出（而不是输出0）。为满足评测需要，程序必须使用seed函数将随机种子设为10，并使用randint函数生成随机数。
'''

import random

random.seed(10)

start, end = map(int, input().split())

memo = {}

for i in range(100):
    num = random.randint(start, end)
    if num in memo:
        memo[num] += 1
    else:
        memo[num] = 1

memo = sorted(memo.items(), key=lambda x: x[0])

for number in memo:
    print(number[0], number[1])
    