'''
18位身份证号码第7~10位为出生年份(四位数),第11~12位为出生月份,第13~14位代表出生日期,第17位代表性别,奇数为男,偶数为女。 
用户输入一个合法的身份证号,请输出用户的出生年月日和性别。（不要求较验输入的合法性）
类似以下格式输出：
出生：1995年11月11日 性别：女
'''

class Solution:
    def getInfo(id_num):
        # 获取出生年月日
        birthday = id_num[6:14]
        # 获取出生年份
        birthYear = birthday[0:4]
        # 获取出生月份
        birthMonth = birthday[4:6]
        # 获取出生日期
        birthDay = birthday[6:8]
        # 获取性别
        if int(id_num[-2]) % 2 != 0:
            gender = '男'
        else:
            gender = '女'
        return '出生：{}年{}月{}日\n性别：{}'.format(birthYear,birthMonth,birthDay,gender)


print(Solution.getInfo(input()))