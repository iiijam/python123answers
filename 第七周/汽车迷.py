'''
当用户只输入生产年份、型号时，品牌按“宝马”输出。
'''

def Car(year,model,brand = '宝马'): # 括号里补充你的代码
    return '这是一辆{}年生产，型号是{}的{}牌汽车。'.format(year,model,brand)

# 以下内容不要修改
ls = input().split()  # 根据空格切分输入字符串为列表
print(Car(*ls))       # 调用函数，取列表中的全部数据做参数