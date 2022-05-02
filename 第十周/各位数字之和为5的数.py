'''
输入一个1000以内的正整数 n,在同一行内输出 [0,n] 之间各位数字之和为5的数，数字之间用空格分开（行末有一个空格）。
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(n+1):
        if sum(map(int, str(i))) == 5:
            print(i, end=' ')