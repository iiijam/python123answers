"""定义一个名为say_hi_default的默认值函数
    根据性别gender值确定称谓，男性称为“先生”，女性称为“女士”，不确定性别时称为“先生/女士”。
    当函数调用时未给出gender时，默认按男性处理
    返回值为替换了姓名与称谓的欢迎字符串
    例如：尊敬的李白先生，欢迎来到火星！"""

def say_hi_default(full_name,gender = '男'):
    if gender == '男':
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '先生')
    elif gender == '女':
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '女士')
    else:
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '先生/女士')
    




# 函数名作为print()函数的参数，输出say_hi_default()的返回值
person_info= input().split() # 输入人名与性别，性别可省略。如输入：李白 男 或 李白
print(say_hi_default(*person_info))        # 输出：尊敬的李白先生，欢迎来到火星！
