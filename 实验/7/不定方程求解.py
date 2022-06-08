'''
给定正整数a,b,c，求不定方程ax+by=c关于未知数x和y的所有非负整数解组数并输出。
部分用例有时间限制。
'''

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    answerList = []
    aMax = c // a + 1
    for x in range(aMax):
        bMax = (c - a * x) // b + 1
        for y in range(bMax):
            if a * x + b * y == c:
                answerList.append([x, y])
    print(answerList)
    print(len(answerList))