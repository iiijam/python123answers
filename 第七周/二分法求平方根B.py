'''
设计一个用二分法计算一个大于或等于 0 的实数 n 的平方根的函数sqrt_binary(n)，实数 n和计算精度控制由用户在同一行内输入，用逗号进行分隔，输出结果保留8位小数。
当(abs(x * x - n) )小于或等于设定的精度时，近似认为 x * x == n。
注：初始区间取[0,n+0.25]
在同行内输入一个实数 n（大于或等于0）和一个代表精度的数字（可用1e-m格式输入），逗号间隔
第一行输出用自己设计的函数计算得到的平方根
第二行输出用math库开平方函数计算得到的平方根
'''
import math

class Solution:
    def __init__(self, n, epsilon):
        self.n = n
        self.epsilon = epsilon
        self.low = 0
        self.high = n + 0.25
        self.mid = (self.low + self.high) / 2
        self.mid_square = self.mid * self.mid
        self.low_square = self.low * self.low
        self.high_square = self.high * self.high

    def sqrt_binary(self):
        while abs(self.mid_square - self.n) > self.epsilon:
            if self.mid_square < self.n:
                self.low = self.mid
            else:
                self.high = self.mid
            self.mid = (self.low + self.high) / 2
            self.mid_square = self.mid * self.mid
        return '{}'.format('%.8f' % self.mid)

    def sqrt_math(self):
        return '{}'.format('%.8f' % math.sqrt(self.n))


if __name__ == '__main__':
    n, epsilon = input().split(',')
    n = float(n)
    epsilon = float(epsilon)
    solution = Solution(n, epsilon)
    print(solution.sqrt_binary())
    print(solution.sqrt_math())
