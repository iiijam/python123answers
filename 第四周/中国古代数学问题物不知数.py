'''
一个正整数n,除以3余2;除以5余3;除以7余2。
现假设物品总数不超过n (n<=1000),请编程计算满足条件的n并输出。
输入为一个正整数n,题目保证 0 < n <= 1000 。
输出不超过n且满足条件的数m,如果有多个解,则分行输出,如果无解则输出"No solution!"。
'''

class Solution:
    def solve(self, n:int):
        count = 0
        newList = []
        for i in range(1, n + 1):
            if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
                count += 1
                newList.append(i)
        if newList == []:
            newList.append('No solution!')
        return newList
            
print(*Solution().solve(int(input())), sep='\n')
