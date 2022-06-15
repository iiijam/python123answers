import string


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，
    只保留文件中的英文字母和西文符号，
    过滤掉中文(中文字符及全角符号Unicode编码都大于256)
    将所有字符转为小写，
    将其中所有标点、符号替换为空格，返回字符串
    """
    with open(file, 'r', encoding='utf-8') as data:
        text = data.read()
        new_text = ''
        for i in text:
            if(ord(i) < 256):
                new_text += i
        new_text = new_text.lower()
        list_of_deldete = ['.', ',', '\"', '\'', ':', '!', '-', '?', '~', ';']
        for i in list_of_deldete:
            new_text = new_text.replace(i, ' ')
        return new_text


def count_of_words(txt):
    """接收去除标点、符号的字符串，统计并返回其中单词数量和不重复的单词数量"""
    word_list = txt.split()
    word_set = set(word_list)
    return len(word_list), len(word_set)


def word_frequency(txt):
    """接收去除标点、符号的字符串，统计并返回每个单词出现的次数
    返回值为字典类型，单词为键，对应出现的次数为值"""
    word_list = txt.split()
    memo = {}
    for word in word_list:
        if word in memo:
            memo[word] += 1
        else:
            memo[word] = 1

    return memo


def top_ten_words(frequency, cnt):
    """接收词频字典，输出出现次数最多的cnt个单词及其出现次数"""
    word_sort = sorted(frequency.items(),
                       key=lambda x: x[1], reverse=True)  # 根据词频降序排序
    for i in range(cnt):
        print(word_sort[i][0], word_sort[i][1])


def top_ten_words_no_excludes(frequency, cnt):
    """接收词频字典，去除常见的冠词、代词、系动词和连接词后，输出出现次数最多的
    cnt个单词及其出现次数，需排除的单词如下：
    """
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we',
                      'or', 'is', 'was', 'do', 'and', 'at', 'to', 'of', 'it', 'on', 'that', 'her',
                      'c', 'in', 'you', 'had', 's', 'with', 'for', 't', 'but', 'as', 'not', 'they',
                      'be', 'were', 'so', 'our', 'all', 'would', 'if', 'him', 'from', 'no', 'me',
                      'could', 'when', 'there', 'them', 'about', 'this', 'their', 'up', 'been',
                      'by', 'out', 'did', 'have']
    word_sort = sorted(frequency.items(),
                       key=lambda x: x[1], reverse=True)  # 根据词频降序排序
    for i in word_sort[:]:
        if i[0] in excludes_words:
            word_sort.remove(i)
    for i in range(cnt):
        print(word_sort[i][0], word_sort[i][1])


if __name__ == '__main__':
    filename = "Who Moved My Cheese.txt"  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    frequency_result = word_frequency(content)  # 统计词频
    cmd = input()
    if cmd == '1':
        n = int(input())
        print(content[:n])
    elif cmd == '2':
        amount_results = count_of_words(content)
        print('文章共有单词{}个，其中不重复单词{}个'.format(*amount_results))
    elif cmd == '3':
        n = int(input())
        top_ten_words(frequency_result, n)
    elif cmd == '4':
        n = int(input())
        top_ten_words_no_excludes(frequency_result, n)
