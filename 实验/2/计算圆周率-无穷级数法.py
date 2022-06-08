def leibniz_of_pi(error: float) -> float:
    '''接收用户输入的浮点数阈值为参数，返回圆周率值
    一个正浮点数error，限定级数法求解pi值时，迭代累加只加绝对值大于error的项。
    编程用(-1) ** n / (2 * n + 1)公式计算π值，输入一个小数作为阈值，当最后一项的绝对值小于给定阈值时停止计算并输出得到的π值。'''
    pi = 0
    n = 0
    while True:
        current = (-1) ** n / (2 * n + 1)
        pi += current
        n += 1
        #当最后一项的绝对值小于给定阈值时停止计算并输出得到的π值。
        if abs((-1) ** n / (2 * n + 1)) < error:
            break

    return pi * 4

if __name__ == '__main__':
    threshold = float(input())
    print("{:.8f}".format(leibniz_of_pi(threshold))) #保留小数点后八位