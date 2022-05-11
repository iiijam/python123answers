'''
我国高铁一等座车座席采用2+2方式布置,
每排设有“2+2”方式排列四个座位,以“A、C、D、F”代表,字母“A”和“F”的座位靠窗,字母“C”和“D”靠中间走道.
二等座车座席采用2+3布置,
每排设有“3+2”方式排列五个座位,以“A、B、C、D、F”代表,字母“A”和“F”的座位靠窗,字母“C”和“D”靠中间走道,“B”代表三人座中间座席。
每个车厢座位排数是1-17，字母不区分大小写。
用户输入一个数字和一个字母组成的座位号，根据字母判断位置是窗口、过道还是中间座席，输入不合法座位号时输出'输入错误'。
'''

while True:
    seat = input()
    seat = seat.upper()
    number = seat[:-1]
    if not seat[-1].isalpha() or not number.isdigit():
        print('输入错误')
    else:
        if int(number) in range(1, 17):
            if seat[-1] in 'AF':
                print('窗口')
            elif seat[-1] in 'CD':
                print('过道')
            elif seat[-1] in 'B':
                print('中间')
            else:
                print('输入错误')
        else:
            print('输入错误')
