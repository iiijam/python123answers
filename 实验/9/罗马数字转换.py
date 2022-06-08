'''
输入一个罗马数字数串，计算对应的10进制整数数值并输出。本题用例均为合法罗马数字表示（不含其他字符）
'''


class Solution:
    def romanToInt(self, s):
        a = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        for i in range(len(s)):
            if i < len(s)-1 and a[s[i]] < a[s[i+1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans


command = input()
answer = Solution().romanToInt(command)
print(answer)
