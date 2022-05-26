'''
输出英文句子中每个单词的中文意思，每行一个单词，单词字母转小写，'s 用 is 替换，n't 用 not 替换，单词与意义间用空格分隔，当查询的词在文件中不存在时，输出 '自己猜'
'''

import re

engSentence=input().lower()
engSentence=engSentence.replace("n't",' not')
engSentence=engSentence.replace("'s",' is')

#replace all punctuations in the sentence with space using re
engSentence=re.sub(r'[^a-zA-Z0-9\s]',' ',engSentence)

ls=engSentence.split()
dic={}

with open('dicts.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lt=line.split()
        dic[lt[0]]=' '.join(lt[1:])

    for i in ls:
        if i in dic:
            print(i,dic[i])
        else:
            print(i,'自己猜')