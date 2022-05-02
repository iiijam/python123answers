'''
输入一个字符串，当输入字符串结尾是 “PY” 时，输出“YES”，否则输出“NO”。
'''

if __name__ == '__main__':
    s = input()
    if s[-2:] == 'PY':
        print('YES')
    else:
        print('NO')