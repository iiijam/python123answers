'''
给定 2 个整数集合Ｍ和N，升序输出他们的对等差分(symmetric difference) 。 对等差分是指结果中的数据来自M或N,但不同时存在于M和N中。
'''

if __name__ == '__main__':
    mList = set(map(int, input().split()))
    nList = set(map(int, input().split()))
    finalAnswer = sorted(list(mList.symmetric_difference(nList)))
    # or finalAnswer = sorted(list(mList ^ nList))
    print(*finalAnswer , sep='\n')