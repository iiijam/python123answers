import math as m

class Solution:
    def calcQuadraticEquationOneUnknown(self, a, b, c) -> float:
        #return keep 2 digits after the decimal point
        if a == 0:
            return "a cannot be zero"
        elif b**2 - 4*a*c < 0:
            return "no real solution"
        else:
            return format((-b+m.sqrt(b*b-4*a*c))/(2*a),'.2f')

a = eval(input())
b = eval(input())
c = eval(input())
print(Solution().calcQuadraticEquationOneUnknown(a, b, c))
