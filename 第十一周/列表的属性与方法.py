'''
初始化一个空列表，输入一个正整数 n，你将被要求读入 n 个输入（输入形式如下所示），每得到一个输入后，根据输入进行操作。
'''
if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        command = input()
        if command == 'print':
            print(l)
        if command[0:6] == 'insert':
            pos = command.split()[1]
            value = command.split()[2]
            l.insert(int(pos), int(value))
        if command[0:4] == 'sort':
            l.sort()
        if command[0:6] == 'append':
            value = command.split()[1]
            l.append(int(value))
        if command[0:7] == 'reverse':
            l.reverse()
        if command[0:6] == 'remove':
            value = command.split()[1]
            l.remove(int(value))
        if command[0:4] == 'pop':
            l.pop()