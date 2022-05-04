'''
输入一系列动物名和其重量，重量单位可能是kg，也可能是t，动物名、与重量间空格分隔，重量数值与单位间无分隔。 按重量由小到大排序以二维列表形式输出。
'''

if __name__ == '__main__':
    ls = []

    while True:
        data = input()
        if data == '':
            break
        ls.append(data.split())
    
    ls.sort(key=lambda weight:float(weight[1][:-1]) * 1000 if weight[1][-1] == 't' else int(weight[1][:-2]))
    print(ls)