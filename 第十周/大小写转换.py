'''
编写程序，用户输入一个字符串，将其中小写字母全部转换成大写字母，把大写字母全部转换成小写字母，其他字符不变输出。
'''

if __name__ == '__main__':
    oldString = input()
    newSrtring = ''
    for i in oldString:
        if i.isupper():
            newSrtring += i.lower()
        elif i.islower():
            newSrtring += i.upper()
        else:
            newSrtring += i

    print(newSrtring)