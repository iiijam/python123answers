'''
输入一个合数
以列表形式输出因子，各因子升序排序
'''

if __name__ == '__main__':
    num = int(input())
    l = []
    for i in range(2, num + 1):
        while num % i == 0:
            l.append(i)
            num = num / i
    print(l)