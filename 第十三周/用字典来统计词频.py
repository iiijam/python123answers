'''
使用freqDict = eval(input()) 读入单词词频字典，再读入一段英文，更新词频字典后输出。
输入为两行，第一行是一个字典，形如{'hello': 12, 'world': 10}，其中存储初始的词频数据。第二行是一段英文文本。
输出一行，直接打印输出更新后的字典。
'''
if __name__ == '__main__':
    freqDict = eval(input())
    s=input().split()

    for item in s:
        freqDict[item]=freqDict.get(item,0)+1

    print(freqDict)