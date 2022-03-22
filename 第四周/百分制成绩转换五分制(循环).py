'''
编写一个学生成绩转换程序，用户输入百分制的学生成绩，
成绩大于或等于90且小于或等于100的输出为“A”，
成绩大于或等于80且小于90的输出为“B”，
成绩大于或等于70且小于80的输出为“C”，
成绩大于或等于60且小于70的输出为“D”，
成绩小于60的输出为“E”。
输入数据不合法时输出“data error!”。
用户可反复输入成绩进行转换，输入负数时输出“end”并结束程序
'''
class Student:
    def __init__(self, score):
        self.score = score

    def convert(self):
        if self.score >= 90 and self.score <= 100:
            return 'A'
        elif self.score >= 80 and self.score < 90:
            return 'B'
        elif self.score >= 70 and self.score < 80:
            return 'C'
        elif self.score >= 60 and self.score < 70:
            return 'D'
        elif self.score >= 0 and self.score < 60:
            return 'E'
        elif self.score < 0:
            return 'end'
        else:
            return 'data error!'

while True:
    score = eval(input())
    if score < 0:
        print(Student(score).convert())
        break
    else:
        print(Student(score).convert())