'''
n由用户输入(n>0), 1-(1/2)+(2/3)-(3/5)+(4/8)-(5/13)+...的前n项和, 结果用str.format()方法保留小数点后6位数字输出。
'''

class Solution:

    def __fib(x):
        # a function can return 1 1 2 3 5 8 13 21 34 55 89...
        if x == 1 or x == 2:
            return 1
        else:
            return Solution.__fib(x-1) + Solution.__fib(x-2)

    def sum_series(n):
        if n == 1:
            return 1
        else:
            sum = 1
            for i in range(2, n + 1):
                if i % 2 == 0:
                    sum = sum - ((i - 1) / Solution.__fib(i+1))
                else:
                    sum = sum + ((i - 1) / Solution.__fib(i+1))
            return sum

print('{}'.format('%.6f' % Solution.sum_series(eval(input()))))
