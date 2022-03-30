'''
编写程序，用户输入一个字符串，以回车结束，统计字符串里英文字母、数字字符和其他字符的个数（回车符代表结束，不计入统计）。
letter = 英文字母个数, digit = 数字字符个数, other = 其他字符个数
'''

class Count:
    def __init__(self):
        self.letter = 0
        self.digit = 0
        self.other = 0

    def count(self, s):
        for i in s:
            if i.isalpha():
                self.letter += 1
            elif i.isdigit():
                self.digit += 1
            else:
                self.other += 1
        return ('letter = ' + str(self.letter) + ', digit = ' + str(self.digit) + ', other = ' + str(self.other))

print(Count().count(input()))