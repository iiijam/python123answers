'''
已知华氏温度转换摄氏温度的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。
编写函数F2C(f)将华氏温度转换为摄氏温度，读入两个华氏温度值f1和f2，打印范围在f1~f2内，每次增加两个华氏温度刻度的速查表。
注意：如果f1>f2，则直接打印error。
'''

if __name__ == '__main__':
    f1, f2 = map(int, input().split(','))
    if f1 > f2:
        print('error')
    else:
        for i in range(f1, f2 + 1, 2):
            print('{:.0f} : {:.2f}'.format(i, 5 * (i - 32) / 9))