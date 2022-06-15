'''
描述 读取附件中的文件（utf-8编码），统计并输出文章的前 n 行里共有多少字符（标点符号及换行符按字符统计），以及有多少个不重复的字符？
输入格式 输入一个正整数 n
输出格式 在一行中输出文章的前 n 行里共有多少字符和有多少个不重复的字符，中间用一个空格分隔
'''

times = int(input())
text = ''
with open('The Great Learning.txt', 'r', encoding='utf-8') as f:
    for i in range(times):
        text += f.readline()

print(f'{len(text)} {len(set(text))}')