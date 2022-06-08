'''
在一组空格分隔的自然数中，有些数出现的次数与该数相等，找出符合这个特征的数，并输出其中的最大数。如果不存在这样的数，则输出-1'''
import collections

numbers = collections.Counter(input().split())
ls = []
for i in numbers:
    if numbers[i] == int(i):
        ls.append(int(i))

print(max(ls) if ls else -1)