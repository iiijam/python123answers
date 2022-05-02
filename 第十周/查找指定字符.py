'''
编写程序，从用户给定字符串中查找某指定的字符。
'''

if __name__ == '__main__':
    char = input()
    string = input()
    index = string.find(char)
    if index == -1:
        print('Not Found')
    else:
        print('index = {}'.format(index))