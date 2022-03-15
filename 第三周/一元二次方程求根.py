#一元二次方程求根
'''
一元二次方程ax2+bx+c=0，a、b、c的值由用户在三行中输入，
根据用户输入的数值求解方程的实数解：
如果a值 为0，根据b值判断方程是否有解并输出，如果a与b同时为0，则输出Data error!
如果方程无实数解，输出“该方程无实数解”；
如果方程有两个相同的实数解，输出一个解，结果保留2位小数；
如果方程有两个不同的实数解，在一行内按从大到小顺序输出方程的两个解，用空格分隔，结果保留2位小数。
'''

class Solution:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def get_solution(self) -> None:
        if self.a == 0:
            if self.b == 0:
                print("Data error!")
            else:
                x = -self.c/self.b
                print("%.2f" % x)
        else:
            delta = self.b**2 - 4*self.a*self.c
            if delta < 0:
                print("该方程无实数解")
            elif delta == 0:
                x = -self.b/(2*self.a)
                print("%.2f" % x)
            else:
                x1 = (-self.b + delta**0.5)/(2*self.a)
                x2 = (-self.b - delta**0.5)/(2*self.a)
                print("%.2f %.2f" % (x1,x2))

Solution(float(input()),float(input()),float(input())).get_solution()