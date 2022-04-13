def say_hi_gender(full_name, gender):
    """定义一个名为say_hi_gender的有参数函数，
    根据性别gender值确定称谓，男性称为“先生”，女性称为“女士”，不确定性别时称为“先生/女士”
    返回值为替换了姓名与称谓的欢迎字符串
    例如：尊敬的李白先生，欢迎来到火星！"""
    if gender == '男':
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '先生')
    elif gender == '女':
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '女士')
    else:
        return '尊敬的{}{}，欢迎来到火星！'.format(full_name, '先生/女士')


# 函数名作为print()函数的参数，输出say_hi_gender()的返回值
person_name = input()               # 输入人名，如输入：李白
person_gender = input()             # 输入性别，如输入：男
print(say_hi_gender(person_name, person_gender))  # 调用函数，输出函数的返回值