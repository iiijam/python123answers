'''

按照上面的分段函数，对输入的整数x，输出对应的y值。对于超出范围的整数x，输出“ERROR”。

本题保证测试数据中x均为整数。
'''

class Solution:
    def f(self, x):
        if x > -10 and x < 0:
            return 2 * (x ** 3) + 4 * (x ** 2) + 3
        elif x >= 0 and x < 6:
            return x + 14
        elif x >= 6 and x <= 10:
            return 6 * x 
        else:
            return 'ERROR'

print(Solution().f(int(input())))
