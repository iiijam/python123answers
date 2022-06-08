'''
第一行输入若干个整数，以空格间隔，本题保证用例中输入的数值顺序一定是从小到大，原始列表中无重复数据
第二行输入一个整数n
将整数序列放入列表ls
如果ls中已经存在n，则不插入该数，输出 'Fail'以及ls列表
若ls中可以插入n，输出插入位置，以及插入后的ls列表
'''

if __name__ == '__main__':
    ls = list(map(int, input().split()))
    n = int(input())
    if n in ls:
        print('Fail')
        print(ls)
    else:
        if n < ls[-1]:
            for i in range(len(ls)):
                if n <= ls[i]:
                    ls.insert(i,n)
                    print(i)
                    print(ls)
                    break
        else:
            ls.append(n)
            print(len(ls)-1)
            print(ls)

