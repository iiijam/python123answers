'''
定义一个函数say_hi_person()，
有一个参数full_name，接受人名的字符串为参数，
函数的返回值为“***，你好！”，
例如函数的参数为“李白”，返回值为“李白，你好！”。
'''

def say_hi_person(full_name) -> str:
    return full_name + '，你好！'


person_name = input()
print(say_hi_person(person_name))