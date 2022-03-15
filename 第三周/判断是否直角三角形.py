class Solution:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def judgeTriangle(self) -> None:
        tempList = [self.a,self.b,self.c]
        tempList.sort()
        self.a = tempList[0]
        self.b = tempList[1]
        self.c = tempList[2]
        if self.a ** 2 + self.b ** 2 == self.c ** 2 and self.a > 0 and self.b > 0 and self.c > 0:
            print('YES')
        else:
            print('NO')

Solution(eval(input()),eval(input()),eval(input())).judgeTriangle()