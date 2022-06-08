import random

if __name__ == '__main__':
    price,seed = map(int, input().split(','))
    random.seed(seed)
    '''
    一件商品价格为 price 元，假设每位朋友帮忙砍价都是整数，最少可以砍掉0元，最多只能砍掉不超过商品标价十分之一的价钱，请问每件商品至少要多少人帮忙砍价才能0元拿？
    '''
    cur_price = price
    cur_num = 0
    while cur_price > 0:
        min_num = 0
        max_num = int(price / 10)
        # 当前价格
        discount = random.randint(min_num, max_num)
        cur_price = cur_price - discount
        cur_num += 1
    print(cur_num)