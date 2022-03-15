#今年多少天？
'''
闰年366天，其他年份365天。普通年（不能被100整除的年份）能被4整除的为闰年。（如2004年就是闰年,1999年不是闰年）；
世纪年（能被100整除的年份）能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)；
用户输入一个正整数，代表年份，输出该年有多少天？
'''

class Solution:
    def __init__(self,year):
        self.year = year
    def get_days(self) -> None:
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            print("366")
        else:
            print("365")

Solution(int(input())).get_days()