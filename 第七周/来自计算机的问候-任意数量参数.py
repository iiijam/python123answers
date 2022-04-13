def say_hi_multi_parameter(*names):    # 括号里填空
    """定义一个不定参数传递函数，可接收不限数量的参数。"""
    for name in names:                         # 遍历输出，观察结果
        print('{}，你好！'.format(name))


say_hi_multi_parameter('孟浩然')
say_hi_multi_parameter('杜甫', '李白', '柳宗元', '李商隐')