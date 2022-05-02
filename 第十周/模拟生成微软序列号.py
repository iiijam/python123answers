'''
微软产品一般都一个25位的序列号，是用来区分每份微软产品的产品序列号。产品序列号由五组被“-”分隔开，由字母数字混合编制的字符串组成，每组字符串是由五个字符串组成。如： 36XJE-86JVF-MTY62-7Q97Q-6BWJ2 每个字符是取自于以下24个字母及数字之中的一个： B C E F G H J K M P Q R T V W X Y 2 3 4 6 7 8 9 采用这24个字符的原因是为了避免混淆相似的字母和数字，如I 和1，O 和0等，避免产生不必要的麻烦。 随机数种子函数语法为：random.seed(n)
本题要求应用random.choice()方法每次获得一个随机字符！！！
在2行中各输入一个正整数：
第1个整数代表要生成的序列号的个数
第2个正整数代表随机数种子
指定个数的序列号
'''

import random
if __name__ == '__main__':
    times = int(input())
    s = int(input())
    random.seed(s)
    
    for i in range(times):
        password = ''
        for j in range(5):
            for i in range(5):
                password += random.choice('BCEFGHJKMPQRTVWXY2346789')
            password += '-'
            if j == 4:
                password = password[:-1]
        print(password)