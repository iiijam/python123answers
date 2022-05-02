'''
输入一个英文句子，以回车符结束，单词间以空格分隔，标点符号后跟至少一个空格，统计并输出单词的个数（仅统计单词，数字按单词计，不计算标点符号，重复单词出现几次就统计几次）。
'''

if __name__ == '__main__':
    s = input()
    hashSet = {}
    for i in s.split():
        if i not in hashSet:
            hashSet[i] = 1
        else:
            hashSet[i] += 1
    sum = 0
    for word in hashSet:
        sum = sum + hashSet[word]
    print(sum)


'''
s = input()
print(len(s.split()))
'''