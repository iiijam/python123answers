'''
月份的缩写为月份单词的前3个字母（9月为前4个），且首字母大写，以 '.' 做为缩写结束标记。
编写一个程序，用户输入一个月份单词，不论输入的单词各字符是大写还是小写，请正确输出对应月份的缩写。
当输入单词拼写错误时，输出“spelling mistake”。
'''

if __name__ == '__main__':
    s = input()
    s = s.lower()
    dict = {'january': 'Jan.', 'february': 'Feb.', 'march': 'Mar.', 'april': 'Apr.', 'may': 'May.', 'june': 'Jun.',
            'july': 'Jul.', 'august': 'Aug.', 'september': 'Sept.', 'october': 'Oct.', 'november': 'Nov.', 'december': 'Dec.'}
    if s in dict:
        print(dict[s])
    else:
        print('spelling mistake')
