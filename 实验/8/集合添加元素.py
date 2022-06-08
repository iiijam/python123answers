'''
向集合中加入单一元素，可以使用.add() 方法操作，该 操作将向集合中加入，返回值为“None”
'''

times = int(input())

s = set()

for i in range(times):
    country = input()
    s.add(country)

print(len(s))
