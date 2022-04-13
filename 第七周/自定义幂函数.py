'''
定义一个函数实现整数的幂运算，用以计算 x 的 n 次方。
在一行内输入两个非负整数 x 和 n，数字间用空格分隔。
输出x 的 n 次幂的运算结果
'''

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x

if __name__ == '__main__':
    x, n = input().split()
    x = int(x)
    n = int(n)
    solution = Solution()
    print(solution.myPow(x, n))
