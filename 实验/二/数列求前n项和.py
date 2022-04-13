'''
输入一个正整数 n，计算并输出2/1, 3/2, 5/3, 8/5, 13/8, …的前n项之和，结果用浮点数类型表示。
'''

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def Calculate(n):
    sum = 0
    for i in range(n):
        upper = Fibonacci(i + 3)
        downer = Fibonacci(i + 2)
        sum += (upper / downer)
    return sum

print(Calculate(eval(input())))