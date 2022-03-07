'''
披萨的尺寸一般分6-15英寸几种，一英寸约等于2.54厘米，将英寸直径乘以2.54即可得出以厘米为单位的直径。
例如6寸披萨，即为6乘以2.54，得出结果为15.24厘米。 
然而披萨加工时并不是严格到毫米不差的，考虑到加工过程及无效的披萨边，真正的有效直径需要去掉小数点后面数字。
例如6寸披萨的标准直径为15.24厘米，实际有效直径一般为15厘米。
披萨店经常会对顾客说：您订购的某尺寸的披萨卖完了，是否可以更换为多个小尺寸的披萨。例如：您订购的9寸披萨卖完了，可以给您2个6寸的披萨吗？
假设披萨厚度相同，价格与面积成正比，试问一个m英寸的大披萨至少要更换几个n英寸的小披萨，顾客才不吃亏？'''
class Soultion:
    def calc(self, biggerPizzaSize:int, smallerPizzaSize:int) -> int:
        x1 = int(biggerPizzaSize * 2.54)
        x2 = int(smallerPizzaSize * 2.54)
        #calculate size
        s1 = x1 * x1 * 3.14
        s2 = x2 * x2 * 3.14
        if s1 % s2 == 0:
            return int(s1 / s2)
        else:
            return int(s1 / s2) + 1

a = int(input())
b = int(input())
print(Soultion().calc(a, b))