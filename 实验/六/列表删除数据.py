'''
第一行输入一行以空格间隔的整数，并放入列表ls
第二行输入一个整数n
删除整数列表中的所有的n值，并输出删除后的列表
如果原输入列表中没有n，则输出‘NOT FOUND’
'''

if __name__ == '__main__':
    ls = list(map(int, input().split()))
    n = int(input())
    if n not in ls:
        print('NOT FOUND')
    else:
        while n in ls:
            ls.remove(n)
        print(ls)