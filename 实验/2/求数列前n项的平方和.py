'''
现有数列:1,2,3,4,……,n,计算并输出其前n项的平方和,即求：
1*1+2*2+3*3+……+n*n的和。
'''

class Solution:
    def SumSquares(self, n):
        sum = 0
        for i in range(1, n + 1):
            sum += i * i
        return sum


if __name__ == '__main__':
    print(Solution().SumSquares(eval(input())))