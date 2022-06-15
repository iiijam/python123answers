'''
描述 读取附件中的JSON文件，转为列表输出。
输入格式 输入一个正整数 n
输出格式 输出列表的前n个元素，格式如示例所示
'''

import json
itemCounter = int(input())
with open('score1034.json', 'r', encoding='utf-8') as f:
    jsonObj = json.loads(f.read())
    ls = [['姓名', '学号', 'C', 'C++', 'Java', 'Python', 'C#', '总分']]
    for i in jsonObj:
        ls.append(list(i.values()))
    print(ls[:itemCounter])