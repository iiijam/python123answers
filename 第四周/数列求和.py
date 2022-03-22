'''
用户输入一个小于10的正整数n，求1 + 12 + 123 + 1234 + …… 的前n项的和
'''

class Solution:
    def sum_of_n(self, n: int) -> int:
        value = 1
        if n == 1:
            return 1
        else:
            value = 1
            tempValue = str(value)
            for i in range(2, n + 1):
                tempValue = tempValue + str(i)
                value = value + int(tempValue)
            return value

print(Solution().sum_of_n(int(input())))