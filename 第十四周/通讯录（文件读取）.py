'''
读取附件中的csv文件（通讯录信息），放入字典中(后两项以列表形式做为字典的值)，并依次输出其中的信息。文件内数据不需要修改，输出时数据之间以空格间隔。
编码格式使用GBK
输入‘A’时，按行输出文件信息
输入‘D’时，直接输出字典内容
输入其他数据时，输出“ERROR”
'''
with open('info.csv', 'r', encoding='GBK') as f:
    f = f.read()
    command = input()

    if command == 'A':
        print(f.replace(',',' '))

    elif command == 'D':
        memo = {}
        f = f.strip().split('\n')

        for i in range(len(f)):
            f[i] = f[i].split(',')
            memo[f[i][0]] = [f[i][1],f[i][2]]
        print(memo)

    else:
        print("ERROR")