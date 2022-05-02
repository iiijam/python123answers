'''从字符串 '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-.' 中每次随机抽取 1 个字符，重复 n 次，用取得的字符构成的一个新字符串用做密码，密码长度 n 和随机数种子 s 由用户输入。
本题必须使用random.choice()函数进行随机抽取
在一行内输入2个正整数 n 和 s，分别表示密码长度和随机数种子，数字间用半角逗号分隔。
输出一个长度为 n 字符串
'''

import random
if __name__ == '__main__':
    n, s = input().split(',')
    n = int(n)
    s = int(s)
    random.seed(s)
    password = ''
    for i in range(n):
        password += random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-.')
    print(password)

