'''输入一个英文句子，每个单词间用空格分隔，标点符号前面无空格，后面跟一个空格，请按出现顺序将每个单词分行输出（标点符号归属于前面的单词）。'''

if __name__ == '__main__':
    sentence = input()
    sentence = sentence.split()
    for i in sentence:
        print(i)