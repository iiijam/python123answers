'''
编写一个美元与人民币转换的程序，用户输入金额和汇率(合理的汇率是正数)，输出转换为另一种货币表示的金额。
第一行输入一个以货币符号结尾的正数，数值作为金额，货币符号表明货币种类
第二行输入一个浮点数作为汇率
输入符合要求时输出一个带货币符号的数值(保留2位小数)
输入不符合要求时输出Data error!
'''

def Solution():
    text = input()
    rate = input()
    if type(eval(rate)) == float and (type(eval(text[:-1])) == float or type(eval(text[:-1])) == int) and eval(rate) > 0:
        rate = eval(rate)
        if text[-1] == '￥':
            print('%.2f' % ((eval(text[:-1])) / rate) + '$')
        elif text[-1] == '$':
            print('%.2f' % ((eval(text[:-1])) * rate) + '￥')
        else:
            print('Data error!')
    else:
        print('Data error!')

Solution()