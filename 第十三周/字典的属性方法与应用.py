'''
dd name number:       # 在字典中加入以name为键 以number为值的元素
print:                # 输出字典
del name:             # 删除字典中以name为键的元素 当name不存在时 输出'键不存在'
update name number:   # 更新字典中以name为键的元素的值为number
value:                # 以列表形式输出字典中的所有值
key:                  # 以列表形式输出字典中所有键
clear:                # 清空字典
'''

n = int(input())
name = input().split(',')
phone = input().split(',')
MyDict = dict(zip(name, phone))

for i in range(n):
    s = input().split()

    if s[0] == 'value':
        print(list(MyDict.values()))

    elif s[0] == 'key':
        print(list(MyDict.keys()))

    elif s[0] == 'clear':
        MyDict.clear()

    elif s[0] == 'add':
        MyDict[s[1]] = s[2]

    elif s[0] == 'print':
        print(MyDict)

    elif s[0] == 'del':
        if s[1] in MyDict.keys():
            delkey = MyDict.pop(s[1])

        else:
            print('键不存在')

    elif s[0] == 'update':
        temp = {s[1]: s[2]}
        MyDict.update(temp)