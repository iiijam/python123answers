'''
输入一个8位数表示的年月日，读出月份数字并输出该月有多少天。
'''


def is_leap(year):
    # 判断year是否为闰年，闰年返回True，非闰年返回False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def days_of_month(date_str):
# 根据输入的年月日，返回该月的天数
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    else:
        return 0


if __name__ == '__main__':
    date_in = input()  # 输入一个年月日
    print(days_of_month(date_in))