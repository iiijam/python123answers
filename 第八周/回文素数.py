'''
回文素数是指一个数既是素数又是回文数。例如,131,既是素数又是回文数。 用户输入一个正整数 n , 请你在一行内输出从小到大排列的的前n个回文素数,数字后面用一个空格进行分隔。
'''

def _isPalindrome(num):
    return str(num) == str(num)[::-1]

def _isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def getPalindromePrime(n):
    i = 0
    result = []
    num = 0
    while i < n:
        if _isPalindrome(num) and _isPrime(num):
            result.append(num)
            i += 1
        num += 1
    return result

PalindromePrimeList = getPalindromePrime(int(input()))
print(' '.join(map(str,PalindromePrimeList)) + ' ')