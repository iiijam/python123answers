'''
请编一个程序，用户在同一行内输入两个整数，代表头和脚的数量，
编程计算笼中各有多少只鸡和兔（假设鸡和兔都正常，无残疾）。
如无解则输出“Data Error!
'''


class Solution:
    def get_chicken_and_rabbit(self, head, foot):
        rabbit = (foot - head * 2) / 2
        chicken = head - rabbit
        if rabbit.is_integer() and chicken.is_integer() and rabbit >= 0 and chicken >= 0:
            return '有%d只鸡，%d只兔' % (chicken, rabbit)
        else:
            return 'Data Error!'

a, b = input().split()
print(Solution().get_chicken_and_rabbit(int(a), int(b)))