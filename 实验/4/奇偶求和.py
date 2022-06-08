'''
输入一个完全由数字字符组成的字符串s，分别统计其中出现的奇数和偶数字符数值之和
'''

if __name__ == '__main__':
    s = input()
    odd = 0
    even = 0
    for i in s:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    print('oddsum={},evensum={}'.format(odd, even))