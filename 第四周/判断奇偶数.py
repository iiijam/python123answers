'''
用户输入一个正整数，判断该数是奇数还是偶数，如果奇数输出odd，偶数则输出even。
'''

class Solution:
    def is_odd_or_even(self, num: int) -> str:
        if (num & 1) == 0:
            return 'even'
        else:
            return 'odd'

print(Solution().is_odd_or_even(int(input())))
