'''
输入一个正整数，计算其各个位的数字之和
'''
class Solution:
    def digitSum(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum 

print(Solution.digitSum(eval(input())))