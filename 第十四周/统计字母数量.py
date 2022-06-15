'''
描述 读取附件是一篇英文短文，请编写程序统计这篇短文前 n 行中每一个英文字母出现的次数，结果按次数降序排列，次数相同时，按字母表顺序输出。若 n 值大于短文行数，输出整篇文章中每一个英文字母出现的次数（大写字母按小写字母统计）。
输入格式 输入一个正整数 n
输出格式 分行输出每个字母的数量，数量占3个字符宽度，居右对齐（参考示例输出）
'''

ls = []
with open('The Old Man and the Sea.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ls.append(i.strip())

times = int(input())
if times > len(ls):
    times = len(ls)
memo = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}
for i in range(times):
    lineText = ls[i]
    for char in lineText.lower():
        if char in memo:
            memo[char] += 1

answer = []
for key in memo:
    answer.append([memo[key], key])
answer.sort(key=lambda x: x[0], reverse=True)

for item in answer:
    char = item[1]
    times = item[0]
    print(f'{char} 的数量是 {times:>3} 个')
