'''
输入格式 -> 每组输入包括两行 第一行是五分制的分数 第二行是一个代表学分的数字 输入 -1 时结束输入
输出格式 -> 平均绩点，严格保留两位小数
'''

if __name__ == '__main__':
    creditsMultipliedByGPA = 0
    credits = 0
    gradeAndGPAMappingTable = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.5,
        'D': 1.3,
        'D-': 1.0,
        'F': 0.0,
    }
    while True:
        inputCommand = input()
        if inputCommand == '-1':
            break
        else:
            if inputCommand in gradeAndGPAMappingTable:
                curGPA = gradeAndGPAMappingTable[inputCommand]
            else:
                curCredits = float(inputCommand)
                creditsMultipliedByGPA += curCredits * curGPA
                credits += curCredits
    print('{:.2f}'.format(creditsMultipliedByGPA / credits))