'''
输入一个字符串
输入是'record'，统计输出图书数据的总数量，格式见示例
输入是'rank'，需要再输入一个书籍编号，分别输出编号对应的书籍信息（编号,书名,出版社,现价,原价,评论数,推荐指数），格式见示例
输入是'maxcomment'，输出评论数量最多的10本书的书名和评论数，按评论数量降序排序，格式见示例
输入是'maxname'，需要再输入一个数值n，输出书名最长的n本书的名字，按书名长度降序排序，格式见示例
非以上输入，输出'无数据'
'''
command = input()
ls = []
with open("CBOOK.csv", 'r', encoding='gbk') as f:
    ls = f.readlines()
    if command == 'record':
        print(len(ls)-1)
    elif command == 'rank':
        book_id = input()
        for i in ls:
            row = list(i.strip().split(','))
            if book_id == row[0]:
                for j in row:
                    print(j)
    elif command == 'maxcomment':
        temp = []
        for i in ls[1:]:
            row = list(i.strip().split(','))
            temp.append([row[1],row[5]])
        temp.sort(key=lambda x:eval(x[1][:-3]),reverse=True)
        for i in temp[:10]:
            print(i[0],i[1])
    elif command == 'maxname':
        n = int(input())
        temp = []
        for i in ls[1:]:
            row = list(i.strip().split(','))
            temp.append([row[1],row[3]])
        temp.sort(key=lambda x:(len(x[0]),eval(x[1])),reverse=True)
        for i in temp[:n]:
            print(i[0])
    else:
        print('无数据')