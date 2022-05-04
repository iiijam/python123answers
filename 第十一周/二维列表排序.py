'''
有以下两个二维列表，第一个列表的元素是元组，请对其按列表元素的第 2 个元素值从小到大进行排序输出，输出其前 m 项；
第二个列表的元素仍是列表，请对其分别按每个元素的第 1 和第 3 个元素值从小到大进行排序，输出其前 n 项。
m 和 n 是由用户输入的非负整数，当 m 或 n 大于列表长度时，对整个列表进行排序输出。
'''

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    list1 = [('dungeon',7),('winterfell',4),('bran',9),('meelo',6)]
    list2 = [[ 'Angle', '0121701100106',99], [ 'Jack', '0121701100107',86], [ 'Tom', '0121701100109',65], [ 'Smith', '0121701100111', 100], ['Bob', '0121701100115',77], ['Lily', '0121701100117', 59]]
    list1.sort(key=lambda x:x[1])
    print(list1[:m])
    list2.sort(key=lambda x:x[0])
    print(list2[:n])
    list2.sort(key=lambda x:x[2])
    print(list2[:n])
