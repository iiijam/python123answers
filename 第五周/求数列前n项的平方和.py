'''现有数列1,2,3,4...n,计算并输出其前n项的平方和;即求1*1+2*2+3*3+...+n*n的和.'''

class Solution:
    def SquareSum(n):
        if n == 1:
            return 1
        else:
            sum = 1
            for i in range(2, n + 1):
                next = i * i
                sum = sum + next
            return sum

print(Solution.SquareSum(eval(input())))