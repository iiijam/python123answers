import string
from tkinter import W


def create_dict(filename):
    """接收表示文件名的字符串参数，读文件中的单词及释义，以单词为键，其他部分为值创建字典。
    多个释义间可能是逗号或空格分隔，但单词与第一个释义间至少有一个空格，
    将文件每一行根据空格切分一次，切分结果分别作为键和值创新字典。
    返回字典。
    """
    memo = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            word, *mean = line.split()
            mean = ' '.join(mean)
            memo[word] = mean
    return memo


def translate(dic, word):
    """接收两个参数，第一个是读文件创建的字典，第二个参数为要查询的单词，字符串
    根据文件创建的字典，从中查询单词word，
    如果查询单词存在，元组形式返回词与词的释义；
    如果查询不存在，返回'这个词我不明白'
    """
    if word in dic:
        return f'{word} {dic[word]}'
    else:
        return f'{word} 这个词我不明白'



def sentence_to_words():
    """调用此函数时，先输出提示信息'请输入查询的句子：'
    用户输入欲翻译的句子
        若输入非空时，先将"n't"替换为 ' not'、"'s"替换为 ' is'，再将标点符号替换为空格。
    根据空格将句子切分为单词的列表，调用translate逐个单词进行翻译。
    用户可重复多次输入，每输入一名翻译一句，
    若直接输入回车时，输出'查询结束，正在退出...'。然后结束程序。
    """
    command = input('请输入查询的句子：')
    while command:
        command = command.replace("n't", ' not').replace("'s", ' is')
        command = command.lower()
        command = command.translate(str.maketrans('', '', string.punctuation))
        command = command.split()
        for word in command:
            print(translate(create_dict('./dict.txt'), word))
        command = input('请输入查询的句子：')
    print('查询结束，正在退出...')




def translate_word():
    """调用此函数时，先输出提示信息：'请输入查询的单词：'
    用户可循环输入欲翻译的单词，若直接输入回车时，输出'查询结束，正在退出...'。
    输入非空时输出翻译结果
    """
    command = input('请输入查询的单词：')
    while command:
        command = command.lower()
        print(translate(create_dict('./dict.txt'), command))
        command = input('请输入查询的单词：')
    print('查询结束，正在退出...')



if __name__ == '__main__':
    file = './dict.txt'           # 表示文件名的字符串，表示位于当前路径下的'dict.txt'文件
    word_dic = create_dict(file)  # 调用函数返回字典类型的数据
    print('载入字典数据成功！查询单词请输入“1”，查询句子请输入“2”')
    choice = input()              # 输入操作选项
    if choice == '1':
        translate_word()          # 翻译单词
    elif choice == '2':
        sentence_to_words()       # 翻译句子
    else:
        print('输入错误，请重新运行程序！')
