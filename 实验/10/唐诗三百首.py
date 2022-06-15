from codecs import charmap_build
import jieba
import re
with open('poem.txt', 'r', encoding='utf-8') as f:
    ls = [i.strip().split(',') for i in f.readlines()]

command = input()
poet = []
text = ''

for i in ls:
    text += i[0]
for i in ls:
    if i != ['']:
        if i[0][0].isdigit():
            poet.append(i[0].split()[0][3:])
    s = set(poet)
poetNum = 309
if command == '作者':
    n = input()
    if n.isdigit():
        n = int(n)
        memo = {}
        for i in s:
            memo[i] = poet.count(i)
        p = sorted(memo.items(), key=lambda x: (
            x[1], (-text.find(x[0]))), reverse=True)
        for i in p[:n]:
            print('{} {}'.format(i[0], i[1]))
elif command == '人物':
    n = input()
    if n.isdigit():
        n = int(n)
        txt = ''
        for i in ls:
            if i != ['']:
                if i[0][0].isdigit():
                    txt += i[0].split()[1]
                else:
                    txt = txt + i[0]
        ls1 = jieba.lcut(txt)
        poet.extend(ls1)
        memo = {}
        for i in s:
            memo[i] = poet.count(i)
        p = sorted(memo.items(), key=lambda x: (
            x[1], (-text.find(x[0]))), reverse=True)
        for i in p[:n]:
            print('{} {}'.format(i[0], i[1]))
elif command.isdigit():
    if command > '321' or command < '010':
        print('输入错误')
    elif len(command) != 3:
        print('输入错误')
    else:
        with open('poem.txt', mode='r', encoding='utf-8') as poem_file:
            content = poem_file.read()
            pattern2 = str(command) + r'(.+?)\d{3}'    # 其余通用匹配
            pattern3 = str(command) + r'(.+?)$'        # 320特殊情况
            if command != '320':
                local = re.findall(pattern2, content, re.S)[
                    0]
                print(local.split(' \n\n')[0] + ' ')   # 去除诗末俩换行
            else:
                local = re.findall(pattern3, content, re.S)[0]
                print(local)
elif command == '唐诗':
    print(f'{poetNum}')
elif command == '飞花':
    char = input()
    if len(char) == 1:
        for i in ls:
            if i != [''] and not i[0][0].isdigit():
                for j in i[0].split():
                    if char in j and len(j) <= 7:
                        print(j)
    else:
        print('输入错误')
else:
    print('输入错误')