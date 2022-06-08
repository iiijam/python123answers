def menu():
    print('''\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存''')


dic = {'张自强': ['12652141777', '材料'], '庚同硕': [
    '14388240417', '自动化'], '王岩': ['11277291473', '文法']}
print(dic)
menu()
command = int(input())
if command == 4:
    item = input()
    if item in dic:
        print(f'{item} {dic[item][0]} {dic[item][1]}')
        print("Success")
        print(dic)
    else:
        print('No Record')
        print(dic)
else:
    print('ERROR')
