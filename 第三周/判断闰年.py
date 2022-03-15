class Solution:
    def __init__(self,year):
        self.year = year
    def get_days(self):
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            print("True")
        else:
            print("False")

Solution(int(input())).get_days()