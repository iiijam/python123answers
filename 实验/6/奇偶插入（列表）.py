'''
给定一个无序的列表A，其中数据均为非负整数，其中奇数和偶数各占一半。
当奇数和偶数个数相同时，将A中的奇数和偶数分别排序，并在放入列表时保持：
    当i是奇数时，A[i]为奇数，i为偶数时，A[i]为偶数
在一行内输入若干个非负整数，放入列表，
输出排序完成后的列表。
如果输入的数据不符合本题要求，输出‘ERROR’
本题不考虑内存限制，可使用多个列表完成操作。
'''

if __name__ == '__main__':
    ls = list(map(int, input().split()))
    oddLs = []
    evenLs = []
    for num in ls:
        if num % 2 == 1:
            oddLs.append(num)
        else:
            evenLs.append(num)

    if len(oddLs) != len(evenLs):
        print('ERROR')
    else:
        oddLs.sort()
        evenLs.sort()
        for i in range(len(ls)):
            if i % 2 == 1:
                ls[i] = oddLs[0]
                oddLs.pop(0)
            else:
                ls[i] = evenLs[0]
                evenLs.pop(0)
        print(ls)