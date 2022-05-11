'''
定义一个函数来判断单词m是否可以由字符串n中出现的字母来组成。
本题保证字符串中出现的字母均为小写字母，n中的字母只能使用一次。
在两行中分别输入两个字符串m,n
如果m,n 满足条件，则输出’FOUND‘ ，否则输出'NOT FOUND'
如果输入的m包含有除字母外的其他字符，输出’ERROR‘结束
'''
def f(m,n):
    #评注：哈希表模拟即可
    #定义函数体完成题目要求功能
    memo = {}
    for char in n:
        if char not in memo:
            memo[char] = 1
        else:
            memo[char] += 1

    for char in m:
        if char not in memo or memo[char] == 0:
            return 'NOT FOUND'
        else:
            memo[char] -= 1
    return 'FOUND'

m=input()
if m.isalpha():    #完成该条件分支，输入字符串n判断单词m是否可以由n中的某些字符组成
    n=input()
    print(f(m,n))
else:
    print('ERROR')