'''
编写一个学生成绩转换程序,用户输入百分制的学生成绩,
成绩大于或等于90的输出为“A”,
成绩大于或等于80且小于90的输出为“B”,
成绩大于或等于70且小于80的输出为“C”,
成绩大于或等于60且小于70的输出为“D”,
成绩小于60的输出为“E”
'''

def main():
    score = float(input())
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('E')

main()