'''
用户输入一个正整数 N，计算并输出不大于 N 的最大素数。 
'''

class Solution:
    def Prime(n):
        if n == 1:
            return 1
        else:
            for i in range(2, n):
                if n % i == 0:
                    return Solution.Prime(n - 1)
            return n

print(Solution.Prime(eval(input())))