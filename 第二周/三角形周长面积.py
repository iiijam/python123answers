import math as m
class Solution:
    def calc(self, A, B, C) -> float:
        cir = (A + B + C) / 2
        area = format((m.sqrt(cir * (cir - A) * (cir - B) * (cir - C))), '.2f')
        print('周长=' + format((A + B + C), '.2f'))
        print('面积=' + area)

a = eval(input())
b = eval(input())
c = eval(input())
Solution().calc(a, b, c)
