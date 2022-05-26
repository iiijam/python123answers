'''
输出字典原始数据 再调用menu函数输出用户选择界面 等待用户输入：
a. 输入 3 进行修改学生信息，输入姓名，如果该姓名已存在，则继续输入电话，学院信息，并输出 Success 的提示信息，如果不存在，给出 No Record 提示信息。
无论是否修改成功，结束后需要输出操作后的字典数据。
b. 如果输入其他选项，无需读入姓名，直接输出 ERROR 。 '''


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
if __name__ == '__main__':
    print(dic)
    menu()
    num = int(input())
    if num == 3 :
        name = input()
        if name in dic.keys():
            dic[name] = [input(), input()]
            print("Success")
            print(dic)
        else:
            print("No Record")
            print(dic)
    else:
        print("ERROR")
