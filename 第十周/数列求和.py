'''
给定某数字A（1≤A≤9）以及非负整数N，求数列之和S=A+AA+AAA+⋯+AA⋯A（N个A）。例如A=1, N=3时，1+11+111=123。
'''

if __name__ == '__main__':
    A = int(input())
    N = int(input())
    sum = 0
    if A > 0 and A < 10 and N > -1:
        for i in range(1,N+1):
            cur = int(str(A) * i)
            sum += cur
        print(sum)
    else:
        print('data error')