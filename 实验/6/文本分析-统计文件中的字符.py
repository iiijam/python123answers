'''
输入为一行，是一个文本文件名，如example1.txt。
输出为一行，是对名为example1.txt文件的内容进行分类统计后的结果， 输出形如：“ 大写字母m个,小写字母n个,数字o个,空格p个,其他q个 ”，具体格式见示例。
'''
import string

def read_file(file):
    """接收文件名为参数，读取文件中的数据到字符串中，返回这个字符串"""
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def classify_char(txt):
    """接收字符串为参数，依序返回大写字母、小写字母、数字、空格、和其他字符数量"""
    upper, lower, digit, space, other = 0, 0, 0, 0, 0

    import re
    pattern_upper = re.compile(r'[A-Z]')
    pattern_lower = re.compile(r'[a-z]')
    pattern_num = re.compile(r'[0-9]')
    pattern_space = re.compile(r'[ ]')
    pattern_other = re.compile(r'[^a-zA-Z0-9 ]')
    lower = len(pattern_lower.findall(text))
    upper = len(pattern_upper.findall(text))
    digit = len(pattern_num.findall(text))
    space = len(pattern_space.findall(text))
    other = len(pattern_other.findall(text))

    return upper, lower, digit, space, other

if __name__ == '__main__':
    filename = input()              # 读入文件名
    text = read_file(filename)      # 调用函数读文件中的内容为字符串
    classify = classify_char(text)  # 调用函数分类统计字符数量
    print('大写字母{}个,小写字母{}个,数字{}个,空格{}个,其他{}个'.format(*classify))