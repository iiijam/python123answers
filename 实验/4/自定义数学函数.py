def choose_function(no):
    """接收一个字符串为参数，根据参数值判断问题类型，调用合适的函数进行操作。"""
    if no == 'pow':       # 调用pow()函数，并输出其返回值
        x = float(input())
        n = int(input())
        print(pow(x, n))
    elif no == 'gcd':     # 调用gcd()函数，并输出其返回值
        a, b = map(int, input().split())
        print(gcd(a, b))
    elif no == 'lcm':     # 调用lcm()函数，并输出其返回值
        a, b = map(int, input().split())
        print(lcm(a, b))
    elif no == 'fabs':     # 调用fabs()函数，并输出其返回值
        x = eval(input())
        print(fabs(x))
    elif no == 'ceil':     # 调用ceil()函数，并输出其返回值
        x = eval(input())
        print(ceil(x))
    elif no == 'floor':     # 调用floor()函数，并输出其返回值
        x = eval(input())
        print(floor(x))
    elif no == 'factorial': # 调用factorial()函数，并输出其返回值
        n = int(input())
        print(factorial(n))
    elif no == 'fsum':     # 调用fsum()函数，并输出其返回值
        ls = list(map(eval, input().split()))
        print(fsum(ls))
    else:
        print('No such function!')
        
    
def pow(x, n):  # 幂运算函数
    """接收一个数字x和一个整数n为参数,返回x的n次幂的结果的浮点数类型
    要求使pow(1.0, x) 和 pow(x, 0.0) 总是返回 1.0"""
    result = 1.0
    for i in range(n):
        result = result * x
    return result

def gcd(a, b):
    """接收两个正整数为参数，返回两个数的最大公约数"""
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a, b):
    """接收两个正整数为参数，以整数类型返回两个数的最小公倍数"""
    s = a * b
    while a % b != 0:
        a, b = b, (a % b)
    return s // b

def fabs(x):
    if x < 0:
        return -x
    else:
        return x

def ceil(x):
    """接受一个浮点数或整数，返回大于或等于该数的最小整数"""
    if int(x) == x or x < 0:
        return int(x)
    else:
        return int(x + 1)

def floor(x):
    """接受一个浮点数或整数，返回不大于该数的最大整数"""
    if int(x) == x or x > 0:
        return int(x)
    else:
        return int(x - 1)

def factorial(n):
    """接收一个非负整数n为参数，返回n的阶乘，0的阶乘值为1"""
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def fsum(iterable):
    """接收一个元素为数值的序列为参数，以浮点数类型返回各元素之和"""
    result = 0.0
    for i in iterable:
        result = result + i
    return result

if __name__ == '__main__':
    func_name = input()
    choose_function(func_name)