'''
函数 random.shuffle(x) 可以将一个序列 x 的顺序打乱。很多人喜欢玩扑克牌，现有一手好牌，牌及顺序为：['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']，请输入一个整数 n 做为随机数种子，使用shuffle(x) 函数将牌序打乱，输出一个新的牌序。
'''
import random
if __name__ == '__main__':
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    x = int(input())
    random.seed(x)
    random.shuffle(order)
    print(order)