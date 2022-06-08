'''
给定一批人的出生日期，请找出其中年龄最大的，并输出他的出生日期
'''

if __name__ == '__main__':
    answerList = []
    inputText = input()
    while inputText != '':
        inputList = []
        inputList = list(map(int,inputText.split('-')))
        inputList.append(inputText)
        answerList.append(inputList)
        inputText = input()
    
    answerList.sort(key=lambda x:(x[0],x[1],x[2]))
    print(answerList[0][3])
    