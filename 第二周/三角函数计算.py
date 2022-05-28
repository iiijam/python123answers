import math as m

class Solution:
    def calcTriFunc(self, a, b) -> float:
        return ((m.sqrt(2 * a * m.sin(m.pi / 3) * m.cos(m.pi / 3)) - b) / (2 * a))

a = eval(input())
b = eval(input())
print(Solution().calcTriFunc(a, b))
