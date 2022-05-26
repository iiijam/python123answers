'''给定一个整数列表 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的列表索引。
每种输入只需要对应一个答案。但是，你不能重复使用这个数组中同样位置的元素。
如果没找到解，输出“Fail”'''

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    hashTable = {}
    for index,num in enumerate(nums):
        if num in hashTable:
            continue
        hashTable[num] = index
    for i,num in enumerate(nums):
        j = hashTable.get(target-num)
        if j != None and j != i:
            ls = [i,j]
            print(' '.join(map(str,sorted(ls))))
            break
    else:
        print('Fail')