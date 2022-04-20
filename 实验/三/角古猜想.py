'''
一个正整数,若为偶数,则把它除以2,若为大于 1 的奇数,则把它乘以3加1。经过如此有限次运算后,可以得到整数1。
求经过多少次运算可得到整数1。
第一行依次输出从n开始每步的运算结果,每步的输出后跟一个空格
第二行输出总的运算次数
若输入数据不是正整数,输出'ERROR'
'''


from doctest import ELLIPSIS_MARKER


def main():
    n = eval(input())
    if type(n) != int or n < 1:
        print('ERROR')
    else:
        print(n, end=' ')
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n // 2
                print(n, end=' ')
            else:
                n = n * 3 + 1
                print(n, end=' ')
        print('\n' + str(count))

if __name__ == '__main__':
    main()