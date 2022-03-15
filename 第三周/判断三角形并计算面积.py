
class Solution:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> None:
        #get the area of triangle
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            print('NO')
        else:
            p = (self.a + self.b + self.c)/2
            print('YES')
            print('%.2f' %((p*(p-self.a)*(p-self.b)*(p-self.c))**0.5))

Solution(eval(input()),eval(input()),eval(input())).get_area()


