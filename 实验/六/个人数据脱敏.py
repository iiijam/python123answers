'''
第一行输入 n，代表 n 个同学的信息
依次输入 n 行学生信息数据，每行输入一名学生的学号、姓名、电话号码，数据间以空格间隔
将学生数据脱敏后的信息保存到二维列表中，并输出这个二维表。
如果 n 不是正整数，输出’ERROR‘。（本题保证 n 是整数，且信息完整）
'''

if __name__ == '__main__':
    n = int(input())
    if n < 1:
        print('ERROR')
    else:
        student_list = []
        for i in range(n):
            student_list.append(input().split())
        for i in range(n):  
            for j in range(3):
                if j == 0:
                    if len(student_list[i][j]) == 13:
                        student_list[i][j] = student_list[i][j][0:4] + '*******' + student_list[i][j][-2:]
                    else:
                        student_list[i][j] = student_list[i][j][0:4] + '*******' + student_list[i][j][-3:]
                elif j == 1:
                    if len(student_list[i][j]) == 2:
                        student_list[i][j] = student_list[i][j][0] + '*'
                    else:
                        student_list[i][j] = student_list[i][j][0] + '*' + student_list[i][j][-1:]
                elif j == 2:
                    student_list[i][j] = student_list[i][j][0:3] + '****' + student_list[i][j][-4:]
        print(student_list)