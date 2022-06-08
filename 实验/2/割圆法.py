import math

def cutting_circle(times):      # n为分割次数
    """接收表示分割次数的整数n为参数，计算分割n次时正多边形的边数和圆周率值，返回边数和圆周率值"""
    side_length = 1 # 初始边长
    edges = 6 # 初始边数
    for i in range(times):
        side_length = math.sqrt(2 - math.sqrt(4 - side_length * side_length)) # 计算边长
        edges = edges * 2
    pi = side_length * edges / 2
    return edges, pi

if __name__ == '__main__':
    times = int(input())          # 割圆次数
    print('分割{}次，边数为{}，圆周率为{:.6f}'.format(times, *cutting_circle(times)))          # 圆周率
    print('math库中的圆周率常量值为{:.6f}'.format(math.pi))