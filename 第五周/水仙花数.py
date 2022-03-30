'''
水仙花数是指一个 3 位数，它的每个位上的数字的 3 次幂之和等于它本身,输出所有3位的水仙花数。
'''

class Solution:
    def get_result(self):
        for i in range(100, 1000):
            a = i // 100
            b = i // 10 % 10
            c = i % 10
            if i == a ** 3 + b ** 3 + c ** 3:
                print(i)

Solution().get_result()