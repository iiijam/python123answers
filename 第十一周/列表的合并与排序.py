'''
读入两行，两行的格式一样，都是用空格分隔的若干个整数，将这些数合并到一个列表中，降序排列后输出整个列表。
提示： list1 = list(map(int,input().split())) #读入一行由空格分隔的整数，将其存入list1列表中
'''

if __name__ == '__main__':
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list3 = list1 + list2
    list3.sort(reverse=True)
    print(list3)