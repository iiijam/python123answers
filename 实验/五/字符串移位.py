def f(s,n):
    '''
    定义一个函数将字符串s循环向右移动n位，n为负数时左移。
    若s为空字符串''，则不论n为多少，均输出空字符串''。
    '''
    if abs(n) > len(s) and s != '':
        n = n % len(s)
    if s == '':
        return ''
    else:
        return s[-n:] + s[:-n]

s=input()
n=int(input())
print(f(s,n))