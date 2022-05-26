'''
第一行输入一个正整数N, 随后的N行各输入一个形如 “Tom  18” 的字符串, 将字符串转为形如 {"name":"Tom","age":18} 的字典, 按顺序加入到列表中，得到一个元素为字典的列表
输出 根据年龄排序的列表, 根据姓名排序的列表
'''

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        name, age = input().split()
        temp = {
            "name": name,
            "age": int(age),
        }
        l.append(temp)
    l1 = sorted(l, key=lambda x: x['age'])
    l2 = sorted(l, key=lambda x: x['name'])
    print(l1)
    print(l2)