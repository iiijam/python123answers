import jieba

command = input()

excludeWordList = ['不错', '比较', '可以', '感觉', '没有', '我们', '就是', '还是', '非常', '但是', '不过', '有点', '一个', '一般', '下次', '携程', '不是', '晚上', '而且', '他们', '什么', '不好', '时候', '知道', '这样',
                   '这个', '还有', '总体', '位置', '客人', '因为', '如果', '这里', '很多', '选择', '居然', '不能', '实在', '不会', '这家', '结果', '发现', '竟然', '已经', '自己', '问题', '不要', '地方', '只有', '第二天', '酒店', '房间', '虽然']

with open('comment.csv', 'r', encoding='GBK') as f:
    ls = [i.strip().split(',', maxsplit=1) for i in f.readlines()[1:]]


if command == '总评':
    # 如果n为’总评‘，分别输出该文件评论总数，好评条数，差评条数，输出格式参照示例一。
    print('总评论:', len(ls))
    print('好评:', len([i for i in ls if i[0] == '1']))
    print('差评:', len([i for i in ls if i[0] == '0']))

elif command == '平均':
    # 如果n为’平均‘，输出该文件中所有评论内容的平均长度（不需要排除字母，标点符号和数字），输出四舍五入后的整数，输出格式参照示例二。
    print(round(sum([len(i[1]) for i in ls])/len(ls)))


elif command == '好评':
    # 如果n为’好评‘，对文件中所有好评进行词频分析，并输出词频出现最多的前15个词以及出现次数，输出格式参照示例三
    lsOfPositiveComment = [i[1] for i in ls if i[0] == '1']
    memo = {}
    for comment in lsOfPositiveComment:
        for word in jieba.lcut(comment):
            if word not in excludeWordList and len(word) > 1 and word.isalpha():
                if word in memo:
                    memo[word] += 1
                else:
                    memo[word] = 1
    memo = sorted(memo.items(), key=lambda x: x[1], reverse=True)
    for i in range(15):
        word = memo[i][0]
        count = memo[i][1]
        print(f'{word}: {count}')


elif command == '差评':
    # 如果n为’差评‘，对文件中所有差评进行词频分析，并输出词频出现最多的前15个词以及出现次数，输出格式参照示例四
    lsOfNegativeComment = [i[1] for i in ls if i[0] == '0']
    memo = {}
    for comment in lsOfNegativeComment:
        for word in jieba.lcut(comment):
            if word not in excludeWordList and len(word) > 1 and word.isalpha():
                if word in memo:
                    memo[word] += 1
                else:
                    memo[word] = 1
    memo = sorted(memo.items(), key=lambda x: x[1], reverse=True)
    for i in range(15):
        word = memo[i][0]
        count = memo[i][1]
        print(f'{word}: {count}')

else:
    # 如果n非以上输入，输出’无数据‘，格式参照示例五
    print('无数据')
