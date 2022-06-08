'''
输入一个正整数n，统计从[0,n]之间的最大的10个素数之和。本题保证测试用例至少有10个满足条件的素数。
例如：输入31 ，应求得3，5，7，11，13，17，19，23，29，31之和。
输出形式为：3+5+...+31=158
'''

def isprime(n:int) -> bool:  #判断素数函数
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def f(n:int) -> str:        #找小于n的素数并求和
    temp = []
    k = 0
    processList = []
    processString = ''
    for i in range(n+1, 2, -1):
        if isprime(i):
            temp.append(i)
            k += 1
            processList.append(str(i))
            if k == 10:
                processList.reverse()
                for j in processList:
                    processString += (j + '+')
                processString = processString[:-1]
                processString += '=' + str(sum(temp))
                break
    return processString

p=int(input())
print(f(p))