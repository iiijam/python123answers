'''
用户输入一个正整数，在一行内输出不大于该数的所有素数，各数后面用一个空格分隔。

'''

def PrimeMax(n):
        if n == 1:
            return 1
        else:
            for i in range(2, n):
                if n % i == 0:
                    return PrimeMax(n - 1)
            return n

max = eval(input())
listNumber = []
while True:
    if max < 2:
        break
    else:
        present = PrimeMax(max)
        listNumber.append(present)
        max = present - 1
listNumber.sort()
print(' '.join(str(x) for x in listNumber) + ' ')