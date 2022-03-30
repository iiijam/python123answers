'''
我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？
'''

class Solution:
    def get_result():
        #return all possible results
        chickenNum = 100
        for chickenW in range(1, chickenNum + 1):
            for chickenM in range(1, chickenNum + 1):
                chickenC = chickenNum - chickenW - chickenM
                if chickenW * 5 + chickenM * 3 + chickenC / 3 == chickenNum:
                    print(chickenW, chickenM, chickenC, sep=' ')
        return None


Solution.get_result()