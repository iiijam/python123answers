'''
计算函数曲线在区间(a,b)与x轴包围的面积, 可将这个区域平行于y轴切分成相等宽度的小梯形, 每个梯形的面积可近似求出, 所有梯形面积的和就是函数曲线与x轴包围的面积, 
也就是函数在给定区间的积分值, dx越小, 梯形近似度越高, 计算结果越精确, 也就是说区间切分段的越多, 结果越精确。
参考下图, 计算函数sin(x)在区间(a,b)与x轴包围的面积, a,b由用户输入, 区间切分多少段也由用户输入。
输出积分值, 结果保留2位小数。
'''
import math as m
a, b = map(float, input().split())
n = int(input())
s = 0
h = abs(b-a)/n
for i in range(n):
    s += (abs(m.sin(a+i*h))+abs(m.sin(a+(i+1)*h)))*h/2
print('{:.2f}'.format(s))
