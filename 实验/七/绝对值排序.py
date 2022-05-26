'''
读入一个列表，按照绝对值从大到小排序，如果绝对值相同，则正数在前面。
例如列表[3,-4,2,4]，排序后的结果为[4,-4,3,2]
'''

if __name__ == '__main__':
    listSortedByAbs = eval(input())
    listSortedByAbs.sort(key=lambda x:(abs(x),x),reverse=True)
    '''
    This generates tuples of (abs(x),x)
    When you sort listSortedByAbs, they are sorted based on
        The first element -> abs(x)
        If the first elements are equal, then the second element -> x
    '''
    print((',').join(map(str,listSortedByAbs)))