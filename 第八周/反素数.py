'''
反素数(逆向拼写的素数)是指一个将其逆向拼写后也是一个素数的非回文数。
例如：
13和31都是素数,且13和31都不是回文数,所以,13和31是反素数。
输入一个正整数n,请在同一行输出从小到大排列的的前n个反素数,每个数字后面加一个空格。
'''

def _isNotPalindrome(num):
    return str(num) != str(num)[::-1]

def _isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def getAntiPrime(n):
    i = 0
    result = []
    num = 0
    while i < n:
        numInverse = int(str(num)[::-1])
        if _isNotPalindrome(num) and _isPrime(num) and _isPrime(numInverse):
            result.append(num)
            i += 1
        num += 1
    return result

PrimeList = getAntiPrime(int(input()))
print(' '.join(map(str,PrimeList)) + ' ')