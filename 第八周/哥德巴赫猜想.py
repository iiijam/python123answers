'''
当输入为偶数时,按照格式“N = p + q”输出N的素数分解；当输入为奇数时,输出'Data error!' 。
'''

def _isOdd(number):
    return number % 2 == 1


def _isPrime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def judge(number):
    if _isOdd(number):
        print('Data error!')
    else:
        i = 1
        while True:
            numberLeft = number - i
            if _isPrime(numberLeft) and _isPrime(i):
                print('%d = %d + %d' % (number, i, numberLeft))
                break
            i += 1

judge(int(input()))