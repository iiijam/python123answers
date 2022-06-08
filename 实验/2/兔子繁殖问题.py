'''
古典问题:有一对兔子,从出生后第3个月起每个月都生一对兔子,小兔子长到第三个月后每个月又生一对兔子,假如兔子都不死,
用户输入一个月份数(一个不小于2的正整数),计算并在一行内输出该月的兔子总对数以及前一个月与该月兔子数量的比值
在一行内输出两个数,数之间用空格隔开。
第一个是整数,表示本月的兔子的对数,第二个是浮点数(保留小数点后三位),表示前一个月兔子数与本月兔子数的比值。
1,1,2,3,5
'''

class Solution:
    def Rabbit(n):
        if n == 1 or n == 2:
            presentRabbit = 1
        else:
            presentRabbit = Solution.Rabbit(n - 1) + Solution.Rabbit(n - 2)
        return presentRabbit

months = eval(input())
print(Solution.Rabbit(months), '{}'.format('%.3f' % (Solution.Rabbit(months-1) / Solution.Rabbit(months))))
