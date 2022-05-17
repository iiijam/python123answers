'''
输入一个非空字符串，去除重复的字符后，从小到大排序输出为一个新字符串。
'''

if __name__ == '__main__':
    s = input()
    l = list(set(s))
    l.sort()
    print(''.join(l))