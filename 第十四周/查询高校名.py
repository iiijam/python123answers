'''
附件'university.csv'中包含北京主要高校的序号、学校名称、学校标识码、主管部门、所在地、办学层次、备注等信息，以逗号分隔符。 参考提示代码，将文件内容逐行读取到列表中，根据用户输入一个关键字，查询学校名称包含用户输入关键字的学校名并输出。
'''
query = input()
ls = []
with open('university.csv', 'r', encoding='utf-8') as Uname:
    ls = Uname.readlines()

for item in ls:
    line = item.strip().split(',')
    if query in line[1]:
        print(line[1])